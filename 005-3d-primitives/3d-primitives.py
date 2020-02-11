import bpy
import math

def save(name):
  bpy.context.scene.render.image_settings.file_format='PNG'
  bpy.context.scene.render.filepath = 'out/' + name
  bpy.ops.render.render(write_still=True)

def deselectAll():
  for obj in bpy.data.objects:
    obj.select_set(False)

def printObjects():
  for obj in bpy.data.objects:
    print(obj.name)

deselectAll()
bpy.data.objects['Camera'].select_set(True)
bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()

spacing = 3

bpy.ops.mesh.primitive_cube_add(size=2, location=(-spacing * 2, spacing, 0))
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, spacing, 0))
bpy.ops.mesh.primitive_ico_sphere_add(location=(spacing * 2, spacing, 0))
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=(-spacing * 2, -spacing, 0))
bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, location=(0, -spacing, 0))
bpy.ops.mesh.primitive_torus_add(location=(spacing * 2, -spacing, 0), major_radius=1, minor_radius=0.25)

bpy.ops.object.camera_add(location=(0, -15, 30), rotation=(math.pi / 7, 0, 0))
bpy.context.scene.camera = bpy.data.objects['Camera']

save('primitives')

deselectAll();
printObjects();
bpy.data.objects['Cone'].select_set(True)
bpy.data.objects['Cube'].select_set(True)
bpy.data.objects['Cylinder'].select_set(True)
bpy.data.objects['Icosphere'].select_set(True)
bpy.data.objects['Sphere'].select_set(True)
bpy.data.objects['Torus'].select_set(True)
bpy.ops.object.shade_smooth()

save('primitives-smooth')
