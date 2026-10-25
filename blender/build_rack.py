"""Build the LEGO Eurobox rack from design/rack.json, save rack.blend, render.

Run headless from the repository root:
    blender --background --factory-startup --python-exit-code 1 --python blender/build_rack.py

Every structural dimension comes from design/rack.json (millimetres); the
model is in metres. Only visual details (slot depth, castor shape, edge
rounds, colours, cameras, lights) are set here. The renders use EEVEE
with screen-space ray tracing at fixed settings.
"""

import json
import math
import os
import struct

import bmesh
import bpy
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RACK = json.load(open(os.path.join(ROOT, "design", "rack.json"), encoding="utf-8"))
RENDERS = os.path.join(ROOT, "renders")


def m(mm):
    return mm / 1000.0


# Visual details only.
SLOT_WIDTH = 8.0
SLOT_DEPTH = 6.0
INSERT_WALL = 1.5
STAGE_GAP = 50.0  # mm between the box rows in the inserts top view
CORNER_SEGMENTS = 6
BOX_EDGE_ROUND = 0.8  # mm
CLIP_EDGE_ROUND = 0.5
INSERT_EDGE_ROUND = 0.4
SHARP_ANGLE = math.radians(30)
# The insert sets fill the published inner top (266 in 265 ± 5), so a tray may
# overlap the drawn wall by this much.
INSERT_FIT_TOLERANCE = 1.0
EEVEE_SAMPLES = 64
# (linear colour, metallic, roughness, IOR); IOR 1.49 for PP, 1.59 for PS.
COLOURS = {
    "aluminium": ((0.62, 0.64, 0.66, 1), 1.0, 0.55, 1.5),
    "box_anthracite": ((0.040, 0.041, 0.043, 1), 0.0, 0.5, 1.49),
    "insert_grey": ((0.22, 0.23, 0.24, 1), 0.0, 0.4, 1.59),
    "castor": ((0.06, 0.06, 0.07, 1), 0.0, 0.6, 1.5),
    "steel": ((0.70, 0.71, 0.72, 1), 1.0, 0.35, 1.5),  # zinc-plated
    "cap_black": ((0.02, 0.02, 0.02, 1), 0.0, 0.5, 1.5),
    "plywood": ((0.609, 0.331, 0.117, 1), 0.0, 0.55, 1.5),  # linear mean of PLY_FACE
    "floor": ((0.45, 0.45, 0.45, 1), 0.0, 0.85, 1.5),
}
CLIP_ROUGHNESS = 0.35
GRAINED = ("box_anthracite",)  # fine moulding grain as bump; not in the glb


# ---------------------------------------------------------------- scene setup

def reset_scene():
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.materials,
                 bpy.data.cameras, bpy.data.lights, bpy.data.collections):
        for item in list(coll):
            coll.remove(item)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.length_unit = "MILLIMETERS"
    return scene


def srgb_to_linear(hex_colour):
    def channel(c):
        c = int(c, 16) / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    h = hex_colour.lstrip("#")
    return tuple(channel(h[i:i + 2]) for i in (0, 2, 4)) + (1,)


def add_grain(mat, bsdf):
    """Moulding grain as a bump only, so colour and roughness stay plain values for the glb."""
    nodes, links = mat.node_tree.nodes, mat.node_tree.links
    coords = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 2500.0
    noise.inputs["Detail"].default_value = 2.0
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.12
    bump.inputs["Distance"].default_value = 0.0002
    links.new(coords.outputs["Object"], noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])


PLY_FACE = ("#C38E52", "#D6A86C")  # oiled birch face, darker and lighter figure
PLY_GRAIN = "#9A6A3A"  # grain lines on the face
PLY_LONG = "#E4CDA0"  # long-grain ply on the edge
PLY_CROSS = "#CDA977"  # cross-grain ply on the edge
PLY_GLUE = "#3E2A1C"
PLY_GRAIN_SCALE = 90.0  # wave texture scale; grain lines about 5 mm apart
PLY_GLUE_WIDTH = 0.15  # half the glue line as a fraction of one ply


def add_plywood(mat, bsdf):
    """Oiled birch plywood from object coordinates (metres, z from the plate's
    bottom): soft figure with fine wandering grain lines along x on the faces,
    pale plies split by thin dark glue lines on the edges. Base Color and
    Roughness default values stay for the glb."""
    tp = RACK["top_plate"]
    nodes, links = mat.node_tree.nodes, mat.node_tree.links

    def node(kind, **inputs):
        n = nodes.new(kind)
        for k, v in inputs.items():
            n.inputs[k].default_value = v
        return n

    def math_node(op, a, b=None, c=None, clamp=False):
        n = nodes.new("ShaderNodeMath")
        n.operation = op
        n.use_clamp = clamp
        for i, v in enumerate((a, b, c)):
            if v is None:
                continue
            if isinstance(v, (int, float)):
                n.inputs[i].default_value = v
            else:
                links.new(v, n.inputs[i])
        return n.outputs[0]

    def mix(fac, a, b):
        n = nodes.new("ShaderNodeMix")
        n.data_type = "RGBA"
        links.new(fac, n.inputs["Factor"])
        for sock, v in ((n.inputs[6], a), (n.inputs[7], b)):
            if isinstance(v, tuple):
                sock.default_value = v
            else:
                links.new(v, sock)
        return n.outputs[2]

    def band(v, lo, hi):
        n = nodes.new("ShaderNodeMapRange")
        n.interpolation_type = "SMOOTHSTEP"
        links.new(v, n.inputs["Value"])
        n.inputs["From Min"].default_value = lo
        n.inputs["From Max"].default_value = hi
        return n.outputs["Result"]

    def stretched(scale, tex):
        mp = node("ShaderNodeMapping")
        mp.inputs["Scale"].default_value = scale
        links.new(coords, mp.inputs["Vector"])
        links.new(mp.outputs[0], tex.inputs["Vector"])
        return tex

    coords = nodes.new("ShaderNodeTexCoord").outputs["Object"]
    # face: soft figure, wandering grain lines and fine fibres, all along x
    figure = stretched((1.5, 25.0, 25.0),
                       node("ShaderNodeTexNoise", Scale=1.0, Detail=6.0, Roughness=0.55, Distortion=0.6))
    figure_fac = band(figure.outputs["Fac"], 0.3, 0.7)
    grain = stretched((0.06, 1.0, 1.0), nodes.new("ShaderNodeTexWave"))
    grain.wave_type, grain.bands_direction, grain.wave_profile = "BANDS", "Y", "SIN"
    for k, v in (("Scale", PLY_GRAIN_SCALE), ("Distortion", 10.0), ("Detail", 3.0),
                 ("Detail Scale", 0.8), ("Detail Roughness", 0.6)):
        grain.inputs[k].default_value = v
    lines = band(grain.outputs["Fac"], 0.9, 0.99)
    fibre = stretched((25.0, 2500.0, 2500.0), node("ShaderNodeTexNoise", Scale=1.0, Detail=2.0))
    fibre_fac = band(fibre.outputs["Fac"], 0.35, 0.7)
    face = mix(figure_fac, srgb_to_linear(PLY_FACE[0]), srgb_to_linear(PLY_FACE[1]))
    face = mix(math_node("MULTIPLY", fibre_fac, 0.18), face, srgb_to_linear(PLY_FACE[1]))
    face = mix(math_node("MULTIPLY", lines, 0.25), face, srgb_to_linear(PLY_GRAIN))
    # edge: plies from object z, wavering a little along the edge
    wobble = stretched((40.0, 40.0, 0.0), node("ShaderNodeTexNoise", Scale=1.0, Detail=3.0))
    sep = node("ShaderNodeSeparateXYZ")
    links.new(coords, sep.inputs[0])
    ply_t = m(tp["thickness"]) / tp["plies"]
    z = math_node("MULTIPLY_ADD", math_node("SUBTRACT", wobble.outputs["Fac"], 0.5), 0.3 * ply_t, sep.outputs["Z"])
    ply = math_node("DIVIDE", z, ply_t)
    index = math_node("FLOOR", ply)
    parity = math_node("MODULO", index, 2.0)
    frac = math_node("FRACT", ply)
    # glue line at each ply boundary, its width varying along the edge
    width = stretched((80.0, 80.0, 0.0), node("ShaderNodeTexNoise", Scale=1.0, Detail=2.0))
    half = math_node("MULTIPLY_ADD", width.outputs["Fac"], PLY_GLUE_WIDTH, PLY_GLUE_WIDTH * 0.25)
    dist = math_node("ABSOLUTE", math_node("SUBTRACT", frac, 0.5))
    glue = band(math_node("SUBTRACT", dist, math_node("SUBTRACT", 0.5, half)), -0.03, 0.03)
    tone = nodes.new("ShaderNodeTexWhiteNoise")
    tone.noise_dimensions = "1D"
    links.new(index, tone.inputs["W"])
    edge = mix(parity, srgb_to_linear(PLY_LONG), srgb_to_linear(PLY_CROSS))
    edge = mix(math_node("MULTIPLY", tone.outputs["Value"], 0.35), edge, srgb_to_linear(PLY_CROSS))
    end_grain = stretched((2000.0, 2000.0, 600.0), node("ShaderNodeTexNoise", Scale=1.0, Detail=2.0))
    speck = math_node("MULTIPLY", band(end_grain.outputs["Fac"], 0.5, 0.75), parity)
    edge = mix(math_node("MULTIPLY", speck, 0.12), edge, srgb_to_linear(PLY_GLUE))
    edge = mix(glue, edge, srgb_to_linear(PLY_GLUE))
    # face vs edge by the geometry normal
    geo = nodes.new("ShaderNodeNewGeometry")
    nsep = node("ShaderNodeSeparateXYZ")
    vt = nodes.new("ShaderNodeVectorTransform")
    vt.vector_type, vt.convert_from, vt.convert_to = "NORMAL", "WORLD", "OBJECT"
    links.new(geo.outputs["Normal"], vt.inputs[0])
    links.new(vt.outputs[0], nsep.inputs[0])
    is_face = math_node("GREATER_THAN", math_node("ABSOLUTE", nsep.outputs["Z"]), 0.9)
    links.new(mix(is_face, edge, face), bsdf.inputs["Base Color"])
    # bump: grain lines and fibres on the face, glue grooves on the edge
    face_height = math_node("SUBTRACT", math_node("MULTIPLY", fibre_fac, 0.3), lines)
    height = math_node("MULTIPLY_ADD", is_face, face_height, math_node("MULTIPLY", math_node("SUBTRACT", 1.0, is_face),
                                                                        math_node("SUBTRACT", 1.0, glue)))
    bump = node("ShaderNodeBump", Strength=0.12, Distance=0.0002)
    links.new(height, bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])


def make_materials():
    mats = {}
    colours = dict(COLOURS)
    for name, spec in RACK["color_clips"]["colours"].items():
        colours[f"clip_{name}"] = (srgb_to_linear(spec["srgb"]), 0.0, CLIP_ROUGHNESS, 1.49)
    for name, (colour, metal, rough, ior) in colours.items():
        mat = bpy.data.materials.new(name)
        if mat.node_tree is None:
            mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        bsdf.inputs["Base Color"].default_value = colour
        bsdf.inputs["Metallic"].default_value = metal
        bsdf.inputs["Roughness"].default_value = rough
        bsdf.inputs["IOR"].default_value = ior
        if name in GRAINED:
            add_grain(mat, bsdf)
        if name == "plywood":
            add_plywood(mat, bsdf)
        mat.diffuse_color = colour
        mat.roughness = rough
        mats[name] = mat
    return mats


def collection(scene, name):
    coll = bpy.data.collections.new(name)
    scene.collection.children.link(coll)
    return coll


def smooth(mesh):
    """Smooth shading with every edge above SHARP_ANGLE kept sharp."""
    mesh.shade_smooth()
    mesh.set_sharp_from_angle(angle=SHARP_ANGLE)


def to_mesh(name, bm, mat):
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    mesh.materials.append(mat)
    smooth(mesh)
    return mesh


def place(name, mesh, coll, parent=None, location=(0, 0, 0)):
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    coll.objects.link(obj)
    if parent is not None:
        obj.parent = parent
    return obj


def finish(name, bm, mat, coll, parent=None, location=(0, 0, 0)):
    return place(name, to_mesh(name, bm, mat), coll, parent, location)


def bm_box(bm, lo, hi):
    lo, hi = Vector(lo), Vector(hi)
    size = hi - lo
    mat = Matrix.Translation((lo + hi) / 2) @ Matrix.Diagonal((*size, 1))
    bmesh.ops.create_cube(bm, size=1.0, matrix=mat)


def mm_box(bm, x0, x1, y0, y1, z0, z1):
    """Axis-aligned box from millimetre bounds in any order; empty boxes are skipped."""
    x0, x1 = sorted((x0, x1))
    y0, y1 = sorted((y0, y1))
    z0, z1 = sorted((z0, z1))
    if x1 - x0 > 1e-6 and y1 - y0 > 1e-6 and z1 - z0 > 1e-6:
        bm_box(bm, (m(x0), m(y0), m(z0)), (m(x1), m(y1), m(z1)))


def bm_cylinder(bm, centre, radius, depth, axis, segments=24):
    rot = {"x": Matrix.Rotation(math.pi / 2, 4, "Y"),
           "y": Matrix.Rotation(math.pi / 2, 4, "X"),
           "z": Matrix.Identity(4)}[axis]
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segments, radius1=radius,
                          radius2=radius, depth=depth,
                          matrix=Matrix.Translation(centre) @ rot)


def hollow_tray(rim_x, rim_y, foot_x, foot_y, height, in_x, in_y, in_foot_x, in_foot_y, floor_z):
    """Closed hollow tray, origin at the bottom centre."""
    bm = bmesh.new()
    rings = [(rim_x / 2, rim_y / 2, height), (foot_x / 2, foot_y / 2, 0.0),
             (in_foot_x / 2, in_foot_y / 2, floor_z), (in_x / 2, in_y / 2, height)]
    loops = [[bm.verts.new(p) for p in
              ((-hx, -hy, z), (hx, -hy, z), (hx, hy, z), (-hx, hy, z))]
             for hx, hy, z in rings]
    for k in range(4):
        a, b = loops[k], loops[(k + 1) % 4]
        if k == 1:
            bm.faces.new(a)  # bottom
            bm.faces.new(b)  # inner floor
            continue
        for i in range(4):
            j = (i + 1) % 4
            bm.faces.new((a[i], a[j], b[j], b[i]))
    return bm


def rect_section(wa, wb):
    """Outline of a slotted profile wa x wb mm, one slot per 30 mm module of each side."""
    w, d = SLOT_WIDTH / 2, SLOT_DEPTH
    ha, hb = wa / 2, wb / 2

    def mods(length, half):
        return [-half + 15 + 30 * i for i in range(int(round(length / 30)))]

    pts = [(-ha, -hb)]
    for c in mods(wa, ha):
        pts += [(c - w, -hb), (c - w, -hb + d), (c + w, -hb + d), (c + w, -hb)]
    pts.append((ha, -hb))
    for c in mods(wb, hb):
        pts += [(ha, c - w), (ha - d, c - w), (ha - d, c + w), (ha, c + w)]
    pts.append((ha, hb))
    for c in reversed(mods(wa, ha)):
        pts += [(c + w, hb), (c + w, hb - d), (c - w, hb - d), (c - w, hb)]
    pts.append((-ha, hb))
    for c in reversed(mods(wb, hb)):
        pts += [(-ha, c + w), (-ha + d, c + w), (-ha + d, c - w), (-ha, c - w)]
    return [(m(a), m(b)) for a, b in pts]


SECTION = None
X, Y, Z = Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1))
MATS = {}
MESHES = {}
NAMES = {}


def mm_vec(p):
    return Vector((m(p[0]), m(p[1]), m(p[2])))


def orient(origin_mm, z_dir, x_hint=None):
    """World matrix at origin_mm (mm) with local z along z_dir and local x along
    x_hint made square to it."""
    z = Vector(z_dir).normalized()
    if x_hint is None:
        x_hint = X if abs(z.x) < 0.9 else Y
    x = Vector(x_hint)
    x = (x - z * x.dot(z)).normalized()
    mat = Matrix((x, z.cross(x), z)).transposed().to_4x4()
    mat.translation = mm_vec(origin_mm)
    return mat


def world_of(obj):
    """World matrix from the matrix_basis chain; every parent inverse is identity."""
    mat = obj.matrix_basis.copy()
    while obj.parent is not None:
        obj = obj.parent
        mat = obj.matrix_basis @ mat
    return mat


def place_at(name, mesh, coll, world, parent=None, part=None):
    """Object at the world matrix world, kept there under parent."""
    obj = bpy.data.objects.new(name, mesh)
    coll.objects.link(obj)
    if parent is not None:
        obj.parent = parent
        world = world_of(parent).inverted() @ world
    obj.matrix_basis = world
    if part:
        obj["part"] = part
    return obj


def shared(key, build):
    """One mesh per kind of part, built on first use."""
    if key not in MESHES:
        MESHES[key] = build()
    return MESHES[key]


def bm_cone(bm, base_mm, axis, r0, r1, length, segments=16):
    """Cone or cylinder from base_mm along axis for length (mm); radius r0 at the
    base, r1 at the far end."""
    mat = orient(base_mm, axis)
    mat = mat @ Matrix.Translation((0, 0, m(length) / 2))
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segments, radius1=m(r0), radius2=m(r1),
                          depth=m(length), matrix=mat)


def profile_bm(length):
    """Slotted 30 x 30 profile along +z from 0 to length (mm), section centred on the axis."""
    bm = bmesh.new()
    rings = [[bm.verts.new((a, b, t)) for a, b in SECTION] for t in (0.0, m(length))]
    n = len(SECTION)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((rings[0][i], rings[0][j], rings[1][j], rings[1][i]))
    bm.faces.new(rings[0])
    bm.faces.new(rings[1][::-1])
    return bm


def profile_mesh(length):
    return shared(f"profile.{length}",
                  lambda: to_mesh(f"mesh.profile.{length}", profile_bm(length), MATS["aluminium"]))


def bar_mesh(top):
    """Bar along +z with the through holes of the core bolts, the top bar also
    with their counterbores; in its frame local y is up (rack z)."""
    def build():
        fr = RACK["frame"]
        holes = fr["bar_holes"]
        cb, h = holes["top_counterbore"], fr["profile"]["section"] / 2
        length = fr["top_bar" if top else "bottom_bar"]["length"]
        cutter = bmesh.new()
        for x in fr["upright_x"]:
            if top:
                bm_cone(cutter, (0, h + 1, x + h), -Y, cb["diameter"] / 2, cb["diameter"] / 2, cb["depth"] + 1)
            bm_cone(cutter, (0, h + 1, x + h), -Y, holes["diameter"] / 2, holes["diameter"] / 2, 2 * h + 2)
        name = "bar.top" if top else "bar.bottom"
        return to_mesh(f"mesh.{name}", boolean_cut(profile_bm(length), cutter), MATS["aluminium"])
    return shared("bar.top" if top else "bar.bottom", build)


def orient_ab(origin_mm, a, b):
    """World matrix at origin_mm with local x along a and local y along b."""
    a, b = Vector(a).normalized(), Vector(b).normalized()
    mat = Matrix((a, b, a.cross(b))).transposed().to_4x4()
    mat.translation = mm_vec(origin_mm)
    return mat


def at(origin_mm, *steps):
    """origin_mm plus each (direction, mm) step, in mm."""
    p = Vector(origin_mm)
    for d, mm in steps:
        p += Vector(d) * mm
    return p


def prism_ab(bm, pts, c0, c1):
    loft(bm, [[(m(a), m(b), m(c)) for a, b in pts] for c in (c0, c1)], closed=False)


def profile(name, part, length, start_mm, axis, coll, parent):
    return place_at(name, profile_mesh(length), coll, orient(start_mm, axis), parent, part)


# ---------------------------------------------------------------- fasteners

def screw_mesh(part):
    """Screw along +z, the way it goes in: origin on the bearing face, so a
    socket, button or pan head lies at z < 0 and a countersunk head at
    0 < z < head_k, flush with the face."""
    s = RACK["fasteners"]["screws"][part]
    d, length, dk, k = s["d"], s["length"], s["head_d"], s["head_k"]
    bm = bmesh.new()
    if s["head"] == "countersunk":
        bm_cone(bm, (0, 0, 0), Z, dk / 2, d / 2, k)
        bm_cone(bm, (0, 0, k), Z, d / 2, d / 2, length - k, segments=12)
    else:
        top = {"socket": dk / 2, "button": dk * 0.3, "pan": dk * 0.4}[s["head"]]
        bm_cone(bm, (0, 0, -k), Z, top, dk / 2, k)
        bm_cone(bm, (0, 0, 0), Z, d / 2, d / 2, length, segments=12)
    return to_mesh(f"mesh.{part}", bm, MATS["steel"])


def nut_mesh(part):
    """Hammer nut turned across the slot: origin on the slot face, +z into the
    profile, its top lip below the face."""
    n = RACK["fasteners"]["nuts"][part]
    lip = RACK["frame"]["slot"]["lip"]
    bm = bmesh.new()
    mm_box(bm, -n["length"] / 2, n["length"] / 2, -n["width"] / 2, n["width"] / 2, lip, lip + n["height"])
    return to_mesh(f"mesh.{part}", bm, MATS["steel"])


def washer_mesh(part):
    w = RACK["fasteners"]["washers"][part]
    bm = bmesh.new()
    bm_cone(bm, (0, 0, -w["h"]), Z, w["d2"] / 2, w["d2"] / 2, w["h"], segments=20)
    return to_mesh(f"mesh.{part}", bm, MATS["steel"])


def cap_mesh(part):
    """End cap flange, +z out of the bar end."""
    c = RACK["fasteners"]["cap"]
    h = c["size"] / 2
    bm = bmesh.new()
    mm_box(bm, -h, h, -h, h, 0, c["thickness"])
    return to_mesh(f"mesh.{part}", bm, MATS["cap_black"])


def fastener_mesh(part):
    """One mesh per screw, nut, washer or cap; it carries the part ID and the
    kind, so its 484 objects need no custom property of their own (in
    rack.blend and as glTF mesh extras, which three.js gives every node)."""
    f = RACK["fasteners"]
    if part in f["screws"]:
        build = screw_mesh
    elif part in f["nuts"]:
        build = nut_mesh
    elif part in f["washers"]:
        build = washer_mesh
    else:
        build = cap_mesh

    def tagged():
        mesh = build(part)
        mesh["part"] = part
        mesh["kind"] = "cap" if part == f["cap"]["part"] else "fastener"
        return mesh
    return shared(part, tagged)


def fastener(part, origin_mm, direction, host, x_hint=None, part_of=None):
    """A screw, nut, washer or cap at origin_mm, going in along direction, held by host.

    part_of: the part whose fixing set it belongs to (host is that part); the
    object then says so, and object_part counts it with that part."""
    key = part_of or part
    NAMES[(key, part)] = NAMES.get((key, part), 0) + 1
    n = NAMES[(key, part)]
    name = f"{part_of}.fixing.{part}.{n}" if part_of else f"{part}.{n}"
    obj = place_at(name, fastener_mesh(part), COLLS["fasteners"], orient(origin_mm, direction, x_hint), host)
    if part_of:
        obj["part_of"] = part_of
    return obj


def object_part(obj):
    """The part ID an object counts as: its own, else its mesh's; none for a
    piece of a fixing set."""
    if obj.get("part_of"):
        return None
    if obj.get("part"):
        return obj["part"]
    return obj.data.get("part") if obj.type == "MESH" else None


def nut(part, face_mm, direction, slot_dir, host, part_of=None):
    """Hammer nut behind face_mm in a slot running along slot_dir, turned across it."""
    across = Vector(direction).cross(Vector(slot_dir))
    return fastener(part, face_mm, direction, host, across, part_of)


COLLS = {}


# ---------------------------------------------------------------- the rack

FRAME = {}  # the frame's profiles by role, for the fasteners that sit in them


def build_frame(mats, colls, frame_root):
    """Profiles, the core bolts of the upright joints and the end caps."""
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    h = sec / 2
    coll = colls["frame"]
    ux, uy = fr["upright_x"], fr["upright_y"]
    up = fr["upright"]
    for i, x in enumerate(ux):
        for y, side in zip(uy, ("front", "back")):
            FRAME[("upright", i, side)] = profile(f"upright.{i + 1}.{side}", "profile.upright", up["length"],
                                                  (x + h, y + h, up["bottom"]), Z, coll, frame_root)
    bb, tb = fr["bottom_bar"], fr["top_bar"]
    for y, side in zip(uy, ("front", "back")):
        for top, bar in ((False, bb), (True, tb)):
            key = "top" if top else "bottom"
            zc = (bar["bottom"] + bar["top"]) / 2
            obj = place_at(f"bar.{key}.{side}", bar_mesh(top), coll, orient_ab((0, y + h, zc), Y, Z),
                           frame_root, f"profile.bar_{key}")
            FRAME[("bar", key, side)] = obj
            for x0, out in ((0, -X), (bar["length"], X)):
                fastener("cap.end_30", (x0, y + h, zc), out, obj)
        for x in ux:
            fastener("screw.m8x70_socket", (x + h, y + h, bb["bottom"]), Z, FRAME[("bar", "bottom", side)])
            fastener("screw.m8x50_socket", (x + h, y + h, tb["top"] - fr["bar_holes"]["top_counterbore"]["depth"]),
                     -Z, FRAME[("bar", "top", side)])
    db = fr["depth_beam"]
    for i, x in enumerate(ux):
        for lvl in ("bottom", "top"):
            FRAME[("beam", lvl, i)] = profile(f"beam.depth.{lvl}.{i + 1}", "profile.beam_depth", db["length"],
                                              (x + h, uy[0] + sec, (db[lvl]["bottom"] + db[lvl]["top"]) / 2),
                                              Y, coll, frame_root)


def angle_mesh(kind):
    """L angle along +y from 0 to its length, the upright face at x 0, the leg
    inward along +x; z 0 is the inner face of the flat leg. base: flat leg
    below, leg up; support (also the guard): flat leg on top, leg down. The
    holes go through the leg against the upright, countersunk on the box side."""
    def build():
        a = RACK["angles"]
        leg, t, length = a["section"]["leg"], a["section"]["thickness"], a["length"]
        if kind == "base":
            outline = [(0, -t), (leg, -t), (leg, 0), (t, 0), (t, leg - t), (0, leg - t)]
        else:
            outline = [(0, t - leg), (t, t - leg), (t, 0), (leg, 0), (leg, t), (0, t)]
        holes = a["holes"]
        s = RACK["fasteners"]["screws"][holes["screw"]]
        cutter = bmesh.new()
        for y, z in angle_holes(kind):
            bm_cone(cutter, (t + 0.01, y, z), -X, s["head_d"] / 2 + 0.01, holes["diameter"] / 2,
                    (s["head_d"] - holes["diameter"]) / 2)
            bm_cone(cutter, (t + 1, y, z), -X, holes["diameter"] / 2, holes["diameter"] / 2, t + 2)
        body = prism_y(outline, 0, length)
        return to_mesh(f"mesh.angle.{kind}", boolean_cut(body, cutter), MATS["aluminium"])
    return shared(f"angle.{kind}", build)


def angle_holes(kind):
    """(y, z) of the holes in the angle's own frame."""
    a = RACK["angles"]
    holes = a["holes"]
    sign = 1 if kind == "base" else -1
    return [(y, sign * dz) for y in (holes["from_end"], a["length"] - holes["from_end"])
            for dz in holes["from_flat_leg"]]


def bay_faces(c):
    """The two upright faces of bay c: (x of the face, inward sign, side, upright index)."""
    fr = RACK["frame"]
    ux, sec = fr["upright_x"], fr["profile"]["section"]
    return ((ux[c] + sec, +1, "left", c), (ux[c + 1], -1, "right", c + 1))


def angle(name, part, kind, x_face, inward, z_ref, upright, coll, parent):
    """An angle against the upright face x_face, its leg pointing inward (+1 or
    -1), z_ref the inner face of its flat leg, with its four screws and nuts.
    The right-hand angle is the left one turned half round, not mirrored."""
    a = RACK["angles"]
    t, length = a["section"]["thickness"], a["length"]
    if inward > 0:
        world = orient_ab((x_face, 0, z_ref), X, Y)
    else:
        world = orient_ab((x_face, length, z_ref), -X, -Y)
    obj = place_at(name, angle_mesh(kind), coll, world, parent, part)
    for y_local, z in angle_holes(kind):
        y = y_local if inward > 0 else length - y_local
        side = "front" if y < length / 2 else "back"
        fastener(a["holes"]["screw"], (x_face + inward * t, y, z_ref + z), -inward * X, obj)
        nut("tnut.m5", (x_face, y, z_ref + z), -inward * X, Z, FRAME[("upright", upright, side)])
    return obj


def build_angles(mats, colls, frame_root):
    fr, a = RACK["frame"], RACK["angles"]
    t = a["section"]["thickness"]
    for c in range(fr["columns"]):
        for lv in RACK["levels"]:
            for x_face, inward, side, up in bay_faces(c):
                if lv["angle"] == "angle.base":
                    angle(f"angle.base.L{lv['level']}.C{c + 1}.{side}", "angle.base", "base", x_face, inward,
                          a["base"]["flat_leg_top"], up, colls["angles"], frame_root)
                else:
                    angle(f"angle.support.L{lv['level']}.C{c + 1}.{side}", "angle.support", "support", x_face,
                          inward, lv["floor"] - t, up, colls["angles"], frame_root)
        for x_face, inward, side, up in bay_faces(c):
            angle(f"angle.guard.C{c + 1}.{side}", "angle.guard", "support", x_face, inward,
                  RACK["tip_guard"]["flat_leg_bottom"], up, colls["angles"], frame_root)


def bracket_mesh():
    """motedis S8BBR30 in its own frame: corner on the origin, leg A along +x
    against a face whose normal is +y, leg B along +y against a face whose
    normal is +x, the width along z."""
    def build():
        b = RACK["brackets"]["inside_30"]
        leg, t, hw, sw, edge = b["leg"], b["thickness"], b["width"] / 2, b["side_wall"], b["side_wall_edge"]
        body = bmesh.new()
        prism_ab(body, [(0, 0), (leg, 0), (leg, t), (0, t)], -hw, hw)
        prism_ab(body, [(0, 0), (t, 0), (t, leg), (0, leg)], -hw, hw)
        wall = [(0, 0), (leg, 0), (leg, edge - leg), (edge - leg, leg), (0, leg)]
        for z0, z1 in ((-hw, -hw + sw), (hw - sw, hw)):
            prism_ab(body, wall, z0, z1)
        hole = b["hole"]
        r, c0, c1 = hole["width"] / 2, hole["from"] + hole["width"] / 2, hole["to"] - hole["width"] / 2
        cutter = bmesh.new()
        for u in (c0, c1):
            bm_cone(cutter, (u, t + 1, 0), -Y, r, r, t + 2, segments=12)
            bm_cone(cutter, (t + 1, u, 0), -X, r, r, t + 2, segments=12)
        mm_box(cutter, c0, c1, -1, t + 1, -r, r)
        mm_box(cutter, -1, t + 1, c0, c1, -r, r)
        return to_mesh("mesh.bracket.inside_30", boolean_cut(body, cutter), MATS["aluminium"])
    return shared("bracket", build)


def bracket(name, part, corner_mm, a, b, parent, slot_a, slot_b, part_of=None, screw_b=True):
    """A bracket in the inside corner at corner_mm, leg A along a, leg B along b,
    with a screw and a hammer nut in each leg; slot_a and slot_b are the
    directions of the slots the legs sit on. screw_b False leaves leg B free."""
    br = RACK["brackets"]["inside_30"]
    obj = place_at(name, bracket_mesh(), COLLS["frame"], orient_ab(corner_mm, a, b), parent, part)
    mid, t = (br["hole"]["from"] + br["hole"]["to"]) / 2, br["thickness"]
    a, b = Vector(a), Vector(b)
    legs = [(a, b, slot_a)] + ([(b, a, slot_b)] if screw_b else [])
    for along, off, slot in legs:
        face = at(corner_mm, (along, mid))
        fastener("screw.m6x12_button", at(face, (off, t)), -off, obj, part_of=part_of)
        host = slot  # the profile that holds the nut
        nut("tnut.m6", face, -off, host[1], host[0], part_of=part_of)
    return obj


def build_brackets(mats, colls, frame_root):
    """The 28 inside brackets of the joints and the 20 plate brackets."""
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    ux, uy = fr["upright_x"], fr["upright_y"]
    db, tb = fr["depth_beam"], fr["top_bar"]
    last = len(ux) - 1
    zc_top, zc_bottom = (tb["bottom"] + tb["top"]) / 2, (db["bottom"]["bottom"] + db["bottom"]["top"]) / 2
    n = 0
    for y_face, dy, side in ((uy[0] + sec, +1, "front"), (uy[1], -1, "back")):
        bar_top, bar_bottom = FRAME[("bar", "top", side)], FRAME[("bar", "bottom", side)]
        for i, x in enumerate(ux):
            up = FRAME[("upright", i, side)]
            # upright to top depth beam: leg A down the upright, leg B under the beam
            n += 1
            bracket(f"bracket.{n}", "bracket.inside_30", (x + sec / 2, y_face, db["top"]["bottom"]), -Z, dy * Y,
                    frame_root, (up, Z), (FRAME[("beam", "top", i)], Y))
            # depth beam to bar on the beam's bay side, and at the middle
            # uprights a second one at the bottom on the other side
            xf, dx = (x, -1) if i == last else (x + sec, +1)
            for zc, bar, lvl, sides in ((zc_top, bar_top, "top", [(xf, dx)]),
                                        (zc_bottom, bar_bottom, "bottom",
                                         [(xf, dx)] + ([(x, -1)] if 0 < i < last else []))):
                for xs, ds in sides:
                    n += 1
                    bracket(f"bracket.{n}", "bracket.inside_30", (xs, y_face, zc), ds * X, dy * Y, frame_root,
                            (bar, X), (FRAME[("beam", lvl, i)], Y))
        # plate brackets in the top bar's inner slot, leg B flush with the bar
        # top under the plate, held to the plate by one wood screw
        br = RACK["brackets"]["inside_30"]
        mid, t = (br["hole"]["from"] + br["hole"]["to"]) / 2, br["thickness"]
        for k, xc in enumerate(RACK["top_plate"]["mounts"]["x"], 1):
            obj = bracket(f"bracket.plate.{side}.{k}", "bracket.plate", (xc, y_face, tb["top"]), -Z, dy * Y,
                          frame_root, (bar_top, X), None, part_of="bracket.plate", screw_b=False)
            fastener("screw.wood_4_5x16", (xc, y_face + dy * mid, tb["top"] - t), Z, obj)
    assert n == 28, n


def corners():
    """Frame corners in the order front-left, front-right, back-left, back-right: (x sign, y sign)."""
    return ((+1, +1), (-1, +1), (+1, -1), (-1, -1))


def corner_frame(sx, sy):
    """Unit vectors (u, v) from a frame corner inward, u along the bar and v along
    the depth beam where that is a right-handed turn; else the two swap, which the
    plate's pattern, symmetric about its diagonal, allows."""
    u, v = sx * X, sy * Y
    return (u, v) if sx * sy > 0 else (v, u)


def castor_plate_mesh():
    """Castor plate from its outer corner at the origin into +x and +y, 0 to its thickness in z."""
    def build():
        cp = RACK["frame"]["castor_plate"]
        holes, s, t = cp["holes"], cp["size"], cp["thickness"]
        body = bmesh.new()
        mm_box(body, 0, s, 0, s, 0, t)
        cutter = bmesh.new()
        sink = RACK["fasteners"]["screws"]["screw.m6x16_countersunk"]
        for u, v in holes["screws"]["at"]:
            d = holes["screws"]["diameter"]
            bm_cone(cutter, (u, v, -0.01), Z, sink["head_d"] / 2 + 0.01, d / 2, (sink["head_d"] - d) / 2)
            bm_cone(cutter, (u, v, -1), Z, d / 2, d / 2, t + 2, segments=12)
        u, v = holes["bolt_clearance"]["at"]
        r = holes["bolt_clearance"]["diameter"] / 2
        bm_cone(cutter, (u, v, -1), Z, r, r, t + 2)
        u, v = holes["castor_thread"]["at"]
        bm_cone(cutter, (u, v, -1), Z, 4, 4, t + 2, segments=12)
        return to_mesh("mesh.plate.castor", boolean_cut(body, cutter), MATS["aluminium"])
    return shared("plate.castor", build)


def build_castor_plates(mats, colls, frame_root):
    fr = RACK["frame"]
    cp = fr["castor_plate"]
    W, D = fr["width"], fr["depth"]
    plates = []
    for n, (sx, sy) in enumerate(corners(), 1):
        x0 = 0 if sx > 0 else W
        y0 = 0 if sy > 0 else D
        u, v = corner_frame(sx, sy)
        obj = place_at(f"plate.castor.{n}", castor_plate_mesh(), colls["frame"],
                       orient_ab((x0, y0, cp["bottom"]), u, v), frame_root, "plate.castor")
        plates.append(obj)
        side = "front" if sy > 0 else "back"
        beam = FRAME[("beam", "bottom", 0 if sx > 0 else len(fr["upright_x"]) - 1)]
        for a, b in cp["holes"]["screws"]["at"]:
            along_bar = b < a  # (60, 15), (80, 15) run along the bar
            p = at((x0, y0, 0), (sx * X, a), (sy * Y, b))
            fastener("screw.m6x16_countersunk", (p.x, p.y, cp["bottom"]), Z, obj)
            host = FRAME[("bar", "bottom", side)] if along_bar else beam
            nut("tnut.m6", (p.x, p.y, cp["top"]), Z, X if along_bar else Y, host)
    return plates


def build_castors(mats, colls, frame_root):
    """Plain swivel castors 1-4 at front-left, front-right, back-left, back-right; wheels trail inward."""
    fr = RACK["frame"]
    ca = fr["castor"]
    h = fr["castor_height"]
    W, D, inset = fr["width"], fr["depth"], ca["inset"]
    head_r, wheel_r = ca["head_diameter"] / 2, ca["wheel"] / 2
    tw, off = ca["tread_width"], ca["offset"]

    def build():
        """The castor with its wheel trailing towards +y; the back ones are turned half round."""
        bm = bmesh.new()
        bm_cylinder(bm, (0, 0, m(h - 4)), m(head_r), m(8), "z")
        bm_cylinder(bm, (0, 0, m(h - 12)), m(head_r * 0.7), m(8), "z")
        ox = tw / 2 + 4
        mm_box(bm, -ox - 3, ox + 3, -12, off + 12, h - 22, h - 16)
        for k in (-1, 1):
            mm_box(bm, k * ox, k * (ox + 3), off - 18, off + 12, wheel_r - 8, h - 16)
        bm_cylinder(bm, (0, m(off), m(wheel_r)), m(wheel_r), m(tw), "x")
        bm_cylinder(bm, (0, m(off), m(wheel_r)), m(6), m(2 * ox + 8), "x", segments=12)
        return to_mesh("mesh.castor.plain", bm, mats["castor"])

    for n, (sx, sy) in enumerate(corners(), 1):
        cx = inset if sx > 0 else W - inset
        cy = inset if sy > 0 else D - inset
        assert head_r <= cx <= W - head_r and head_r <= cy <= D - head_r, "castor head outside"
        world = orient_ab((cx, cy, 0), sy * X, sy * Y)
        obj = place_at(f"castor.plain.{n}", shared("castor.plain", build), colls["castors"], world, frame_root,
                       "castor.plain")
        w = RACK["fasteners"]["washers"]["washer.m8"]["h"]
        face = h - ca["top_plate"]
        fastener("washer.m8", (cx, cy, face), Z, obj)
        fastener("screw.m8x20_socket", (cx, cy, face - w), Z, obj)


# ---------------------------------------------------------------- boxes

# mm the handle frame face sits behind the rim plane: it stands out of the
# recessed panel but keeps the box 400 long and off the coplanar ledge face.
FRAME_PROUD = -0.2


def rr_outline(hx, hy, radii, segments=CORNER_SEGMENTS):
    """Rounded rectangle of half sizes hx, hy (mm), counter-clockwise from +x.

    radii: one radius for all corners or (ne, nw, sw, se); every outline has the
    same point count, so two outlines bridge quad by quad.
    """
    if not isinstance(radii, (tuple, list)):
        radii = (radii,) * 4
    pts = []
    for (sx, sy, a0), r in zip(((1, 1, 0), (-1, 1, 90), (-1, -1, 180), (1, -1, 270)), radii):
        r = max(0.0, min(r, hx - 1e-3, hy - 1e-3))
        cx, cy = sx * (hx - r), sy * (hy - r)
        if r == 0.0:
            pts.append((cx, cy))
            continue
        for i in range(segments + 1):
            a = math.radians(a0 + 90 * i / segments)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def loft(bm, loops, closed=True):
    """Bridge outlines of equal length in order; the first and last get caps."""
    vs = [[bm.verts.new(p) for p in loop] for loop in loops]
    n = len(vs[0])
    pairs = list(zip(vs, vs[1:])) + ([(vs[-1], vs[0])] if closed else [])
    for a, b in pairs:
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((a[i], a[j], b[j], b[i]))
    if not closed:
        bm.faces.new(vs[0])
        bm.faces.new(vs[-1][::-1])


def bevel_edges(bm, offset_mm):
    """Round every edge sharper than SHARP_ANGLE; the corner arcs stay as they are."""
    edges = [e for e in bm.edges if e.is_manifold and e.calc_face_angle(0) > SHARP_ANGLE]
    bmesh.ops.bevel(bm, geom=edges, offset=m(offset_mm), offset_type="OFFSET", segments=2,
                    profile=0.5, affect="EDGES", clamp_overlap=True)


def merge(dst, piece, round_mm):
    """Bevel a closed piece on its own, then append it to dst."""
    bmesh.ops.recalc_face_normals(piece, faces=piece.faces[:])
    if round_mm:
        bevel_edges(piece, round_mm)
    tmp = bpy.data.meshes.new("tmp.piece")
    piece.to_mesh(tmp)
    piece.free()
    dst.from_mesh(tmp)
    bpy.data.meshes.remove(tmp)


def prism_z(outline, z0, z1):
    """Closed prism from an outline in xy (mm) between z0 and z1."""
    bm = bmesh.new()
    loft(bm, [[(m(x), m(y), m(z)) for x, y in outline] for z in (z0, z1)], closed=False)
    return bm


def prism_y(outline, y0, y1, holes=()):
    """Closed prism from an outline in xz (mm) between y0 and y1; a hole outline
    of the same point count makes it a ring."""
    bm = bmesh.new()
    rings = [[(m(x), m(y), m(z)) for x, z in outline] for y in (y0, y1)]
    if holes:
        inner = [[(m(x), m(y), m(z)) for x, z in holes] for y in (y1, y0)]
        loft(bm, rings + inner, closed=True)
    else:
        loft(bm, rings, closed=False)
    return bm


INNER_SKIN = 2.5  # mm, the smooth inner wall the outer bands sit on


def offset_outline(pts, dx, dz):
    return [(x + dx, z + dz) for x, z in pts]


def weighted_normals(mesh, name):
    """Custom normals weighted by face area, so the big flat faces stay flat
    next to the rounded corners instead of showing shading streaks."""
    scene = bpy.context.scene
    obj = bpy.data.objects.new("tmp.normals", mesh)
    scene.collection.objects.link(obj)
    mod = obj.modifiers.new("normals", "WEIGHTED_NORMAL")
    mod.mode = "FACE_AREA"
    mod.weight = 100
    mod.keep_sharp = True
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(obj.evaluated_get(depsgraph), preserve_all_data_layers=True,
                                             depsgraph=depsgraph)
    bpy.data.objects.remove(obj)
    bpy.data.meshes.remove(mesh)
    result.name = name
    return result


def shell(outers, inner_at, grow=0.0):
    """Wall ring through outer rounded rectangles (hx, hy, r, z), bottom to top,
    closed by the tapered inner face moved out by grow (mm)."""
    bm = bmesh.new()
    loops = [[(m(x), m(y), m(z)) for x, y in rr_outline(ox, oy, r)] for ox, oy, r, z in outers]
    for z in (outers[-1][3], outers[0][3]):
        ix, iy, ir = inner_at(z)
        loops.append([(m(x), m(y), m(z)) for x, y in rr_outline(ix + grow, iy + grow, ir + grow)])
    loft(bm, loops, closed=True)
    return bm


def boolean_cut(body, cutter):
    """body minus cutter with the exact boolean solver, as a new bmesh; use_self
    makes it unite the closed pieces of body even where they interpenetrate."""
    scene = bpy.context.scene
    objs = []
    for label, bm in (("body", body), ("cutter", cutter)):
        mesh = bpy.data.meshes.new(f"tmp.{label}")
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
        bm.to_mesh(mesh)
        bm.free()
        obj = bpy.data.objects.new(f"tmp.{label}", mesh)
        scene.collection.objects.link(obj)
        objs.append(obj)
    body_obj, cutter_obj = objs
    mod = body_obj.modifiers.new("cut", "BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = cutter_obj
    mod.solver = "EXACT"
    mod.use_self = True
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(body_obj.evaluated_get(depsgraph))
    for obj in objs:
        mesh = obj.data
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)
    out = bmesh.new()
    out.from_mesh(result)
    bpy.data.meshes.remove(result)
    return out


def rounded_mesh(bm, name, mat, round_mm):
    """Mesh from bm with every edge sharper than SHARP_ANGLE rounded after the
    union, so the joints of the pieces are rounded too."""
    scene = bpy.context.scene
    mesh = bpy.data.meshes.new("tmp.round")
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("tmp.round", mesh)
    scene.collection.objects.link(obj)
    mod = obj.modifiers.new("round", "BEVEL")
    mod.width = m(round_mm)
    mod.segments = 1
    mod.limit_method = "ANGLE"
    mod.angle_limit = SHARP_ANGLE
    mod.use_clamp_overlap = True
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(obj.evaluated_get(depsgraph))
    bpy.data.objects.remove(obj)
    bpy.data.meshes.remove(mesh)
    result.name = name
    result.materials.clear()
    result.materials.append(mat)
    smooth(result)
    return weighted_normals(result, name)


def inner_wall(bx):
    """Inner half sizes and corner radius at height z (mm): the wall tapers from
    the inner top at the rim to the inner floor."""
    s = RACK["box_shape"]
    H = bx["height"]
    floor_z = H - bx["inner_height"]
    top = (bx["inner_width"] / 2, bx["inner_length"] / 2)
    bottom = (bx["inner_floor_width"] / 2, bx["inner_floor_length"] / 2)

    def at(z):
        t = (z - floor_z) / (H - floor_z)
        return (bottom[0] + t * (top[0] - bottom[0]),
                bottom[1] + t * (top[1] - bottom[1]),
                s["inner_corner_radius"])
    return at


def cycle_box(bx, mat, name):
    """NextGen 2.0 Cycle box after box_shape; origin at the front bottom centre."""
    s = RACK["box_shape"]
    hd = s["handle"]
    H = bx["height"]
    X, Y = bx["width"] / 2, bx["length"] / 2
    R = s["corner_radius"]
    inner = inner_wall(bx)
    floor_z = H - bx["inner_height"]
    rim0 = H - s["rim_band"]
    collar0 = rim0 - s["collar"]
    ledge0 = collar0 - s["ledge"]
    foot1 = s["foot_band"]
    p, cr = s["panel_recess"], s["collar_recess"]
    body = bmesh.new()
    fx, fy, _ = inner(floor_z)
    # The smooth inner wall and floor as one tapered tub; the outer bands hide
    # their inner faces in its wall, so no band joint shows inside the box.
    skin = bmesh.new()
    loops = []
    for (z, grow) in ((0, INNER_SKIN), (H, INNER_SKIN)):
        ix, iy, ir = inner(z)
        loops.append([(m(x), m(y), m(z)) for x, y in rr_outline(ix + grow, iy + grow, ir + grow)])
    for z in (H, floor_z):
        ix, iy, ir = inner(z)
        loops.append([(m(x), m(y), m(z)) for x, y in rr_outline(ix, iy, ir)])
    vs = [[skin.verts.new(pt) for pt in loop] for loop in loops]
    n = len(vs[0])
    for a, b in zip(vs, vs[1:]):
        for i in range(n):
            j = (i + 1) % n
            skin.faces.new((a[i], a[j], b[j], b[i]))
    skin.faces.new(vs[0][::-1])
    skin.faces.new(vs[-1])
    merge(body, skin, 0)
    ch = s["foot_chamfer"]
    # Outer profile from the floor up: foot, lit chamfer, panel, ledge lip, collar, rim.
    profile_ = ((1, 0), (1, foot1), (p, foot1 + ch), (p, ledge0), (0, ledge0), (0, collar0),
                (cr, collar0), (cr, rim0), (0, rim0), (0, H))
    merge(body, shell([(X - d, Y - d, R - d, z) for d, z in profile_], inner, grow=INNER_SKIN / 2), 0)
    web = s["rib_web"]
    deep = p + 1  # webs and blocks start buried behind the deepest recess

    def x_web(yc, sx):  # web across a long side, outer face on the envelope
        out = [(sx * (X - deep / 2) + x, yc + y) for x, y in rr_outline(deep / 2, web / 2, 0.0)]
        merge(body, prism_z(out, foot1, H - 1), 0)

    def y_web(xc, sy, z0, z1):  # web across a short side
        out = [(xc + x, sy * (Y - deep / 2) + y) for x, y in rr_outline(web / 2, deep / 2, 0.0)]
        merge(body, prism_z(out, z0, z1), 0)

    half_pair = (s["rib_pair_width"] - web) / 2
    pb = s["pin_block"]
    cutters = bmesh.new()
    hole_depth = 3
    for sx in (-1, 1):
        for sy in (-1, 1):
            x_web(sy * (Y - s["corner_web"]), sx)
            y_web(sx * (X - s["corner_web"]), sy, foot1, H - 1)
            # Pin block in the collar with its round hole.
            yc = sy * (Y - pb["from_corner"])
            blk = [(sx * (X - deep / 2) + x, yc + y) for x, y in rr_outline(deep / 2, pb["width"] / 2, 0.0)]
            merge(body, prism_z(blk, collar0, rim0 + 1), 0)
            bm_cylinder(cutters, (m(sx * X), m(yc), m((collar0 + rim0) / 2)), m(pb["hole"] / 2),
                        m(2 * hole_depth), "x", segments=12)
        for yr in s["long_side_rib_pairs"]:
            for d in (-half_pair, half_pair):
                x_web(-Y + yr + d, sx)
    fw, fh = hd["frame_width"] / 2, hd["frame_height"] / 2
    fz = H - hd["frame_top_below_rim"] - fh
    frame = offset_outline(rr_outline(fw, fh, hd["frame_radius"]), 0, fz)
    iy = inner(fz - fh)[1] - 1  # ends inside the wall at the frame's lowest, narrowest point
    rw = hd["rim_webs"]
    lip = s["ledge"]
    # The ledge lip steps round the frame: a shoulder one ledge wide, cut back to the frame face.
    shoulder = offset_outline(rr_outline(fw + lip, fh + lip, hd["frame_radius"] + lip), 0, fz)
    cl = s["clip"]
    band_w = (cl["outer_height"] - hd["pocket_height"]) / 2 - hd["clip_clearance"]  # as clip_ring
    tw, th = cl["outer_width"] / 2 - band_w, cl["outer_height"] / 2 - band_w
    tray = offset_outline(rr_outline(tw, th, cl["inner_radius"]), 0, fz)
    ow, oh = hd["pocket_width"] / 2, hd["pocket_height"] / 2
    oz = H - hd["pocket_top_below_rim"] - oh
    pocket = offset_outline(rr_outline(ow, oh, hd["pocket_radius"]), 0, oz)
    for sy in (-1, 1):
        merge(body, prism_y(frame, sy * Y, sy * iy), 0)
        for sx in (-1, 1):
            y_web(sx * (fw - rw["from_frame_edge"]), sy, fz, H - 1)
        merge(body, prism_y(shoulder, sy * Y, sy * (Y - deep)), 0)
        merge(cutters, prism_y(frame, sy * (Y + FRAME_PROUD), sy * (Y + 5)), 0)
        merge(cutters, prism_y(tray, sy * (Y - hd["tray_recess"]), sy * (Y + 4)), 0)
    body = boolean_cut(body, cutters)
    # Raised lip round the grip: a solid block standing on the tray floor, its
    # front 0.5 behind the frame face; the grip cut below hollows it to a rim.
    lw = hd["lip_width"]
    rolled = offset_outline(rr_outline(ow + lw, oh + lw, hd["pocket_radius"] + lw), 0, oz)
    for sy in (-1, 1):
        merge(body, prism_y(rolled, sy * (Y - hd["tray_recess"] - 1), sy * (Y + FRAME_PROUD - 0.5)), 0)
    # The grip is a closed pocket, not a hole: it stops short of the inner wall.
    grip = bmesh.new()
    for sy in (-1, 1):
        merge(grip, prism_y(pocket, sy * (Y + FRAME_PROUD - hd["pocket_depth"]), sy * (Y + 3)), 0)
    mesh = rounded_mesh(boolean_cut(body, grip), name, mat, BOX_EDGE_ROUND)
    shift = Matrix.Translation((0, m(Y), 0))
    mesh.transform(shift)
    return mesh


def clip_ring(bx, sy):
    """ColorClip round the grip pocket on the face of the handle frame of one
    short side, sy -1 the front, +1 the back; origin as the box."""
    s = RACK["box_shape"]
    hd, cl = s["handle"], s["clip"]
    H, Y = bx["height"], bx["length"] / 2
    zc = H - hd["frame_top_below_rim"] - hd["frame_height"] / 2
    band_w = (cl["outer_height"] - hd["pocket_height"]) / 2 - hd["clip_clearance"]
    ow, oh = cl["outer_width"] / 2, cl["outer_height"] / 2
    outer = offset_outline(rr_outline(ow, oh, cl["outer_radius"]), 0, zc)
    hole = offset_outline(rr_outline(ow - band_w, oh - band_w, cl["inner_radius"]), 0, zc)
    bm = bmesh.new()
    y0, y1 = sy * (Y + FRAME_PROUD), sy * (Y + FRAME_PROUD + cl["thickness"])
    if sy < 0:
        y0, y1 = y1, y0
    merge(bm, prism_y(outer, y0, y1, holes=hole), CLIP_EDGE_ROUND)
    bmesh.ops.translate(bm, verts=bm.verts[:], vec=(0, m(Y), 0))
    return bm


def check_box(mesh, bx):
    """Stop the build unless the box keeps its published outer size and inner top."""
    xs = [v.co.x for v in mesh.vertices]
    ys = [v.co.y for v in mesh.vertices]
    zs = [v.co.z for v in mesh.vertices]
    dx, dy, dz = (max(a) - min(a) for a in (xs, ys, zs))
    tol = 1e-6
    assert abs(dx - m(bx["width"])) < tol, f"{bx['article']}: width {dx * 1000:.2f}"
    assert abs(dz - m(bx["height"])) < tol, f"{bx['article']}: height {dz * 1000:.2f}"
    assert abs(dy - m(bx["length"])) < tol, f"{bx['article']}: length {dy * 1000:.2f}"
    ix, iy, _ = inner_wall(bx)(bx["height"])
    assert (2 * ix, 2 * iy) == (bx["inner_width"], bx["inner_length"]), f"{bx['article']}: inner top"


def clip_colour(level):
    return RACK["color_clips"]["levels"][str(level)]


def build_boxes(mats, colls):
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    ux = fr["upright_x"]
    front_y = RACK["box_position"]["front_y"]
    box_meshes, clip_meshes = {}, {}
    boxes = {}
    for lv in RACK["levels"]:
        key = RACK["model_boxes"][lv["class"]]
        bx = RACK["box_models"][key]
        if key not in box_meshes:
            box_meshes[key] = cycle_box(bx, mats["box_anthracite"], f"mesh.{key}")
            check_box(box_meshes[key], bx)
        for c in range(fr["columns"]):
            name = f"box.L{lv['level']}.C{c + 1}"
            xc = (ux[c] + sec + ux[c + 1]) / 2
            obj = place(name, box_meshes[key], colls["boxes"],
                        location=(m(xc), m(front_y), m(lv["floor"])))
            obj["kind"] = "box"
            obj["level"] = lv["level"]
            obj["column"] = c + 1
            obj["class"] = lv["class"]
            obj["model"] = key
            obj["travel"] = m(RACK["pull_out"]["travel"])
            obj["pull_axis"] = [0, 0, 1]
            obj["sides"] = list(RACK["pull_out"]["sides"])
            colour = clip_colour(lv["level"])
            # one ring per handle, so the exploded view can take each off its own side
            for sy, side in ((-1, "front"), (1, "back")):
                ck = (key, colour, side)
                if ck not in clip_meshes:
                    clip_meshes[ck] = to_mesh(f"mesh.clip.{key}.{colour}.{side}", clip_ring(bx, sy),
                                              mats[f"clip_{colour}"])
                clip = place(f"clip.L{lv['level']}.C{c + 1}.{colour}.{side}", clip_meshes[ck], colls["boxes"],
                             parent=obj)
                clip["kind"] = "clip"
                clip["colour"] = colour
            boxes[(lv["level"], c + 1)] = (obj, bx)
    return boxes


def check_insert(bx, key, x0, x1, y0, y1, z0):
    """Stop the build if an insert tray reaches through the tapered box wall.

    x0..x1, y0..y1: the tray's top outline in box coordinates around the box
    centre (mm); its bottom is bottom_inset smaller on every side.
    """
    ins = RACK["inserts"]
    inner = inner_wall(bx)
    for z, inset in ((z0, ins["bottom_inset"]), (z0 + ins["height"], 0.0)):
        hx, hy, _ = inner(z)
        over = max(-hx - (x0 + inset), (x1 - inset) - hx, -hy - (y0 + inset), (y1 - inset) - hy)
        assert over <= INSERT_FIT_TOLERANCE, f"insert {key} reaches {over:.2f} mm through the wall at z {z}"


def build_inserts(mats, colls, boxes):
    ins = RACK["inserts"]
    inset, floor = ins["bottom_inset"], ins["floor"]
    meshes = {}
    for key, layout_name in ins["boxes"].items():
        level, column = (int(part[1:]) for part in key.split("."))
        box, bx = boxes[(level, column)]
        rows = ins["layouts"][layout_name]
        row_w = ins["types"][rows[0][0]]["width"]
        x_start = -row_w * len(rows) / 2
        floor_z = bx["height"] - bx["inner_height"]
        for r, row in enumerate(rows):
            run = sum(ins["types"][t]["length"] for t in row)
            y = bx["length"] / 2 - run / 2
            for k, t in enumerate(row):
                size = ins["types"][t]
                w, l, h = size["width"], size["length"], ins["height"]
                if t not in meshes:
                    bm = hollow_tray(m(w), m(l), m(w - 2 * inset), m(l - 2 * inset), m(h),
                                     m(w - 2 * INSERT_WALL), m(l - 2 * INSERT_WALL),
                                     m(w - 2 * inset - 2 * INSERT_WALL),
                                     m(l - 2 * inset - 2 * INSERT_WALL), m(floor))
                    bevel_edges(bm, INSERT_EDGE_ROUND)
                    meshes[t] = to_mesh(f"mesh.insert.{t}", bm, mats["insert_grey"])
                cx = x_start + r * row_w + w / 2
                check_insert(bx, f"{key}.R{r + 1}.{k + 1}", cx - w / 2, cx + w / 2,
                             y - bx["length"] / 2, y + l - bx["length"] / 2, floor_z)
                loc = (m(cx), m(y + l / 2), m(floor_z))
                obj = place(f"insert.{key}.R{r + 1}.{k + 1}.{t}", meshes[t], colls["inserts"],
                            parent=box, location=loc)
                obj["kind"] = "insert"
                obj["type"] = t
                obj["part"] = ins["sets"][layout_name]
                y += l


def build_top_plate(mats, colls):
    tp = RACK["top_plate"]
    x0 = -tp["overhang"]
    y0 = -(tp["depth"] - RACK["frame"]["depth"]) / 2
    hx, hy = tp["width"] / 2, tp["depth"] / 2
    # mesh z starts at 0 so the ply pattern reads object z directly
    bm = prism_z(rr_outline(hx, hy, tp["corner_radius"], segments=12), 0, tp["thickness"])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    bevel_edges(bm, tp["edge_round"])
    mesh = weighted_normals(to_mesh("plate.top", bm, mats["plywood"]), "plate.top")
    obj = place("plate.top", mesh, colls["top_plate"],
                location=(m(x0 + hx), m(y0 + hy), m(tp["top"] - tp["thickness"])))
    obj["kind"] = "plate"
    obj["status"] = tp["status"]
    # The procedural plywood does not survive the glb; the viewer redraws it
    # from these values (mesh z from the plate's bottom, sRGB colours).
    obj["plywood"] = {
        "thickness": tp["thickness"], "plies": tp["plies"],
        "face_dark": PLY_FACE[0], "face_light": PLY_FACE[1], "grain": PLY_GRAIN,
        "ply_long": PLY_LONG, "ply_cross": PLY_CROSS, "glue": PLY_GLUE,
        "grain_spacing_mm": 5.0, "glue_width": PLY_GLUE_WIDTH,
    }
    return obj


# ---------------------------------------------------------------- stage, cameras, renders

def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def area_light(coll, name, energy, size, location, target, size_y=None):
    light = bpy.data.lights.new(name, "AREA")
    light.energy = energy
    light.shape = "RECTANGLE"
    light.size = size
    light.size_y = size_y or size
    obj = bpy.data.objects.new(name, light)
    obj.location = location
    coll.objects.link(obj)
    look_at(obj, target)
    return obj


BACKDROP = (0.62, 0.63, 0.65, 1)  # linear; what the camera sees past the floor


def fade_floor(mat, centre, colour):
    """Blend the floor into the backdrop colour from 2 to 5 m off the rack, so
    the floor has no visible edge or horizon."""
    nodes, links = mat.node_tree.nodes, mat.node_tree.links
    bsdf = nodes["Principled BSDF"]
    out = nodes["Material Output"]
    coords = nodes.new("ShaderNodeTexCoord")
    offset = nodes.new("ShaderNodeVectorMath")
    offset.operation = "SUBTRACT"
    offset.inputs[1].default_value = (centre[0], centre[1], 0.0)
    dist = nodes.new("ShaderNodeVectorMath")
    dist.operation = "LENGTH"
    ramp = nodes.new("ShaderNodeMapRange")
    ramp.inputs["From Min"].default_value = 2.0
    ramp.inputs["From Max"].default_value = 5.0
    glow = nodes.new("ShaderNodeEmission")
    glow.inputs["Color"].default_value = colour
    path = nodes.new("ShaderNodeLightPath")
    camera_only = nodes.new("ShaderNodeMath")
    camera_only.operation = "MULTIPLY"
    mix = nodes.new("ShaderNodeMixShader")
    links.new(coords.outputs["Object"], offset.inputs[0])
    links.new(offset.outputs["Vector"], dist.inputs[0])
    links.new(dist.outputs["Value"], ramp.inputs["Value"])
    links.new(ramp.outputs["Result"], camera_only.inputs[0])
    links.new(path.outputs["Is Camera Ray"], camera_only.inputs[1])
    links.new(camera_only.outputs["Value"], mix.inputs["Fac"])
    links.new(bsdf.outputs["BSDF"], mix.inputs[1])
    links.new(glow.outputs["Emission"], mix.inputs[2])
    links.new(mix.outputs["Shader"], out.inputs["Surface"])


def build_stage(scene, mats, colls):
    """Studio: a wide floor, three soft area lights and a light grey backdrop that
    only the camera sees, so every view gets a clean background."""
    cx, cy, cz = 0.53, 0.22, 0.5
    bm = bmesh.new()
    bm_box(bm, (-20, -20, -0.01), (20, 20, 0))
    floor = finish("stage.floor", bm, mats["floor"], colls["stage"])
    fade_floor(floor.data.materials[0], (cx, cy), BACKDROP)
    # A smaller, higher key from the left grazes the box walls so the ribs
    # cast shadows; the fill stays about a quarter of it.
    area_light(colls["stage"], "stage.key", 260, 0.8, (cx - 2.6, -2.0, 3.0), (cx, cy, cz))
    area_light(colls["stage"], "stage.fill", 55, 3.0, (cx + 2.8, -2.0, 1.4), (cx, cy, cz))
    area_light(colls["stage"], "stage.top", 80, 2.4, (cx, cy, 3.2), (cx, cy, 0), size_y=1.2)
    area_light(colls["stage"], "stage.rim", 100, 2.0, (cx + 0.5, 3.0, 2.2), (cx, cy, cz))

    world = bpy.data.worlds.new("stage.world")
    nodes, links = world.node_tree.nodes, world.node_tree.links
    background = nodes["Background"]
    background.inputs["Color"].default_value = (0.62, 0.63, 0.65, 1)
    background.inputs["Strength"].default_value = 0.8
    backdrop = nodes.new("ShaderNodeBackground")
    backdrop.inputs["Color"].default_value = BACKDROP
    backdrop.inputs["Strength"].default_value = 1.0
    path = nodes.new("ShaderNodeLightPath")
    mix = nodes.new("ShaderNodeMixShader")
    links.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
    links.new(background.outputs["Background"], mix.inputs[1])
    links.new(backdrop.outputs["Background"], mix.inputs[2])
    links.new(mix.outputs["Shader"], nodes["World Output"].inputs["Surface"])
    scene.world = world

    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1200
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    # No metadata in the PNGs: it holds the render time, which changes every
    # run, and the path of the .blend.
    for prop in scene.render.bl_rna.properties:
        if prop.identifier.startswith("use_stamp"):
            setattr(scene.render, prop.identifier, False)
    # Screen-space ray tracing at full resolution gives the rib pockets their
    # contact shadows; only the spatial denoiser, which works within one frame.
    eevee = scene.eevee
    eevee.taa_render_samples = EEVEE_SAMPLES
    eevee.use_raytracing = True
    eevee.ray_tracing_method = "SCREEN"
    rt = eevee.ray_tracing_options
    rt.resolution_scale = "1"
    rt.use_denoise = True
    rt.denoise_spatial = True
    rt.denoise_temporal = False
    rt.denoise_bilateral = True
    eevee.use_fast_gi = True
    eevee.fast_gi_method = "GLOBAL_ILLUMINATION"
    eevee.use_shadows = True
    eevee.shadow_ray_count = 3
    eevee.shadow_step_count = 12
    scene.view_settings.view_transform = "AgX"
    scene.view_settings.look = "AgX - Punchy"


def camera(scene, coll, name, location, target, ortho_scale=None, lens=50):
    cam = bpy.data.cameras.new(name)
    if ortho_scale:
        cam.type = "ORTHO"
        cam.ortho_scale = ortho_scale
    else:
        cam.lens = lens
    cam.clip_end = 100
    obj = bpy.data.objects.new(name, cam)
    obj.location = location
    coll.objects.link(obj)
    look_at(obj, target)
    return obj


def model_bounds(exclude=()):
    """Bounding box (lo, hi) of all visible meshes outside `exclude`."""
    lo = [float("inf")] * 3
    hi = [float("-inf")] * 3
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH" or not obj.visible_get():
            continue
        if any(c.name in exclude for c in obj.users_collection):
            continue
        for corner in obj.bound_box:
            w = obj.matrix_world @ Vector(corner)
            for i in range(3):
                lo[i] = min(lo[i], w[i])
                hi[i] = max(hi[i], w[i])
    return Vector(lo), Vector(hi)


def fit_camera(cam, lo, hi, margin=1.0):
    """Move a perspective camera along its view axis until the box lo..hi fits
    the render's frame; its direction and aim stay."""
    scene = bpy.context.scene
    data = cam.data
    aspect = scene.render.resolution_x / scene.render.resolution_y
    half_w = data.sensor_width / 2 / data.lens  # tan of the half field of view across
    half_h = half_w / aspect
    rot = cam.rotation_euler.to_matrix()  # matrix_world is stale until the next update
    right, up, back = rot.col[0], rot.col[1], rot.col[2]
    aim = (lo + hi) / 2
    need = 0.0
    for i in range(8):
        c = Vector((hi.x if i & 1 else lo.x, hi.y if i & 2 else lo.y, hi.z if i & 4 else lo.z)) - aim
        x, y, z = c.dot(right), c.dot(up), c.dot(back)
        need = max(need, z + abs(x) * margin / half_w, z + abs(y) * margin / half_h)
    cam.location = aim + back * need


def model_center(exclude=()):
    """Centre of the bounding box of all visible meshes outside `exclude`."""
    lo, hi = model_bounds(exclude)
    return (lo + hi) / 2


def center_rotation():
    """Place the 3D cursor and the viewport's rotation pivot at the middle of
    the model, so opening the file and orbiting turns the rack around itself
    and not around the floor corner at the world origin."""
    centre = model_center(exclude=("stage",))
    bpy.context.scene.cursor.location = centre
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                view = area.spaces.active.region_3d
                view.view_location = centre
                view.view_distance = 3.0


def shaded_viewports():
    """Open every 3D view of the saved file in Material Preview (EEVEE), so the
    window shows the shaders (the plywood plies, the grain) and not the flat
    viewport colours of Solid shading. Rendered shading would be closer to the
    renders, but Blender resets a saved Rendered view to Solid on loading."""
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == "VIEW_3D":
                area.spaces.active.shading.type = "MATERIAL"


def strip_png_text(path):
    """Drop any text chunks the renderer writes even with every stamp off; they
    can hold the render time, so a second run would not give the same file."""
    data = open(path, "rb").read()
    out, i = [data[:8]], 8
    while i < len(data):
        length = struct.unpack(">I", data[i:i + 4])[0]
        chunk = data[i:i + 12 + length]
        if chunk[4:8] not in (b"tEXt", b"iTXt", b"zTXt"):
            out.append(chunk)
        i += 12 + length
    with open(path, "wb") as f:
        f.write(b"".join(out))


def render(scene, cam, filename):
    scene.camera = cam
    scene.render.filepath = os.path.join(RENDERS, filename)
    bpy.ops.render.render(write_still=True)
    strip_png_text(scene.render.filepath)
    print("rendered", filename)


# ---------------------------------------------------------------- exploded view

EXPLODE_STEPS = 3  # the boxes out to the front; the boxes up and aside; everything else


def explode_world(obj, memo):
    """Where the exploded view moves obj, world vectors in mm, one per step
    (rack.json → explode). The boxes leave first: straight out to the front of
    their bay, then up and aside, clear of the rack; only then does the rest
    move, so no part passes through another. A screw, nut, washer or cap moves
    with the part that holds it and then out of its hole; the inserts lift out
    of their box and the rings come off its handles in the last step."""
    if obj.name in memo:
        return memo[obj.name]
    E, fr = RACK["explode"], RACK["frame"]
    up, top = E["frame_up"], E["frame_up"] + E["top_up"]
    world = world_of(obj)
    loc = world.translation * 1000
    side = -1 if loc.y < fr["depth"] / 2 else 1  # the front frame moves to the front, -y
    name = obj.name
    mesh_part = obj.data.get("part") if obj.type == "MESH" else None
    steps = [Vector() for _ in range(EXPLODE_STEPS)]
    last = steps[-1]
    if mesh_part:
        out = -(world.to_3x3() @ Z).normalized()  # back out of the hole
        f = RACK["fasteners"]
        if mesh_part in f["screws"]:
            d = E["screw_lengths_out"] * f["screws"][mesh_part]["length"]
        elif mesh_part in f["nuts"]:
            d = E["nuts_out"]
        elif mesh_part in f["washers"]:
            d = E["washers_out"]
        else:
            out, d = -out, E["caps_out"]  # a cap's own axis points out of the bar end
        steps = [v.copy() for v in explode_world(obj.parent, memo)]
        steps[-1] += out * d
    elif name.startswith(("upright.", "bar.bottom.")):
        last[:] = (0, side * E["frames_apart"], up)
    elif name.startswith("bar.top."):
        last[:] = (0, side * E["frames_apart"], top)
    elif name.startswith("beam.depth."):
        last[:] = (0, 0, top if ".top." in name else up)
    elif name.startswith("bracket.plate."):
        last[:] = (0, side * E["frames_apart"], top + E["plate_brackets_up"])
    elif name.startswith("bracket."):
        last[:] = (0, side * E["brackets_apart"], top if loc.z > fr["top_bar"]["bottom"] - 40 else up)
    elif name.startswith("angle."):
        last[:] = ((1 if name.endswith(".left") else -1) * E["angles_in"], 0, up)
    elif name.startswith("plate.castor."):
        last[:] = (0, 0, E["castor_plates_up"])
    elif name == "plate.top":
        last[:] = (0, 0, top + E["plate_up"])
    elif name.startswith("box."):
        # out of the bay to the front, then up, each level further than the one
        # below so its inserts clear the box above, and aside past the rack
        steps[0][:] = (0, -E["boxes_forward"], 0)
        steps[1][:] = (E["boxes_aside"], 0, up + (obj["level"] - 1) * E["box_levels_apart"])
    elif name.startswith("insert."):
        steps = [v.copy() for v in explode_world(obj.parent, memo)]
        steps[-1] += Vector((0, 0, E["inserts_up"]))
    elif name.startswith("clip."):
        out = -1 if name.endswith(".front") else 1
        steps = [v.copy() for v in explode_world(obj.parent, memo)]
        steps[-1] += Vector((0, out * E["clips_off"], 0))
    elif obj.parent is not None:
        steps = explode_world(obj.parent, memo)
    memo[obj.name] = steps
    return steps


def check_boxes_clear():
    """Stop the build unless a box pulled out by boxes_forward has left the rack:
    its back clear of the frame's front, the top plate's overhang and the rings."""
    E, tp = RACK["explode"], RACK["top_plate"]
    overhang = (tp["depth"] - RACK["frame"]["depth"]) / 2
    back = RACK["box_position"]["front_y"] + max(b["length"] for b in RACK["box_models"].values())
    ring = RACK["box_shape"]["clip"]["thickness"]
    assert back + ring - E["boxes_forward"] < -overhang, "boxes_forward does not take the boxes out of the rack"


def build_explode(scene, colls):
    """A scene property `explode` from 0 to 1 drives every part from its place to
    its exploded place in EXPLODE_STEPS steps, each a third of the range: one
    simple-expression driver per moving axis on the object's delta location, in
    its parent's axes, `<metres>*clamp(e*3-<step>,0,1)` summed over the steps,
    so Blender runs them without Python auto-run. export_web.py reads them back
    for the viewer."""
    check_boxes_clear()
    scene["explode"] = 0.0
    scene.id_properties_ui("explode").update(min=0.0, max=1.0, soft_min=0.0, soft_max=1.0, step=10,
                                             description="0 assembled, 1 exploded (rack.json → explode)")
    memo = {}
    drivers = 0
    n = EXPLODE_STEPS
    for obj in bpy.data.objects:
        if any(c.name == "stage" for c in obj.users_collection):
            continue
        steps = explode_world(obj, memo)
        if obj.parent is not None:
            inv = world_of(obj.parent).to_3x3().inverted()
            steps = [inv @ (v - p) for v, p in zip(steps, explode_world(obj.parent, memo))]
        for i in range(3):
            terms = []
            for k, v in enumerate(steps):
                d = round(m(v[i]), 6)
                if abs(d) >= 1e-6:
                    terms.append(f"{d:g}*clamp(e*{n}-{k},0,1)")
            if not terms:
                continue
            drv = obj.driver_add("delta_location", i).driver
            drv.type = "SCRIPTED"
            var = drv.variables.new()
            var.name = "e"
            var.targets[0].id_type = "SCENE"
            var.targets[0].id = scene
            var.targets[0].data_path = '["explode"]'
            drv.expression = "+".join(terms)
            assert drv.is_simple_expression, drv.expression
            drivers += 1
    print("explode drivers:", drivers)


def set_explode(scene, k):
    """Set `explode` and evaluate the drivers, so matrix_world follows at once."""
    scene["explode"] = k
    scene.update_tag()
    bpy.context.view_layer.update()
    scene.frame_set(scene.frame_current)


def check_parts():
    """Stop the build unless the model holds every build part of the catalog as
    often as the parts list says. An insert set counts once per box, a ColorClip
    set (two rings, one per handle) once per box."""
    ins = RACK["inserts"]
    per_set = {ins["sets"][k]: sum(len(row) for row in layout) for k, layout in ins["layouts"].items()}
    per_set.update({f"clip.{c}": 2 for c in set(RACK["color_clips"]["levels"].values())})
    counts = {}
    for obj in bpy.data.objects:
        part = object_part(obj)
        if obj.get("kind") == "clip":
            part = f"clip.{obj['colour']}"
        if part:
            counts[part] = counts.get(part, 0) + 1
    for part, n in per_set.items():
        counts[part] = counts.get(part, 0) / n
    want = {p["id"]: p["quantity"] for p in RACK["parts"] if p["status"] == "build" and p["unit"] == "piece"}
    wrong = {p: (counts.get(p, 0), q) for p, q in want.items() if counts.get(p, 0) != q}
    extra = sorted(set(counts) - set(want))
    assert not wrong and not extra, f"model counts (drawn, listed): {wrong}; not in the parts list: {extra}"
    print("parts check:", sum(want.values()), "pieces of", len(want), "part IDs")


def main():
    global SECTION
    sec = RACK["frame"]["profile"]["section"]
    SECTION = rect_section(sec, sec)
    scene = reset_scene()
    mats = make_materials()
    MATS.update(mats)
    names = ["frame", "angles", "fasteners", "castors", "boxes", "inserts", "top_plate", "stage"]
    colls = {n: collection(scene, n) for n in names}
    COLLS.update(colls)

    frame_root = bpy.data.objects.new("frame", None)
    frame_root["kind"] = "frame"
    colls["frame"].objects.link(frame_root)
    build_frame(mats, colls, frame_root)
    build_angles(mats, colls, frame_root)
    build_brackets(mats, colls, frame_root)
    build_castor_plates(mats, colls, frame_root)
    build_castors(mats, colls, frame_root)
    boxes = build_boxes(mats, colls)
    build_inserts(mats, colls, boxes)
    plate = build_top_plate(mats, colls)
    plate["part"] = "plate.top"
    for box, _ in boxes.values():
        box["part"] = "box.e120" if box["class"] == "120" else "box.e220"
    check_parts()

    scene["rack_schema"] = RACK["schema"]
    out = RACK["outer"]
    scene["outer_mm"] = [out["width"], out["depth"], out["height"]]

    build_stage(scene, mats, colls)
    build_explode(scene, colls)

    W, D, H = m(out["width"]), m(out["depth"]), m(out["height"])
    cx, cy, cz = m(RACK["frame"]["width"]) / 2, D / 2, H / 2
    cams = colls["stage"]
    front = camera(scene, cams, "cam.front", (cx, -10, cz), (cx, 0, cz),
                   ortho_scale=max(W, H * 4 / 3) * 1.12)
    side = camera(scene, cams, "cam.side", (-10, cy, cz), (0, cy, cz), ortho_scale=H * 1.2 * 4 / 3)
    three = camera(scene, cams, "cam.three_quarter", (cx - 1.5, -2.2, 1.55), (cx, cy, cz * 0.9), lens=42)
    drawer = camera(scene, cams, "cam.drawer_out", (cx - 1.4, -2.2, 1.55), (cx, cy - 0.15, cz * 0.95), lens=40)
    top = camera(scene, cams, "cam.inserts_top", (cx, 0, 10), (cx, 0, 0), ortho_scale=W * 1.4)

    os.makedirs(RENDERS, exist_ok=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.context.view_layer.update()
    center_rotation()
    shaded_viewports()
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "rack.blend"), compress=True)

    render(scene, front, "front.png")
    render(scene, side, "side.png")
    render(scene, three, "three_quarter.png")

    box, _ = boxes[(3, 2)]
    home = box.location.copy()
    box.location.y -= m(RACK["pull_out"]["travel"])
    render(scene, drawer, "drawer_out.png")
    box.location = home

    # Top view: frame and top plate hidden, every level with inserts taken out
    # and staged in its own row, so all twelve 120 boxes and their inserts are
    # visible.
    hidden = [colls[n] for n in ("frame", "angles", "castors", "top_plate")]
    for coll in hidden:
        coll.hide_render = True
    length = m(RACK["box_models"][RACK["model_boxes"]["120"]]["length"])
    step = length + m(STAGE_GAP)
    staged = [lv["level"] for lv in RACK["levels"] if (lv["level"], 1) in boxes and
              f"L{lv['level']}.C1" in RACK["inserts"]["boxes"]]
    moved = {}
    for i, level in enumerate(reversed(staged)):
        shift = i * step  # the top level stays, the next ones move forward one row each
        moved[level] = shift
        for c in range(1, RACK["frame"]["columns"] + 1):
            boxes[(level, c)][0].location.y -= shift
    y_min = -max(moved.values()) if moved else 0.0
    span = length - y_min  # rows run from y_min (front row) to length (back row)
    y_mid = y_min + span / 2
    top.location.y = y_mid
    top.data.ortho_scale = max(W, span / 0.75) * 1.06
    look_at(top, (cx, y_mid, 0))
    render(scene, top, "inserts_top.png")
    for level, shift in moved.items():
        for c in range(1, RACK["frame"]["columns"] + 1):
            boxes[(level, c)][0].location.y += shift
    for coll in hidden:
        coll.hide_render = False

    # Close-up of the left support angle of column 2 at level 3, front end.
    fr = RACK["frame"]
    lv3 = next(l for l in RACK["levels"] if l["level"] == 3)
    ax = m(fr["upright_x"][1] + fr["profile"]["section"])
    az = m(lv3["floor"])
    detail = camera(scene, cams, "cam.angle_detail", (ax + 0.16, -0.45, az + 0.10),
                    (ax + 0.02, 0.0, az - 0.01), lens=45)
    render(scene, detail, "angle_detail.png")

    # Exploded, from the front left and above, just far enough back that every
    # corner of the exploded model's bounding box is inside the 4:3 picture.
    set_explode(scene, 1.0)
    lo, hi = model_bounds(exclude=("stage",))
    aim = (lo + hi) / 2
    exploded = camera(scene, cams, "cam.exploded", aim + Vector((-2.4, -1.5, 1.4)), aim, lens=42)
    fit_camera(exploded, lo, hi, margin=1.06)
    render(scene, exploded, "exploded.png")
    set_explode(scene, 0.0)


main()
