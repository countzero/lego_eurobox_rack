"""Build the LEGO Eurobox rack from design/rack.json, save rack.blend, render.

Run headless from the repository root:
    blender --background --factory-startup --python-exit-code 1 --python blender/build_rack.py

Every structural dimension comes from design/rack.json (millimetres); the
model is in metres. Only visual details (slot depth, castor shape, edge
rounds, colours, cameras, lights) are set here. The renders use EEVEE
without ray tracing, so a second run gives the same files.
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
    "plywood": ((0.80, 0.64, 0.44, 1), 0.0, 0.6, 1.5),
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


def profile(name, axis, centre_a, centre_b, start, end, mat, coll, parent, section=None):
    """Slotted profile along axis from start to end (mm); section in the other two axes."""
    section = section or SECTION
    bm = bmesh.new()
    rings = []
    for t in (m(start), m(end)):
        ring = []
        for a, b in section:
            a, b = a + m(centre_a), b + m(centre_b)
            p = {"x": (t, a, b), "y": (a, t, b), "z": (a, b, t)}[axis]
            ring.append(bm.verts.new(p))
        rings.append(ring)
    n = len(section)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((rings[0][i], rings[0][j], rings[1][j], rings[1][i]))
    bm.faces.new(rings[0])
    bm.faces.new(rings[1][::-1])
    return finish(name, bm, mat, coll, parent)


# ---------------------------------------------------------------- the rack

def build_frame(mats, colls, frame_root):
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    h = sec / 2
    al, coll = mats["aluminium"], colls["frame"]
    ux, uy = fr["upright_x"], fr["upright_y"]
    up = fr["upright"]
    for i, x in enumerate(ux):
        for y, side in zip(uy, ("front", "back")):
            profile(f"upright.{i + 1}.{side}", "z", x + h, y + h, up["bottom"], up["top"],
                    al, coll, frame_root)
    bb, tb = fr["bottom_bar"], fr["top_bar"]
    bar_section = rect_section(bb["depth"], bb["height"])
    for y, side in zip(uy, ("front", "back")):
        profile(f"bar.bottom.{side}", "x", y + bb["depth"] / 2, (bb["bottom"] + bb["top"]) / 2,
                0, bb["length"], al, coll, frame_root, section=bar_section)
        profile(f"bar.top.{side}", "x", y + h, (tb["bottom"] + tb["top"]) / 2,
                0, tb["length"], al, coll, frame_root)
    db = fr["depth_beam"]
    for i, x in enumerate(ux):
        for lvl in ("bottom", "top"):
            zz = db[lvl]
            profile(f"beam.depth.{lvl}.{i + 1}", "y", x + h, (zz["bottom"] + zz["top"]) / 2,
                    uy[0] + sec, uy[1], al, coll, frame_root)


def build_plates(mats, colls, frame_root):
    """Joint plates on the outer faces of the front and the back frame."""
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    jp = fr["joint_plate"]
    t, size = jp["thickness"], jp["size"]
    ux, last = fr["upright_x"], len(fr["upright_x"]) - 1
    bb, tb = fr["bottom_bar"], fr["top_bar"]
    joints = (("bottom", bb["top"] - sec, bb["top"], +1), ("top", tb["bottom"], tb["top"], -1))
    for y0, side in ((-t, "front"), (fr["depth"], "back")):
        for i, x in enumerate(ux):
            kind = "l" if i in (0, last) else "t"
            for lvl, z0, z1, up in joints:
                bm = bmesh.new()
                vz = (z0, z0 + size) if up > 0 else (z1 - size, z1)
                mm_box(bm, x, x + sec, y0, y0 + t, *vz)
                if kind == "t":
                    hx = (x - sec, x + 2 * sec)
                else:
                    hx = (x, x + size) if i == 0 else (x + sec - size, x + sec)
                mm_box(bm, *hx, y0, y0 + t, z0, z1)
                finish(f"plate.{kind}.{side}.{lvl}.{i + 1}", bm, mats["aluminium"],
                       colls["frame"], frame_root)


def angle(name, x_face, inward, z_flat_lo, flat_up, mats, coll, parent):
    """L angle along y. x_face: upright face, inward: +1 or -1.

    flat_up=True: flat leg on top at z_flat_lo..+t, hanging leg down.
    flat_up=False: flat leg at the bottom, vertical leg up.
    """
    a = RACK["angles"]
    leg, t, length = a["section"]["leg"], a["section"]["thickness"], a["length"]
    zf0, zf1 = z_flat_lo, z_flat_lo + t
    zl0, zl1 = (zf1 - leg, zf1) if flat_up else (zf0, zf0 + leg)
    bm = bmesh.new()
    mm_box(bm, x_face, x_face + inward * leg, 0, length, zf0, zf1)
    mm_box(bm, x_face, x_face + inward * t, 0, length, zl0, zl1)
    bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=1e-6)
    return finish(name, bm, mats["aluminium"], coll, parent)


def bay_faces(c):
    fr = RACK["frame"]
    ux, sec = fr["upright_x"], fr["profile"]["section"]
    return ((ux[c] + sec, +1, "left"), (ux[c + 1], -1, "right"))


def build_angles(mats, colls, frame_root):
    fr, a = RACK["frame"], RACK["angles"]
    t = a["section"]["thickness"]
    for c in range(fr["columns"]):
        for lv in RACK["levels"]:
            for x_face, inward, side in bay_faces(c):
                if lv["angle"] == "angle.base":
                    angle(f"angle.base.L{lv['level']}.C{c + 1}.{side}", x_face, inward,
                          a["base"]["flat_leg_top"] - t, False, mats, colls["angles"], frame_root)
                else:
                    angle(f"angle.support.L{lv['level']}.C{c + 1}.{side}", x_face, inward,
                          lv["floor"] - t, True, mats, colls["angles"], frame_root)
        for x_face, inward, side in bay_faces(c):
            angle(f"angle.guard.C{c + 1}.{side}", x_face, inward,
                  RACK["tip_guard"]["flat_leg_bottom"], True, mats, colls["angles"], frame_root)


def build_brackets(mats, colls, frame_root):
    """Inside brackets 30: L of two 30 mm legs, 3 thick, 20 wide, per the joints of rack.json."""
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    ux, uy = fr["upright_x"], fr["upright_y"]
    db, tb = fr["depth_beam"], fr["top_bar"]
    leg, t, w = 30, 3, 20
    last = len(ux) - 1
    pieces = []
    for y_face, dy in ((uy[0] + sec, +1), (uy[1], -1)):
        ya, yt, yl = y_face, y_face + dy * t, y_face + dy * leg
        for i, x in enumerate(ux):
            xm0, xm1 = x + (sec - w) / 2, x + (sec + w) / 2
            # upright to top depth beam: vertical leg on the upright, flat leg under the beam
            zt = db["top"]["bottom"]
            pieces.append([(xm0, xm1, ya, yt, zt - leg, zt), (xm0, xm1, ya, yl, zt - t, zt)])
            # top depth beam to bar, on the beam's bay side
            xf, dx = (x, -1) if i == last else (x + sec, +1)
            z0 = (tb["bottom"] + tb["top"] - w) / 2
            pieces.append([(xf, xf + dx * leg, ya, yt, z0, z0 + w), (xf, xf + dx * t, ya, yl, z0, z0 + w)])
            # bottom depth beam's top face to bar
            zb = db["bottom"]["top"]
            pieces.append([(xm0, xm1, ya, yl, zb, zb + t), (xm0, xm1, ya, yt, zb, zb + leg)])
            # bottom depth beam's side to bar, middle uprights only
            if 0 < i < last:
                z0 = (db["bottom"]["bottom"] + db["bottom"]["top"] - w) / 2
                xf = x + sec
                pieces.append([(xf, xf + leg, ya, yt, z0, z0 + w), (xf, xf + t, ya, yl, z0, z0 + w)])
    for n, boxes in enumerate(pieces, 1):
        bm = bmesh.new()
        for b in boxes:
            mm_box(bm, *b)
        bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=1e-6)
        finish(f"bracket.{n}", bm, mats["aluminium"], colls["frame"], frame_root)


def corners():
    """Frame corners in the order front-left, front-right, back-left, back-right: (x sign, y sign)."""
    return ((+1, +1), (-1, +1), (+1, -1), (-1, -1))


def build_castor_plates(mats, colls, frame_root):
    fr = RACK["frame"]
    cp = fr["castor_plate"]
    W, D, s = fr["width"], fr["depth"], cp["size"]
    for n, (sx, sy) in enumerate(corners(), 1):
        x0 = 0 if sx > 0 else W
        y0 = 0 if sy > 0 else D
        assert min(x0, x0 + sx * s) >= 0 and max(x0, x0 + sx * s) <= W
        assert min(y0, y0 + sy * s) >= 0 and max(y0, y0 + sy * s) <= D
        bm = bmesh.new()
        mm_box(bm, x0, x0 + sx * s, y0, y0 + sy * s, cp["bottom"], cp["top"])
        finish(f"plate.castor.{n}", bm, mats["aluminium"], colls["frame"], frame_root)


def build_castors(mats, colls, frame_root):
    """Plain swivel castors 1-4 at front-left, front-right, back-left, back-right; wheels trail inward."""
    fr = RACK["frame"]
    ca = fr["castor"]
    h = fr["castor_height"]
    W, D, inset = fr["width"], fr["depth"], ca["inset"]
    head_r, wheel_r = ca["head_diameter"] / 2, ca["wheel"] / 2
    tw, off = ca["tread_width"], ca["offset"]
    for n, (sx, sy) in enumerate(corners(), 1):
        cx = inset if sx > 0 else W - inset
        cy = inset if sy > 0 else D - inset
        assert head_r <= cx <= W - head_r and head_r <= cy <= D - head_r, "castor head outside"
        bm = bmesh.new()
        bm_cylinder(bm, (0, 0, m(h - 4)), m(head_r), m(8), "z")
        bm_cylinder(bm, (0, 0, m(h - 12)), m(head_r * 0.7), m(8), "z")
        ox = tw / 2 + 4
        mm_box(bm, -ox - 3, ox + 3, -12, sy * off + sy * 12, h - 22, h - 16)
        for k in (-1, 1):
            mm_box(bm, k * ox, k * (ox + 3), sy * (off - 18), sy * (off + 12), wheel_r - 8, h - 16)
        bm_cylinder(bm, (0, m(sy * off), m(wheel_r)), m(wheel_r), m(tw), "x")
        bm_cylinder(bm, (0, m(sy * off), m(wheel_r)), m(6), m(2 * ox + 8), "x", segments=12)
        obj = finish(f"castor.plain.{n}", bm, mats["castor"], colls["castors"], frame_root)
        obj.location = (m(cx), m(cy), 0)


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


def band(outer, inner_at, z0, z1, grow=0.0):
    """Wall band: a vertical rounded outer face and the tapered inner face,
    moved out by grow (mm) so it can hide inside another piece."""
    (ox, oy, r) = outer
    bm = bmesh.new()
    loops = [[(m(x), m(y), m(z)) for x, y in rr_outline(ox, oy, r)] for z in (z0, z1)]
    for z in (z1, z0):
        ix, iy, ir = inner_at(z)
        loops.append([(m(x), m(y), m(z)) for x, y in rr_outline(ix + grow, iy + grow, ir + grow)])
    loft(bm, loops, closed=True)
    return bm


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


def boolean_cut(body, cutter, name, mat):
    """body minus cutter with the manifold solver; overlapping pieces of body are united."""
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
    mod.solver = "MANIFOLD"
    mod.use_self = True
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(body_obj.evaluated_get(depsgraph))
    result.name = name
    for obj in objs:
        mesh = obj.data
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)
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
    merge(body, skin, BOX_EDGE_ROUND)
    for inset, z0, z1 in ((1, 0, foot1), (p, foot1, ledge0), (0, ledge0, collar0),
                          (cr, collar0, rim0), (0, rim0, H)):
        merge(body, band((X - inset, Y - inset, R - inset), inner, z0, z1, grow=INNER_SKIN / 2),
              BOX_EDGE_ROUND)
    cp = s["corner_post"] / 2
    for sx in (-1, 1):
        for sy in (-1, 1):
            # The outer corner of the post follows the box corner; the others are buried in the wall.
            radii = [0.0] * 4
            radii[{(1, 1): 0, (-1, 1): 1, (-1, -1): 2, (1, -1): 3}[(sx, sy)]] = R
            post = [(sx * (X - cp) + x, sy * (Y - cp) + y) for x, y in rr_outline(cp, cp, radii)]
            merge(body, prism_z(post, foot1, ledge0), BOX_EDGE_ROUND)
        for r0, r1 in s["long_side_ribs"]:
            rib = rr_outline((p + 2) / 2, (r1 - r0) / 2, 0.0)
            rib = [(sx * (X - (p + 2) / 2) + x, -Y + (r0 + r1) / 2 + y) for x, y in rib]
            merge(body, prism_z(rib, foot1, ledge0), BOX_EDGE_ROUND)
    fw, fh = hd["frame_width"] / 2, hd["frame_height"] / 2
    fz = H - hd["frame_top_below_rim"] - fh
    frame = offset_outline(rr_outline(fw, fh, hd["frame_radius"]), 0, fz)
    iy = inner(fz - fh)[1] - 1  # ends inside the wall at the frame's lowest, narrowest point
    for sy in (-1, 1):
        merge(body, prism_y(frame, sy * (Y + FRAME_PROUD), sy * iy), BOX_EDGE_ROUND)
    ow, oh = hd["opening_width"] / 2, hd["opening_height"] / 2
    oz = H - hd["opening_top_below_rim"] - oh
    cutter = prism_y(offset_outline(rr_outline(ow, oh, hd["opening_radius"]), 0, oz),
                     -(Y + 20), Y + 20)
    mesh = boolean_cut(body, cutter, name, mat)
    shift = Matrix.Translation((0, m(Y), 0))
    mesh.transform(shift)
    return mesh


def clip_ring(bx):
    """ColorClip round the handle opening on the face of the handle frame, both
    short sides; origin as the box."""
    s = RACK["box_shape"]
    hd, cl = s["handle"], s["clip"]
    H, Y = bx["height"], bx["length"] / 2
    zc = H - hd["frame_top_below_rim"] - hd["frame_height"] / 2
    band_w = (cl["outer_height"] - hd["opening_height"]) / 2 - 2
    ow, oh = cl["outer_width"] / 2, cl["outer_height"] / 2
    outer = offset_outline(rr_outline(ow, oh, cl["outer_radius"]), 0, zc)
    hole = offset_outline(rr_outline(ow - band_w, oh - band_w, cl["inner_radius"]), 0, zc)
    bm = bmesh.new()
    for sy in (-1, 1):
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
            ck = (key, colour)
            if ck not in clip_meshes:
                clip_meshes[ck] = to_mesh(f"mesh.clip.{key}.{colour}", clip_ring(bx), mats[f"clip_{colour}"])
            clip = place(f"clip.L{lv['level']}.C{c + 1}.{colour}", clip_meshes[ck], colls["boxes"], parent=obj)
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
                y += l


def build_top_plate(mats, colls):
    tp = RACK["top_plate"]
    x0 = -tp["overhang"]
    y0 = -RACK["frame"]["joint_plate"]["thickness"] - tp["overhang"]
    bm = bmesh.new()
    bm_box(bm, (m(x0), m(y0), m(tp["top"] - tp["thickness"])),
           (m(x0 + tp["width"]), m(y0 + tp["depth"]), m(tp["top"])))
    obj = finish("plate.top", bm, mats["plywood"], colls["top_plate"])
    obj["kind"] = "plate"
    obj["status"] = tp["status"]
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
    area_light(colls["stage"], "stage.key", 220, 2.0, (cx - 2.2, -2.6, 2.6), (cx, cy, cz))
    area_light(colls["stage"], "stage.fill", 60, 3.0, (cx + 2.8, -2.0, 1.4), (cx, cy, cz))
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
    # Ray tracing off: with it a second run differs in a few pixels.
    eevee = scene.eevee
    eevee.taa_render_samples = EEVEE_SAMPLES
    eevee.use_raytracing = False
    eevee.use_fast_gi = True
    eevee.fast_gi_method = "GLOBAL_ILLUMINATION"
    eevee.use_shadows = True
    eevee.shadow_ray_count = 2
    eevee.shadow_step_count = 8
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


def model_center(exclude=()):
    """Centre of the bounding box of all visible meshes outside `exclude`."""
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
    return Vector((l + h) / 2 for l, h in zip(lo, hi))


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


def main():
    global SECTION
    sec = RACK["frame"]["profile"]["section"]
    SECTION = rect_section(sec, sec)
    scene = reset_scene()
    mats = make_materials()
    names = ["frame", "angles", "castors", "boxes", "inserts", "top_plate", "stage"]
    colls = {n: collection(scene, n) for n in names}

    frame_root = bpy.data.objects.new("frame", None)
    frame_root["kind"] = "frame"
    colls["frame"].objects.link(frame_root)
    build_frame(mats, colls, frame_root)
    build_plates(mats, colls, frame_root)
    build_angles(mats, colls, frame_root)
    build_brackets(mats, colls, frame_root)
    build_castor_plates(mats, colls, frame_root)
    build_castors(mats, colls, frame_root)
    boxes = build_boxes(mats, colls)
    build_inserts(mats, colls, boxes)
    build_top_plate(mats, colls)
    colls["top_plate"].hide_render = True

    scene["rack_schema"] = RACK["schema"]
    out = RACK["outer"]
    scene["outer_mm"] = [out["width"], out["depth"], out["height"]]

    build_stage(scene, mats, colls)

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
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "rack.blend"), compress=True)

    render(scene, front, "front.png")
    render(scene, side, "side.png")
    render(scene, three, "three_quarter.png")

    box, _ = boxes[(3, 2)]
    home = box.location.copy()
    box.location.y -= m(RACK["pull_out"]["travel"])
    render(scene, drawer, "drawer_out.png")
    box.location = home

    # Top view: frame hidden, every level with inserts taken out and staged in
    # its own row, so all twelve 120 boxes and their inserts are visible.
    hidden = [colls[n] for n in ("frame", "angles", "castors")]
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


main()
