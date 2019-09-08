import os
import bpy
import math

# Add another cude aside from the default cube
bpy.ops.mesh.primitive_cube_add(location=(1, 1, 1))

# Add a text to the scene
bpy.ops.object.text_add(
    location=(-.5, -1.75, 1),
    rotation=(math.pi / 2, 0, math.pi / 4)
)

bpy.context.object.data.body = "Hello     hi :)"

# Make the text red
red = bpy.data.materials.new("Red")
red.diffuse_color = (1, 0, 0, 0)  # RGB?
bpy.context.object.data.materials.append(red)

# Direct the render to the repository directory
bpy.data.scenes['Scene'].render.filepath = os.getcwd() + '/render.png'

# Render the scene
bpy.ops.render.render(write_still=True)
