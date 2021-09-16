from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def drawcanvas(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

x = 400
y = 90

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


close_canvas()
