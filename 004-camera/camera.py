import bpy

def save(name):
  bpy.context.scene.render.image_settings.file_format='PNG'
  bpy.context.scene.render.filepath = 'out/' + name
  bpy.ops.render.render(write_still=True)

def deselectAll():
  for obj in bpy.data.objects:
    obj.select_set(False)

deselectAll()
bpy.data.objects['Camera'].select_set(True)
bpy.ops.object.delete()

print("before")
for obj in bpy.data.objects:
  print(obj.name)

bpy.ops.object.camera_add(location=(0, 0, 10))

bpy.context.scene.camera = bpy.data.objects['Camera']

print("after")
for obj in bpy.data.objects:
  print(obj.name)

save('camera')
