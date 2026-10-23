"""Reload blender/rack.blend in an open Blender whenever the headless build rewrites it.

Start the GUI once with it (blender-launcher opens no console window on Windows):
    blender-launcher blender/rack.blend --python blender/live_reload.py
or, in a Blender that is already open: Scripting workspace, Text > Open
blender/live_reload.py, Run Script. The reload discards unsaved changes in the
open file; rack.blend is generated, so nothing is lost that the build does not
recreate.
"""

import os

import bpy

INTERVAL = 1.0
_state = {"path": None, "sig": None, "pending": None}


def _signature(path):
    st = os.stat(path)
    return st.st_mtime_ns, st.st_size


def _tick():
    # An exception would unregister the timer for good, so none may escape.
    try:
        path = bpy.data.filepath
        if not path or not os.path.exists(path):
            return INTERVAL
        sig = _signature(path)
        if _state["path"] != path:
            _state.update(path=path, sig=sig, pending=None)
        elif sig != _state["sig"]:
            # Reload only once the file has stopped changing for one interval,
            # so a file the build is still writing is never opened.
            if _state["pending"] != sig:
                _state["pending"] = sig
                return INTERVAL
            window = bpy.context.window_manager.windows[0]
            with bpy.context.temp_override(window=window):
                bpy.ops.wm.revert_mainfile()
            _state.update(sig=sig, pending=None)
            print("live_reload: reloaded", os.path.basename(path))
    except Exception as exc:
        print("live_reload: reload failed, retrying:", exc)
    return INTERVAL


if not bpy.app.timers.is_registered(_tick):
    bpy.app.timers.register(_tick, first_interval=INTERVAL, persistent=True)
    print("live_reload: watching", os.path.basename(bpy.data.filepath))
