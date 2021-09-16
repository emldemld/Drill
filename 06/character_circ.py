from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def drawcanvas(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

x = 400
y = 300
angle = 270

while True:
    cos = math.cos(angle / 360 * 2 * math.pi) * 200
    sin = math.sin(angle / 360 * 2 * math.pi) * 200
    drawcanvas(cos + x, sin + y)
    angle+=10
    delay(0.02)


close_canvas()
