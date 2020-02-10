import bpy

bpy.context.scene.render.image_settings.file_format='PNG'
bpy.context.scene.render.filepath = 'out/hello'
bpy.ops.render.render(write_still=True)
