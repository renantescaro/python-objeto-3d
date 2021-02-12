import ctypes
import os
import pyglet
from pyglet.gl import *
from pywavefront import visualization
import pywavefront
from joystick import Joystick

rotation = 0
x, y, z  = 0.0, 0.0, 0.0
path_obj = os.path.join(os.path.dirname(__file__), 'teste.obj')
meshes   = pywavefront.Wavefront(path_obj)
window   = pyglet.window.Window(resizable=True)
lightfv  = ctypes.c_float * 4
joystick = Joystick()


@window.event
def on_resize(width, height):
    viewport_width, viewport_height = window.get_framebuffer_size()
    glViewport(0, 0, viewport_width, viewport_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(110., float(width)/height, 1., 100.)
    glMatrixMode(GL_MODELVIEW)
    return True


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))
    glEnable(GL_LIGHT0)
    glTranslated(0.0, 0.0, -3.0)
    glRotatef(rotation, x, y, x)
    glEnable(GL_LIGHTING)
    visualization.draw(meshes)


def update(dt):
    global rotation, x, y, z
    acao, tipo = joystick.get_botao_pressionado()
    if acao != -1:
        # esquerda
        if acao == 2:
            rotation += 10.0
            y = 10
        # direita
        if acao == 1:
            rotation -= 10.0
            y = 10
        # cima
        if acao == 3:
            rotation += 10.0
            x = 10
        # baixo
        if acao == 0:
            rotation -= 10.0
            x = 10


pyglet.clock.schedule(update)
pyglet.app.run()