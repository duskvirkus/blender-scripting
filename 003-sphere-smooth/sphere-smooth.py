import bpy

def save(name):
  bpy.context.scene.render.image_settings.file_format='PNG'
  bpy.context.scene.render.filepath = 'out/' + name
  bpy.ops.render.render(write_still=True)

for obj in bpy.data.objects:
  print(obj.name)

bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(radius=1.5)

for obj in bpy.data.objects:
  print(obj.name)

bpy.data.objects['Sphere'].select_set(True)
bpy.ops.object.shade_smooth()

save('sphere-smooth')
