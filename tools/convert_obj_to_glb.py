"""Convert every OBJ in this repository to GLB using Blender.

Run from the repository root:
    blender --background --python tools/convert_obj_to_glb.py

Requires Blender 3.6+ with the built-in Wavefront OBJ and glTF exporters.
The script writes a sibling .glb next to each OBJ.
"""
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]
OBJ_FILES = sorted(ROOT.rglob("*.obj"))

for obj_path in OBJ_FILES:
    if "node_modules" in obj_path.parts:
        continue

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

    # Import OBJ and its sibling MTL (if present).
    try:
        bpy.ops.wm.obj_import(filepath=str(obj_path))
    except Exception:
        bpy.ops.import_scene.obj(filepath=str(obj_path))

    # Preserve imported materials; apply transforms for predictable engine import.
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
            obj.select_set(False)

    out_path = obj_path.with_suffix(".glb")
    bpy.ops.export_scene.gltf(
        filepath=str(out_path),
        export_format="GLB",
        export_apply=True,
        export_yup=True,
        export_materials="EXPORT",
    )
    print(f"Exported: {out_path}")
