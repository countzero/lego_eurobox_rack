"""Export blender/rack.blend to web/rack.glb for the web viewer.

Run headless on the saved model; the .blend is never saved:
    blender --background blender/rack.blend --python-exit-code 1 --python blender/export_web.py

After Blender's exporter, compact() makes the file smaller without changing
what the viewer shows:
- normals become normalized 8-bit integers (KHR_mesh_quantization, which
  three.js's GLTFLoader reads), 4 bytes a vertex instead of 12, about half a
  degree of error;
- positions of a mesh within 1 m of its origin become normalized 16-bit
  integers, a 0.03 mm grid, 8 bytes a vertex instead of 12; the longer bars
  keep floats snapped to a 0.01 mm grid;
- every mesh's triangles are reordered for a vertex cache (tipsify) and its
  vertices numbered in the order the triangles first use them, then indices
  and vertices are stored with KHR_meshopt_compression, losslessly, by the
  meshoptimizer that ships with Blender's glTF exporter; the exporter's own
  meshopt option is not used, since it stores the attributes as filtered
  floats, which pack worse than the integers above;
- identical buffers are stored once;
- node transforms round to 1e-6 m and 1e-7 of a unit quaternion, which
  deflate packs far better than float noise;
- the JSON loses its spaces.
"""

import ctypes
import json
import os
import re
import struct

import bpy
import numpy as np
from io_scene_gltf2.io.exp import meshopt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "web", "rack.glb")

EXPORT_COLLECTIONS = ("frame", "angles", "fasteners", "castors", "boxes", "inserts", "top_plate")
GRID = 1e-5  # m, the positions' grid
FLOAT, BYTE, SHORT, USHORT, UINT = 5126, 5120, 5122, 5123, 5125
INDEX_TYPES = {5121: np.uint8, USHORT: np.uint16, UINT: np.uint32}
ARRAY_BUFFER, ELEMENT_ARRAY_BUFFER = 34962, 34963
QUANT = "KHR_mesh_quantization"
MESHOPT = "KHR_meshopt_compression"
VERTEX_CACHE = 16  # entries tipsify orders the triangles for


def export():
    for obj in bpy.data.objects:
        obj.select_set(False)
    keep = {obj for name in EXPORT_COLLECTIONS for obj in bpy.data.collections[name].all_objects}
    for obj in keep:
        obj.hide_set(False)
        obj.select_set(True)
    for coll in bpy.data.collections:
        coll.hide_viewport = False
        coll.hide_render = False
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=OUT,
        export_format="GLB",
        use_selection=True,
        export_extras=True,
        export_yup=True,
        export_apply=True,
        export_cameras=False,
        export_lights=False,
        export_animations=False,
        export_normals=True,
        export_texcoords=False,
        export_image_format="NONE",
    )


TERM = re.compile(r"^(-?[\d.e+-]+)\*clamp\(e\*(\d+)-(\d+),0,1\)$")


def explode_offsets():
    """Each object's exploded move, in glTF axes and its parent's space, as one
    offset per step: build_rack.py drives delta_location with a sum of
    `<metres>*clamp(e*<steps>-<step>,0,1)` per axis, and the exporter turns
    Blender's (x, y, z) into glTF's (x, z, -y)."""
    out = {}
    for obj in bpy.data.objects:
        ad = obj.animation_data
        if not ad:
            continue
        steps = {}
        count = 1
        for fc in ad.drivers:
            if fc.data_path != "delta_location":
                continue
            for term in fc.driver.expression.split("+"):
                found = TERM.match(term)
                assert found, fc.driver.expression
                d, count, k = float(found.group(1)), int(found.group(2)), int(found.group(3))
                steps.setdefault(k, [0.0, 0.0, 0.0])[fc.array_index] = d
        if steps:
            full = [[0.0, 0.0, 0.0] for _ in range(count)]
            for k, v in steps.items():
                full[k] = [v[0], v[2], -v[1]]
            out[obj.name] = full
    return out


def read_glb(path):
    data = open(path, "rb").read()
    jlen = struct.unpack("<I", data[12:16])[0]
    doc = json.loads(data[20:20 + jlen])
    blen = struct.unpack("<I", data[20 + jlen:24 + jlen])[0]
    return doc, data[28 + jlen:28 + jlen + blen]


def write_glb(path, doc, binary):
    js = json.dumps(doc, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    js += b" " * (-len(js) % 4)
    binary += b"\0" * (-len(binary) % 4)
    total = 12 + 8 + len(js) + 8 + len(binary)
    with open(path, "wb") as f:
        f.write(struct.pack("<III", 0x46546C67, 2, total))
        f.write(struct.pack("<II", len(js), 0x4E4F534A) + js)
        f.write(struct.pack("<II", len(binary), 0x004E4942) + binary)


def short(values, digits):
    """Round to digits after the point and keep the shortest float that prints so."""
    return [float(f"{v:.{digits}f}") + 0.0 for v in values]


def quantized(role, floats):
    """A float VEC3 attribute as the rows the file stores, one row of bytes a
    vertex, with the accessor fields that change."""
    if role == "POSITION" and np.abs(floats).max() <= 1.0:
        q = np.zeros((len(floats), 4), np.int16)
        q[:, :3] = np.round(floats * 32767)
        return q, {"componentType": SHORT, "normalized": True}
    if role == "POSITION":
        return (np.round(floats.astype(np.float64) / GRID) * GRID).astype(np.float32), {}
    q = np.zeros((len(floats), 4), np.int8)
    q[:, :3] = np.clip(np.round(floats * 127), -127, 127)
    return q, {"componentType": BYTE, "normalized": True}


def tipsify(tris, vertex_count, cache=VERTEX_CACHE):
    """Triangles reordered for a vertex cache of `cache` entries (Sander, Nehab,
    Barczak 2007, "Fast triangle reordering for vertex locality and reduced
    overdraw"), so meshopt's index codec finds the vertices it has just seen."""
    adjacent = [[] for _ in range(vertex_count)]
    for t, tri in enumerate(tris):
        for v in tri:
            adjacent[v].append(t)
    live = [len(a) for a in adjacent]
    stamp = [0] * vertex_count
    emitted = [False] * len(tris)
    out, dead_end = [], []
    time, cursor, fan = cache + 1, 0, 0
    while fan >= 0:
        candidates = []
        for t in adjacent[fan]:
            if emitted[t]:
                continue
            emitted[t] = True
            out.append(tris[t])
            for v in tris[t]:
                dead_end.append(v)
                candidates.append(v)
                live[v] -= 1
                if time - stamp[v] > cache:
                    stamp[v] = time
                    time += 1
        fan, best = -1, -1
        for v in candidates:
            if live[v] > 0:
                priority = time - stamp[v] if time - stamp[v] + 2 * live[v] <= cache else 0
                if priority > best:
                    fan, best = v, priority
        while fan < 0 and dead_end:
            v = dead_end.pop()
            if live[v] > 0:
                fan = v
        while fan < 0 and cursor < vertex_count:
            if live[cursor] > 0:
                fan = cursor
            cursor += 1
    return out


def vertex_order(indices):
    """The triangles in vertex-cache order and the vertices numbered by first use:
    (new indices, old vertex of each new number)."""
    tris = tipsify(indices.reshape(-1, 3).tolist(), int(indices.max()) + 1)
    number, old = {}, []
    for tri in tris:
        for v in tri:
            if v not in number:
                number[v] = len(old)
                old.append(v)
    flat = [number[v] for tri in tris for v in tri]
    return np.array(flat, np.uint32), np.array(old, np.int64)


class Meshopt:
    """meshoptimizer's encoder as Blender's glTF exporter ships it."""

    def __init__(self):
        settings = {"gltf_meshopt_extension": MESHOPT}
        meshopt.MeshoptEncoder.load_library(settings)
        self.lib = settings["meshopt_encoder"]

    def vertices(self, rows):
        count, stride = rows.shape
        bound = self.lib.encodeVertexBufferBound(count, stride)
        out = (ctypes.c_ubyte * bound)()
        written = self.lib.encodeVertexBuffer(out, bound, rows.ctypes.data_as(ctypes.c_void_p), count, stride)
        return bytes(out[:written])

    def triangles(self, indices):
        indices = np.ascontiguousarray(indices, np.uint32)
        bound = self.lib.encodeIndexBufferBound(len(indices), int(indices.max()) + 1)
        out = (ctypes.c_ubyte * bound)()
        written = self.lib.encodeIndexBuffer(out, bound, indices.ctypes.data_as(ctypes.c_void_p), len(indices))
        return bytes(out[:written])


def compact(path, offsets):
    doc, old = read_glb(path)
    for node in doc["nodes"]:
        if node.get("name") in offsets:
            node.setdefault("extras", {})["explode"] = [short(v, 6) for v in offsets[node["name"]]]
    views, accessors = doc["bufferViews"], doc["accessors"]

    def floats(i):
        acc = accessors[i]
        view = views[acc["bufferView"]]
        assert acc["componentType"] == FLOAT and acc["type"] == "VEC3" and "byteStride" not in view, acc
        start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
        return np.frombuffer(old, "<f4", acc["count"] * 3, start).reshape(-1, 3)

    def indices(i):
        acc = accessors[i]
        view = views[acc["bufferView"]]
        start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
        return np.frombuffer(old, INDEX_TYPES[acc["componentType"]], acc["count"], start).astype(np.uint32)

    # Every attribute goes with the index accessor of its primitives; each
    # index accessor is reordered once, so meshes that share one keep sharing.
    rows, order, owner = {}, {}, {}
    for mesh in doc["meshes"]:
        for prim in mesh["primitives"]:
            assert prim.get("mode", 4) == 4 and "indices" in prim, mesh["name"]
            assert set(prim["attributes"]) <= {"POSITION", "NORMAL"}, mesh["name"]
            ix = prim["indices"]
            if ix not in order:
                order[ix] = vertex_order(indices(ix))
            for role, a in prim["attributes"].items():
                assert owner.setdefault(a, ix) == ix, f"{mesh['name']}: {role} shared across index buffers"
                if a not in rows:
                    data, fields = quantized(role, floats(a))
                    data = np.ascontiguousarray(data[order[ix][1]])
                    accessors[a].update(fields, count=len(data))
                    if role == "POSITION":
                        xyz = data[:, :3]
                        accessors[a]["min"] = xyz.min(axis=0).tolist()
                        accessors[a]["max"] = xyz.max(axis=0).tolist()
                    rows[a] = data
    encoder = Meshopt()
    chunks = []  # (encoded bytes, extension fields, plain view fields), one per distinct buffer
    seen = {}
    for i, acc in enumerate(accessors):
        if i in order:
            new = order[i][0]
            acc.update(componentType=USHORT if new.max() < 65536 else UINT, count=len(new))
            stride = 2 if acc["componentType"] == USHORT else 4
            ext = {"byteStride": stride, "mode": "TRIANGLES", "count": len(new)}
            chunk = (encoder.triangles(new), ext, {"target": ELEMENT_ARRAY_BUFFER})
        else:
            data = rows[i]
            stride = data.strides[0]
            ext = {"byteStride": stride, "mode": "ATTRIBUTES", "count": len(data)}
            chunk = (encoder.vertices(data.view(np.uint8).reshape(len(data), stride)), ext,
                     {"byteStride": stride, "target": ARRAY_BUFFER})
        acc.pop("byteOffset", None)
        key = (chunk[0], stride, ext["mode"], ext["count"])
        if key not in seen:
            seen[key] = len(chunks)
            chunks.append(chunk)
        acc["bufferView"] = seen[key]
    # The compressed bytes fill the GLB's binary chunk, buffer 0; buffer 1 holds
    # no data and only gives the decoded views their place.
    binary, fallback, new_views = b"", 0, []
    for data, ext, plain in chunks:
        binary += b"\0" * (-len(binary) % 4)
        size = ext["byteStride"] * ext["count"]
        new_views.append({"buffer": 1, "byteOffset": fallback, "byteLength": size, **plain,
                          "extensions": {MESHOPT: {"buffer": 0, "byteOffset": len(binary),
                                                   "byteLength": len(data), **ext}}})
        binary += data
        fallback += size + (-size % 4)
    binary += b"\0" * (-len(binary) % 4)
    doc["bufferViews"] = new_views
    doc["buffers"] = [{"byteLength": len(binary)},
                      {"byteLength": fallback, "extensions": {MESHOPT: {"fallback": True}}}]
    for node in doc["nodes"]:
        for key, digits in (("translation", 6), ("rotation", 7), ("scale", 7)):
            if key in node:
                node[key] = short(node[key], digits)
    for key in ("extensionsUsed", "extensionsRequired"):
        doc[key] = sorted(set(doc.get(key, [])) | {QUANT, MESHOPT})
    write_glb(path, doc, binary)


def main():
    bpy.context.scene["explode"] = 0.0
    bpy.context.view_layer.update()
    offsets = explode_offsets()
    export()
    before = os.path.getsize(OUT)
    compact(OUT, offsets)
    print("wrote", OUT, before, "->", os.path.getsize(OUT), "bytes")


main()
