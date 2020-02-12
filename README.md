# Blender Script

[**LIVE**](https://tomashubelbauer.github.io/blender-script)

![](render.png)

![](screenshot.png)

1. Add Blender to `%PATH%` and run `pip install bpy`
2. Open the repository in VS Code
3. Open `script.py` and `render.png` in split view side by side
3. Open the VS Code terminal
4. Run `npx nodemon --exec blender --background --python script.py`
5. Observe the `render.png` preview refresh after each save
6. Debug by either:
  - Removing `--background`
  - Splitting terminal and running `blender --python script.py`
  - Pressing F12 in Blender to preview render

## Stalking Blender Operations' Corresponding Python

As per https://www.youtube.com/watch?v=45WZWqmpRQE, open up the Scripting
workspace and do your work, observe the console to see the Python code for
each operation that you carry out.

## To-Do

### Figure out how to get autocompletion for `bpy`

https://github.com/TomasHubelbauer/blender-python-intellisense

### Set up a GitHub Actions workflow which installs Blender and runs the script

`blender --python script.py` on every push and push `render.png` to the repository.
