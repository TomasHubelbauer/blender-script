# Blender Script

![](render.png)

1. Add Blender to `%PATH%`
2. Open the repository in VS Code
3. Open `script.py` and `render.png` in split view side by side
3. Open the VS Code terminal
4. Run `npx nodemon --exec blender --background --python script.py`
5. Observe the `render.png` preview refresh after each save
6. Debug by either:
  - Removing `--background`
  - Splitting terminal and running `blender --python script.py`
  - Pressing F12 in Blender to preview render
