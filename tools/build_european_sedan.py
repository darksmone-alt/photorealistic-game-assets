"""Build a more detailed, generic European sedan and export a game-ready GLB.

Run from repository root:
    blender --background --python tools/build_european_sedan.py

Creates:
    vehicles/european_sedan_01_detailed.glb

Coordinate system: Blender Z-up internally; vehicle forward is +X.
Wheel objects have their origins at the hubs, so they can rotate/steer independently.
No real-world manufacturer, logo, or trademark is used.
"""
from pathlib import Path
import math
import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "vehicles" / "european_sedan_01_detailed.glb"

# Reset scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

def material(name, color, metallic=0.0, roughness=0.35):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    bs = mat.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value = (*color, 1.0)
    bs.inputs["Metallic"].default_value = metallic
    bs.inputs["Roughness"].default_value = roughness
    return mat

PAINT = material("Paint | metallic blue", (0.025, 0.12, 0.32), 0.78, 0.23)
GLASS = material("Glass | dark tinted", (0.012, 0.035, 0.052), 0.28, 0.12)
RUBBER = material("Rubber", (0.012, 0.014, 0.018), 0.0, 0.82)
ALLOY = material("Alloy", (0.42, 0.46, 0.50), 0.86, 0.22)
TRIM = material("Black trim", (0.018, 0.021, 0.025), 0.18, 0.32)
CHROME = material("Bright metal", (0.62, 0.67, 0.72), 0.92, 0.18)
LED = material("LED headlamps", (0.82, 0.91, 1.0), 0.25, 0.16)
RED = material("Tail lamps", (0.62, 0.012, 0.018), 0.22, 0.2)

def finish(obj, name, mat, bevel=0.0):
    obj.name = name
    if mat:
        obj.data.materials.append(mat)
    if bevel and obj.type == "MESH":
        mod = obj.modifiers.new("Soft manufactured edges", "BEVEL")
        mod.width = bevel
        mod.segments = 2
        obj.modifiers.new("Weighted corner normals", "WEIGHTED_NORMAL")
    return obj

def cube(name, loc, scale, mat, bevel=0.04):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish(obj, name, mat, bevel)

def mesh_obj(name, verts, faces, mat, bevel=0.0):
    mesh = bpy.data.meshes.new(name + "Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.materials.append(mat)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    if bevel:
        mod = obj.modifiers.new("Edge highlights", "BEVEL")
        mod.width = bevel
        mod.segments = 2
        obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    return obj

def beam(name, a, b, radius, mat):
    mid = (Vector(a) + Vector(b)) * 0.5
    vec = Vector(b) - Vector(a)
    bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=radius, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = vec.to_track_quat("Z", "Y")
    return finish(obj, name, mat, radius * 0.25)

def uv_sphere(name, loc, scale, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=12, location=loc)
    obj = bpy.context.object
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish(obj, name, mat)

# Main lower body: shaped cross sections give a tapered nose and shoulders.
stations = [
    (0.05, 0.73, 0.53), (0.25, 0.86, 0.64), (0.75, 0.91, 0.69),
    (1.45, 0.90, 0.70), (2.30, 0.90, 0.70), (3.35, 0.89, 0.68),
    (4.05, 0.84, 0.62), (4.48, 0.75, 0.52)
]
verts = []
for x, halfw, top in stations:
    verts.extend([(x, 0.48, -halfw), (x, top, -halfw*0.96),
                  (x, top, halfw*0.96), (x, 0.48, halfw)])
faces = []
for i in range(len(stations)-1):
    for j in range(4):
        a=i*4+j; b=i*4+(j+1)%4
        c=(i+1)*4+(j+1)%4; d=(i+1)*4+j
        faces.append((a,b,c,d))
faces.extend([(3,2,1,0), tuple(range((len(stations)-1)*4, len(stations)*4))])
mesh_obj("Body | sculpted lower shell", verts, faces, PAINT, 0.025)

# Hood and trunk surface panels.
cube("Hood | sculpted panel", (0.77, 0.91, 0), (1.12, 0.10, 1.36), PAINT, 0.075)
cube("Trunk | sculpted panel", (3.93, 0.91, 0), (0.82, 0.10, 1.22), PAINT, 0.065)
cube("Front bumper | painted", (0.08, 0.52, 0), (0.16, 0.25, 1.52), PAINT, 0.07)
cube("Rear bumper | painted", (4.46, 0.53, 0), (0.16, 0.24, 1.48), PAINT, 0.07)
cube("Front lower grille", (0.0, 0.54, 0), (0.025, 0.14, 0.72), TRIM, 0.025)
cube("Grille upper chrome bar", (0.015, 0.67, 0), (0.035, 0.025, 0.62), CHROME, 0.01)
for z in [-0.22,-0.11,0,0.11,0.22]:
    cube("Grille vertical slat", (0.02,0.59,z), (0.025,0.12,0.012), CHROME, 0.004)

# Cabin shell with windshield, rear screen and side glazing.
cab_verts = [
    (1.22,1.00,-0.64),(3.45,1.00,-0.64),(3.12,1.82,-0.53),(1.72,1.82,-0.53),
    (1.22,1.00,0.64),(3.45,1.00,0.64),(3.12,1.82,0.53),(1.72,1.82,0.53)
]
cab_faces = [(0,1,2,3),(4,7,6,5),(0,3,7,4),(1,5,6,2),(3,2,6,7)]
mesh_obj("Cabin | painted pillars and roof", cab_verts, cab_faces, PAINT, 0.018)
# Windshield and rear windscreen as separate dark glazing panels.
mesh_obj("Windshield", [(1.34,1.08,-.625),(1.34,1.08,.625),(1.78,1.75,.51),(1.78,1.75,-.51)], [(0,1,2,3)], GLASS)
mesh_obj("Rear windscreen", [(3.34,1.08,-.61),(3.34,1.08,.61),(3.08,1.74,.50),(3.08,1.74,-.50)], [(0,1,2,3)], GLASS)
for side in [-1,1]:
    z = side * 0.645
    mesh_obj("Front side window", [(1.48,1.10,z),(2.28,1.10,z),(2.28,1.68,side*.56),(1.80,1.68,side*.56)], [(0,1,2,3)], GLASS)
    mesh_obj("Rear side window", [(2.38,1.10,z),(3.22,1.10,z),(3.02,1.68,side*.56),(2.38,1.68,side*.56)], [(0,1,2,3)], GLASS)
    beam("B-pillar", (2.31,1.08,side*.655),(2.31,1.72,side*.56),.035,TRIM)
    beam("A-pillar", (1.23,1.00,side*.65),(1.73,1.80,side*.54),.035,PAINT)
    beam("C-pillar", (3.43,1.00,side*.65),(3.10,1.80,side*.54),.04,PAINT)

# Door seams, handles, rocker trim and mirrors.
for side in [-1,1]:
    z = side*0.895
    for x in [1.32,2.32,3.38]:
        beam("Door panel seam", (x,.57,z),(x,.99,z),.006,TRIM)
    for x in [1.78,2.86]:
        cube("Door handle", (x,1.015,side*.905), (.22,.035,.025), CHROME, .012)
    cube("Rocker panel trim", (2.35,.49,side*.88),(1.72,.09,.045),TRIM,.018)
    beam("Mirror stalk", (1.34,1.10,side*.72),(1.34,1.20,side*.93),.025,TRIM)
    uv_sphere("Side mirror housing",(1.34,1.23,side*.96),(.16,.10,.13),PAINT)

# Wheel arches as dark arch liners and painted flares, plus four wheels with true hub origins.
def torus_wheel(name, x, y, z, major, minor, mat):
    bpy.ops.mesh.primitive_torus_add(major_segments=32, minor_segments=12, location=(x,y,z),
                                    major_radius=major, minor_radius=minor)
    obj=bpy.context.object
    obj.rotation_euler[0]=math.pi/2
    return finish(obj,name,mat)

for x, axle in [(0.92,"F"),(3.55,"R")]:
    for side in [-1,1]:
        z=side*.83
        # fender lip curved segments
        for k in range(13):
            ang=math.radians(18 + k*(144/12))
            px=x+.47*math.cos(ang); py=.48+.47*math.sin(ang)
            uv_sphere("Wheel arch lip",(px,py,z),(.045,.045,.055),PAINT)
        # Wheel object origin precisely at hub.
        bpy.ops.mesh.primitive_torus_add(major_segments=32,minor_segments=12,location=(x,.43,z),major_radius=.305,minor_radius=.105)
        tire=bpy.context.object
        tire.rotation_euler[0]=math.pi/2
        finish(tire, f"wheel_{'F' if axle=='F' else 'R'}_{'L' if side<0 else 'R'}_tire", RUBBER)
        bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=.255, depth=.16, location=(x,.43,z))
        rim=bpy.context.object; rim.rotation_euler[0]=math.pi/2
        finish(rim, f"wheel_{'F' if axle=='F' else 'R'}_{'L' if side<0 else 'R'}_rim", ALLOY, .012)
        # Five-spoke alloy wheel.
        for spoke in range(5):
            a=2*math.pi*spoke/5
            p1=(x+.06*math.cos(a),.43+.06*math.sin(a),z+side*.09)
            p2=(x+.235*math.cos(a+.12),.43+.235*math.sin(a+.12),z+side*.09)
            beam("Alloy spoke",p1,p2,.025,CHROME)
        bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=.07,depth=.19,location=(x,.43,z))
        cap=bpy.context.object; cap.rotation_euler[0]=math.pi/2
        finish(cap,"Alloy centre cap",CHROME,.008)
        # Combine wheel pieces into a single wheel assembly and set origin at hub.
        wheel_parts=[o for o in bpy.context.scene.objects if o.name.startswith((
            f"wheel_{'F' if axle=='F' else 'R'}_{'L' if side<0 else 'R'}_"))]
        # Keep all wheel components as children of a hub-empty, preserving independent control.
        hub=bpy.data.objects.new(f"wheel_{'FL' if axle=='F' and side<0 else 'FR' if axle=='F' else 'RL' if side<0 else 'RR'}",None)
        bpy.context.collection.objects.link(hub)
        hub.location=(x,.43,z)
        for part in wheel_parts:
            part.parent=hub
            part.matrix_parent_inverse=hub.matrix_world.inverted()
        # Set all components to use a common origin by parenting to the hub.

# Lighting clusters, mirrors, parking sensors, exhaust tips.
for side in [-1,1]:
    z=side*.54
    cube("LED headlamp",(.12,.83,z),(.06,.19,.34),LED,.035)
    cube("Rear tail lamp",(4.39,.83,z),(.055,.20,.30),RED,.025)
    cube("Parking sensor",(4.55,.52,side*.38),(.025,.035,.035),TRIM,.012)
    beam("Exhaust tip",(4.48,.36,side*.48),(4.60,.36,side*.48),.035,CHROME)

# Front/rear badges deliberately plain and unbranded.
cube("Front emblem blank",(.105,.76,0),(.025,.055,.075),CHROME,.012)
cube("Rear emblem blank",(4.38,.77,0),(.025,.045,.06),CHROME,.01)

# Set origin for body geometry already at world origin; create export selection.
bpy.ops.object.select_all(action="SELECT")
bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
# GLB uses Y-up by default from glTF exporter. Preserve object transforms and hierarchy.
bpy.ops.export_scene.gltf(filepath=str(OUT), export_format="GLB",
                           export_apply=False, export_materials="EXPORT",
                           export_yup=True)
print(f"Exported detailed sedan: {OUT}")
