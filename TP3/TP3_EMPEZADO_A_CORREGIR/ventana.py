import pyglet
from pyglet.window import key
window = pyglet.window.Window(width=400, height=400, caption="Lista de reproduccion")
label=pyglet.text.Label('fernando',x=window.width//2, y=window.height//2)
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()


window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',font_name='Times New Roman',font_size=36,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
