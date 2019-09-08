import os
import bpy

# Add another cude aside from the default cube
bpy.ops.mesh.primitive_cube_add(location=(1, 1, 1))

# Direct the render to the repository directory
bpy.data.scenes['Scene'].render.filepath = os.getcwd() + '/render.png'

# Render the scene
bpy.ops.render.render(write_still=True)
