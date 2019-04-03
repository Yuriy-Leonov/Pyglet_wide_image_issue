import pyglet

GOOD_FILE = "8192x1px.png"
BAD_FILE = "8193x1px.png"

image_8192x1px = pyglet.image.load(GOOD_FILE)
image_grid_8192x1px = pyglet.image.ImageGrid(image=image_8192x1px, rows=1, columns=1)
texture_grid_8192x1px = image_grid_8192x1px.get_texture_sequence()

image_8193x1px = pyglet.image.load(BAD_FILE)
image_grid_8193x1px = pyglet.image.ImageGrid(image=image_8193x1px, rows=1, columns=1)
texture_grid_8193x1px = image_grid_8193x1px.get_texture_sequence()
