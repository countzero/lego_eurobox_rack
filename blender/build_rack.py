"""Build the LEGO Eurobox rack from design/rack.json, save rack.blend, render.

Run headless from the repository root:
    blender --background --factory-startup --python-exit-code 1 --python blender/build_rack.py

Every structural dimension comes from design/rack.json (millimetres); the
model is in metres. Only visual details (slot depth, castor shape, colours,
cameras, lights) are set here.
"""

import json
import math
import os

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
BOX_TAPER = 10.0  # mm the foot is narrower than the rim on each side
INSERT_WALL = 1.5
STAGE_GAP = 50.0  # mm between the two box rows in the inserts top view
COLOURS = {
    "aluminium": ((0.70, 0.72, 0.75, 1), 0.6, 0.3),
    "panel_white": ((0.92, 0.92, 0.92, 1), 0.0, 0.5),
    "box_grey": ((0.15, 0.17, 0.19, 1), 0.0, 0.55),
    "insert_grey": ((0.45, 0.47, 0.50, 1), 0.0, 0.55),
    "castor": ((0.06, 0.06, 0.07, 1), 0.0, 0.6),
    "plywood": ((0.80, 0.64, 0.44, 1), 0.0, 0.6),
    "floor": ((0.35, 0.35, 0.35, 1), 0.0, 0.9),
}


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


def make_materials():
    mats = {}
    for name, (colour, metal, rough) in COLOURS.items():
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        bsdf.inputs["Base Color"].default_value = colour
        bsdf.inputs["Metallic"].default_value = metal
        bsdf.inputs["Roughness"].default_value = rough
        mat.diffuse_color = colour
        mats[name] = mat
    return mats


def collection(scene, name):
    coll = bpy.data.collections.new(name)
    scene.collection.children.link(coll)
    return coll


def finish(name, bm, mat, coll, parent=None, location=(0, 0, 0)):
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    mesh.materials.append(mat)
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    coll.objects.link(obj)
    if parent is not None:
        obj.parent = parent
    return obj


def bm_box(bm, lo, hi):
    lo, hi = Vector(lo), Vector(hi)
    size = hi - lo
    mat = Matrix.Translation((lo + hi) / 2) @ Matrix.Diagonal((*size, 1))
    bmesh.ops.create_cube(bm, size=1.0, matrix=mat)


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


def profile_section():
    w, d = SLOT_WIDTH / 2, SLOT_DEPTH
    s = RACK["frame"]["profile"]["section"] / 2
    pts = [(-s, -s), (-w, -s), (-w, -s + d), (w, -s + d), (w, -s),
           (s, -s), (s, -w), (s - d, -w), (s - d, w), (s, w),
           (s, s), (w, s), (w, s - d), (-w, s - d), (-w, s),
           (-s, s), (-s, w), (-s + d, w), (-s + d, -w), (-s, -w)]
    return [(m(a), m(b)) for a, b in pts]


SECTION = None


def profile(name, axis, centre_a, centre_b, start, end, mat, coll, parent):
    """30x30 slotted profile along axis from start to end (mm)."""
    bm = bmesh.new()
    rings = []
    for t in (m(start), m(end)):
        ring = []
        for a, b in SECTION:
            a, b = a + m(centre_a), b + m(centre_b)
            p = {"x": (t, a, b), "y": (a, t, b), "z": (a, b, t)}[axis]
            ring.append(bm.verts.new(p))
        rings.append(ring)
    n = len(SECTION)
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
    ux, uy = fr["upright_x"], fr["upright_y"]
    up = fr["upright"]
    for i, x in enumerate(ux):
        for y, side in zip(uy, ("front", "back")):
            profile(f"upright.{i + 1}.{side}", "z", x + h, y + h, up["bottom"], up["top"],
                    mats["aluminium"], colls["frame"], frame_root)
    levels = {"bottom": fr["bottom_frame"], "top": fr["top_frame"]}
    for lvl, zz in levels.items():
        zc = (zz["bottom"] + zz["top"]) / 2
        for c in range(fr["columns"]):
            for y, side in zip(uy, ("front", "back")):
                profile(f"beam.width.{lvl}.{side}.C{c + 1}", "x", y + h, zc,
                        ux[c] + sec, ux[c + 1], mats["aluminium"], colls["frame"], frame_root)
        for i, x in enumerate(ux):
            profile(f"beam.depth.{lvl}.{i + 1}", "y", x + h, zc, uy[0] + sec, uy[1],
                    mats["aluminium"], colls["frame"], frame_root)


def angle(name, x_face, inward, z_flat_lo, flat_up, mats, coll, parent):
    """L angle along y. x_face: upright face, inward: +1 or -1.

    flat_up=True: flat leg on top at z_flat_lo..+t, hanging leg down.
    flat_up=False: flat leg at the bottom, vertical leg up.
    """
    a = RACK["angles"]
    leg, t, length = a["section"]["leg"], a["section"]["thickness"], a["length"]
    x0, x1 = sorted((x_face, x_face + inward * leg))
    xl0, xl1 = sorted((x_face, x_face + inward * t))
    zf0, zf1 = z_flat_lo, z_flat_lo + t
    zl0, zl1 = (zf1 - leg, zf1) if flat_up else (zf0, zf0 + leg)
    bm = bmesh.new()
    bm_box(bm, (m(x0), 0, m(zf0)), (m(x1), m(length), m(zf1)))
    bm_box(bm, (m(xl0), 0, m(zl0)), (m(xl1), m(length), m(zl1)))
    bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=1e-6)
    return finish(name, bm, mats["aluminium"], coll, parent)


def build_angles(mats, colls, frame_root):
    fr, a = RACK["frame"], RACK["angles"]
    sec, t = fr["profile"]["section"], a["section"]["thickness"]
    ux = fr["upright_x"]
    for c in range(fr["columns"]):
        faces = ((ux[c] + sec, +1, "left"), (ux[c + 1], -1, "right"))
        for lv in RACK["levels"]:
            kind = lv["angle"]
            for x_face, inward, side in faces:
                if kind == "angle.base":
                    angle(f"angle.base.L{lv['level']}.C{c + 1}.{side}", x_face, inward,
                          a["base"]["flat_leg_top"] - t, False, mats, colls["angles"], frame_root)
                else:
                    angle(f"angle.support.L{lv['level']}.C{c + 1}.{side}", x_face, inward,
                          lv["floor"] - t, True, mats, colls["angles"], frame_root)
        for x_face, inward, side in faces:
            angle(f"angle.guard.C{c + 1}.{side}", x_face, inward,
                  RACK["tip_guard"]["flat_leg_bottom"], True, mats, colls["angles"], frame_root)


def build_castors(mats, colls, frame_root):
    fr = RACK["frame"]
    h = fr["castor_height"]
    half = fr["profile"]["section"] / 2
    wheel_r = 0.375 * h
    for i, x in enumerate(fr["upright_x"]):
        for y, kind in zip(fr["upright_y"], ("brake", "plain")):
            cx, cy = m(x + half), m(y + half)
            bm = bmesh.new()
            bm_box(bm, (-m(0.3 * h), -m(0.3 * h), m(0.95 * h)), (m(0.3 * h), m(0.3 * h), m(h)))
            bm_cylinder(bm, (0, 0, m(0.9 * h)), m(0.2 * h), m(0.1 * h), "z")
            ox = m(0.12 * h)
            for sx in (-1, 1):
                bm_box(bm, (sx * ox - m(0.02 * h), -m(0.15 * h), m(wheel_r)),
                       (sx * ox + m(0.02 * h), m(0.15 * h), m(0.85 * h)))
            bm_box(bm, (-ox, -m(0.15 * h), m(0.82 * h)), (ox, m(0.15 * h), m(0.85 * h)))
            bm_cylinder(bm, (0, -m(0.06 * h), m(wheel_r)), m(wheel_r), m(0.18 * h), "x")
            if kind == "brake":
                bm_box(bm, (-m(0.06 * h), -m(0.32 * h), m(0.6 * h)),
                       (m(0.06 * h), -m(0.15 * h), m(0.65 * h)))
            obj = finish(f"castor.{kind}.{i + 1}", bm, mats["castor"], colls["castors"], frame_root)
            obj.location = (cx, cy, 0)


def build_panels(mats, colls):
    p, fr = RACK["panels"], RACK["frame"]
    t = p["thickness"]
    z0 = fr["upright"]["bottom"]
    out = []
    bm = bmesh.new()
    bm_box(bm, (0, m(p["back"]["y"]), m(z0)),
           (m(p["back"]["width"]), m(p["back"]["y"] + t), m(z0 + p["back"]["height"])))
    out.append(finish("panel.back", bm, mats["panel_white"], colls["panels"]))
    for name, x0 in (("panel.side.left", -t), ("panel.side.right", fr["width"])):
        bm = bmesh.new()
        bm_box(bm, (m(x0), 0, m(z0)),
               (m(x0 + t), m(p["side"]["depth"]), m(z0 + p["side"]["height"])))
        out.append(finish(name, bm, mats["panel_white"], colls["panels"]))
    for obj in out:
        obj["kind"] = "panel"


def build_boxes(mats, colls):
    fr = RACK["frame"]
    sec = fr["profile"]["section"]
    ux = fr["upright_x"]
    front_y = RACK["box_position"]["front_y"]
    boxes = {}
    for lv in RACK["levels"]:
        key = RACK["model_boxes"][lv["class"]]
        bx = RACK["box_models"][key]
        for c in range(fr["columns"]):
            name = f"box.L{lv['level']}.C{c + 1}"
            floor_z = bx["height"] - bx["inner_height"]
            bm = hollow_tray(
                m(bx["width"]), m(bx["length"]),
                m(bx["width"] - 2 * BOX_TAPER), m(bx["length"] - 2 * BOX_TAPER),
                m(bx["height"]),
                m(bx["inner_width"]), m(bx["inner_length"]),
                m(bx["inner_width"] - 2 * BOX_TAPER), m(bx["inner_length"] - 2 * BOX_TAPER),
                m(floor_z))
            # origin at the front bottom centre of the box
            bmesh.ops.translate(bm, verts=bm.verts[:], vec=(0, m(bx["length"] / 2), 0))
            xc = (ux[c] + sec + ux[c + 1]) / 2
            obj = finish(name, bm, mats["box_grey"], colls["boxes"],
                         location=(m(xc), m(front_y), m(lv["floor"])))
            obj["kind"] = "box"
            obj["level"] = lv["level"]
            obj["column"] = c + 1
            obj["class"] = lv["class"]
            obj["model"] = key
            obj["travel"] = m(RACK["pull_out"]["travel"])
            obj["pull_axis"] = [0, 0, 1]
            boxes[(lv["level"], c + 1)] = (obj, bx)
    return boxes


def build_inserts(mats, colls, boxes):
    ins = RACK["inserts"]
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
                bm = hollow_tray(m(w), m(l), m(w), m(l), m(h),
                                 m(w - 2 * INSERT_WALL), m(l - 2 * INSERT_WALL),
                                 m(w - 2 * INSERT_WALL), m(l - 2 * INSERT_WALL), m(INSERT_WALL))
                loc = (m(x_start + r * row_w + w / 2), m(y + l / 2), m(floor_z))
                obj = finish(f"insert.{key}.R{r + 1}.{k + 1}.{t}", bm, mats["insert_grey"],
                             colls["inserts"], parent=box, location=loc)
                obj["kind"] = "insert"
                obj["type"] = t
                y += l


def build_top_plate(mats, colls):
    tp, out = RACK["top_plate"], RACK["outer"]
    t = RACK["panels"]["thickness"]
    x0 = -t - tp["overhang"]
    y0 = -tp["overhang"]
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


def build_stage(scene, mats, colls):
    bm = bmesh.new()
    bm_box(bm, (-20, -20, -0.01), (20, 20, 0))
    finish("stage.floor", bm, mats["floor"], colls["stage"])
    sun = bpy.data.lights.new("stage.sun", "SUN")
    sun.energy = 3.0
    sun.angle = math.radians(8)
    sun_obj = bpy.data.objects.new("stage.sun", sun)
    sun_obj.rotation_euler = (math.radians(50), 0, math.radians(-35))
    colls["stage"].objects.link(sun_obj)
    world = bpy.data.worlds.new("stage.world")
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.30, 0.32, 0.35, 1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0
    scene.world = world

    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1200
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.render.use_stamp = False
    scene.render.use_stamp_date = False
    scene.eevee.taa_render_samples = 64
    try:
        scene.view_settings.view_transform = "Standard"
    except TypeError:
        pass


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


def render(scene, cam, filename):
    scene.camera = cam
    scene.render.filepath = os.path.join(RENDERS, filename)
    bpy.ops.render.render(write_still=True)
    print("rendered", filename)


def main():
    global SECTION
    SECTION = profile_section()
    scene = reset_scene()
    mats = make_materials()
    names = ["frame", "angles", "castors", "panels", "boxes", "inserts", "top_plate", "stage"]
    colls = {n: collection(scene, n) for n in names}

    frame_root = bpy.data.objects.new("frame", None)
    frame_root["kind"] = "frame"
    colls["frame"].objects.link(frame_root)
    build_frame(mats, colls, frame_root)
    build_angles(mats, colls, frame_root)
    build_castors(mats, colls, frame_root)
    build_panels(mats, colls)
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
    front = camera(scene, cams, "cam.front", (cx, -10, cz), (cx, 0, cz), ortho_scale=W * 1.12)
    side = camera(scene, cams, "cam.side", (-10, cy, cz), (0, cy, cz), ortho_scale=H * 1.2 * 4 / 3)
    three = camera(scene, cams, "cam.three_quarter", (cx - 1.6, -2.3, 1.45), (cx, cy, cz * 0.85), lens=42)
    drawer = camera(scene, cams, "cam.drawer_out", (cx - 1.5, -2.3, 1.45), (cx, cy - 0.2, cz * 0.9), lens=40)
    top = camera(scene, cams, "cam.inserts_top", (cx, 0, 10), (cx, 0, 0), ortho_scale=W * 1.4)

    os.makedirs(RENDERS, exist_ok=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "rack.blend"), compress=True)

    render(scene, front, "front.png")
    render(scene, side, "side.png")
    render(scene, three, "three_quarter.png")

    box, _ = boxes[(3, 2)]
    home = box.location.copy()
    box.location.y -= m(RACK["pull_out"]["travel"])
    render(scene, drawer, "drawer_out.png")
    box.location = home

    # Top view: frame and panels hidden, the level 3 boxes taken out in front of level 4.
    hidden = [colls[n] for n in ("frame", "angles", "castors", "panels")]
    for coll in hidden:
        coll.hide_render = True
    lower = [boxes[(3, c)][0] for c in (1, 2, 3)]
    upper = [boxes[(4, c)][0] for c in (1, 2, 3)]
    others = [boxes[(l, c)][0] for l in (1, 2) for c in (1, 2, 3)]
    for b in others:
        b.hide_render = True
    length = m(RACK["box_models"][RACK["model_boxes"]["120"]]["length"])
    for b in lower:
        b.location.y -= length + m(STAGE_GAP)
    y_mid = (lower[0].location.y + upper[0].location.y + length) / 2
    top.location.y = y_mid
    look_at(top, (cx, y_mid, 0))
    render(scene, top, "inserts_top.png")
    for b in lower:
        b.location.y += length + m(STAGE_GAP)
    for b in others:
        b.hide_render = False
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
