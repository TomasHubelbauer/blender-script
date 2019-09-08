import os
import bpy

# Add another cude aside from the default cube
bpy.ops.mesh.primitive_cube_add(location=(1, 1, 1))

# Add a text to the scene
bpy.ops.object.text_add(location=(0, -.75, 1.5))
bpy.context.object.data.body = "Blender"

# Direct the render to the repository directory
bpy.data.scenes['Scene'].render.filepath = os.getcwd() + '/render.png'

# Render the scene
bpy.ops.render.render(write_still=True)
