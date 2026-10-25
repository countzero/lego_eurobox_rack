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
- node transforms round to 1e-6 m and 1e-7 of a unit quaternion, which
  deflate packs far better than float noise;
- the JSON loses its spaces and the buffer views their padding gaps.
"""

import array
import json
import os
import struct

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "web", "rack.glb")

EXPORT_COLLECTIONS = ("frame", "angles", "fasteners", "castors", "boxes", "inserts", "top_plate")
GRID = 1e-5  # m, the positions' grid
FLOAT, BYTE, SHORT = 5126, 5120, 5122
QUANT = "KHR_mesh_quantization"


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


def rounded(values, step):
    return [round(v / step) * step for v in values]


def short(values, digits):
    """Round to digits after the point and keep the shortest float that prints so."""
    return [float(f"{v:.{digits}f}") + 0.0 for v in values]


def compact(path):
    doc, old = read_glb(path)
    views, accessors = doc["bufferViews"], doc["accessors"]
    roles = {}
    for mesh in doc["meshes"]:
        for prim in mesh["primitives"]:
            for name, index in prim["attributes"].items():
                roles[index] = name
    chunks = []
    for i, acc in enumerate(accessors):
        view = views[acc["bufferView"]]
        start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
        raw = old[start:start + view["byteLength"]]
        role = roles.get(i)
        if role in ("POSITION", "NORMAL") and acc["componentType"] == FLOAT and acc["type"] == "VEC3":
            assert "byteStride" not in view, "interleaved attributes are not handled"
            vals = array.array("f")
            vals.frombytes(raw[:acc["count"] * 12])
            if role == "POSITION" and max(map(abs, vals)) <= 1.0:
                q = array.array("h")
                for k in range(0, len(vals), 3):
                    q.extend(round(v * 32767) for v in vals[k:k + 3])
                    q.append(0)
                acc["min"] = [min(q[k::4]) for k in range(3)]
                acc["max"] = [max(q[k::4]) for k in range(3)]
                raw = q.tobytes()
                acc["componentType"] = SHORT
                acc["normalized"] = True
                view["byteStride"] = 8
            elif role == "POSITION":
                vals = array.array("f", rounded(vals, GRID))
                acc["min"] = [min(vals[k::3]) for k in range(3)]
                acc["max"] = [max(vals[k::3]) for k in range(3)]
                raw = vals.tobytes()
            else:
                q = array.array("b")
                for k in range(0, len(vals), 3):
                    q.extend(max(-127, min(127, round(v * 127))) for v in vals[k:k + 3])
                    q.append(0)
                raw = q.tobytes()
                acc["componentType"] = BYTE
                acc["normalized"] = True
                view["byteStride"] = 4
        chunks.append((acc["bufferView"], raw))
    # one tightly packed buffer view per accessor, in accessor order
    binary = b""
    new_views = []
    for i, (view_index, raw) in enumerate(chunks):
        binary += b"\0" * (-len(binary) % 4)
        view = {k: v for k, v in views[view_index].items() if k not in ("byteOffset", "byteLength")}
        view.update(buffer=0, byteOffset=len(binary), byteLength=len(raw))
        new_views.append(view)
        accessors[i]["bufferView"] = i
        accessors[i].pop("byteOffset", None)
        binary += raw
    doc["bufferViews"] = new_views
    doc["buffers"] = [{"byteLength": len(binary)}]
    for node in doc["nodes"]:
        for key, digits in (("translation", 6), ("rotation", 7), ("scale", 7)):
            if key in node:
                node[key] = short(node[key], digits)
    for key in ("extensionsUsed", "extensionsRequired"):
        doc[key] = sorted(set(doc.get(key, [])) | {QUANT})
    write_glb(path, doc, binary)


def main():
    export()
    before = os.path.getsize(OUT)
    compact(OUT)
    print("wrote", OUT, before, "->", os.path.getsize(OUT), "bytes")


main()
