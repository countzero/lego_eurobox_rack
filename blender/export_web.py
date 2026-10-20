"""Export blender/rack.blend to web/rack.glb for the web viewer.

Run headless on the saved model; the .blend is never saved:
    blender --background blender/rack.blend --python-exit-code 1 --python blender/export_web.py
"""

import os

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "web", "rack.glb")

EXPORT_COLLECTIONS = ("frame", "angles", "castors", "panels", "boxes", "inserts", "top_plate")


def main():
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
    )
    print("wrote", OUT)


main()
