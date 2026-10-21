"""Reload blender/rack.blend in an open Blender whenever the headless build rewrites it.

Start the GUI once with it:
    blender blender/rack.blend --python blender/live_reload.py
or, in a Blender that is already open: Scripting workspace, Text > Open
blender/live_reload.py, Run Script. The reload discards unsaved changes in the
open file; rack.blend is generated, so nothing is lost that the build does not
recreate.
"""

import os

import bpy

INTERVAL = 1.0
_state = {"path": None, "mtime": None}


def _tick():
    path = bpy.data.filepath
    if not path or not os.path.exists(path):
        return INTERVAL
    mtime = os.path.getmtime(path)
    if _state["path"] != path:
        _state.update(path=path, mtime=mtime)
    elif mtime != _state["mtime"]:
        _state["mtime"] = mtime
        window = bpy.context.window_manager.windows[0]
        with bpy.context.temp_override(window=window):
            bpy.ops.wm.revert_mainfile()
        print("live_reload: reloaded", path)
    return INTERVAL


if not bpy.app.timers.is_registered(_tick):
    bpy.app.timers.register(_tick, first_interval=INTERVAL, persistent=True)
    print("live_reload: watching", bpy.data.filepath)
