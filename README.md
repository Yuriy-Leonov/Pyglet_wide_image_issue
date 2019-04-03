$ python main.py

```
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    texture_grid_8193x1px = image_grid_8193x1px.get_texture_sequence()
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 2308, in get_texture_sequence
    self._texture_grid = TextureGrid(self)
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 2379, in __init__
    image = grid.get_texture()
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 2301, in get_texture
    return self.image.get_texture(rectangle, force_rectangle)
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 859, in get_texture
    force_rectangle)
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 844, in create_texture
    rectangle, force_rectangle)
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/image/__init__.py", line 1564, in create
    blank)
  File "/path/to/venv/lib/python3.6/site-packages/pyglet/gl/lib.py", line 105, in errcheck
    raise GLException(msg)
pyglet.gl.lib.GLException: b'invalid value'
```