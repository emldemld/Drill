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
y = 90
angle = -90

while True:
    while x < 780:
        drawcanvas(x, y)
        x += 10
        delay(0.01)
    while y < 560:
        drawcanvas(x, y)
        y += 10
        delay(0.01)
    while x > 20:
        drawcanvas(x, y)
        x -= 10
        delay(0.01)
    while y > 90:
        drawcanvas(x, y)
        y -= 10
        delay(0.01)
    while x < 400:
        drawcanvas(x, y)
        x += 10
        delay(0.01)    
    x = 400
    y = 290
    while angle < 270:
        cos = math.cos(angle / 360 * 2 * math.pi) * 200
        sin = math.sin(angle / 360 * 2 * math.pi) * 200
        drawcanvas(cos + x, sin + y)
        angle+=10
        delay(0.02)
    angle = -90
    x = 400
    y = 90

    
close_canvas()
