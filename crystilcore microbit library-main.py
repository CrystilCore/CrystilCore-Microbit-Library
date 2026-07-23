from microbit import *
import math

def world_to_grid(x, y):
    return x + 2, y + 2

def grid_to_world(x, y):
    return x - 2, y - 2

def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))

def v2distance(va, vb):
    return math.sqrt(((va[0] - vb[0]) ** 2) + ((va[1] - vb[2]) ** 2))
    
def is_near_posistion(x, y, px, py):
    px = max(min(px, 4), 0)
    py = max(min(py, 4), 0)
    px = int(px)
    py = int(py)
    x += 2
    y += 2
    if (
        (
            math.floor(x) == px
            or math.ceil(x) == px
        )
        and (
            math.floor(y) == py
            or math.ceil(y) == py
        )
    ):
        return True
    else:
        return False

def is_near_position(x, y, px, py):
    px = max(min(int(px), 4), 0)
    py = max(min(int(py), 4), 0)

    x += 2
    y += 2

    return (
        px in (math.floor(x), math.ceil(x))
        and py in (math.floor(y), math.ceil(y))
    )


def add_pixel(x, y, brightness):
    if 0 <= x <= 4 and 0 <= y <= 4:
        current = display.get_pixel(x, y)
        display.set_pixel(x, y, min(9, round(current + brightness)))


def render_dot(x, y, brightness):
    x += 2
    y += 2

    x0 = math.floor(x)
    x1 = math.ceil(x)
    y0 = math.floor(y)
    y1 = math.ceil(y)

    tx = x - x0
    ty = y - y0

    w00 = (1 - tx) * (1 - ty)
    w10 = tx * (1 - ty)
    w01 = (1 - tx) * ty
    w11 = tx * ty

    add_pixel(x0, y0, brightness * w00)
    add_pixel(x1, y0, brightness * w10)
    add_pixel(x0, y1, brightness * w01)
    add_pixel(x1, y1, brightness * w11)

# below is just a demonstration, but you can add whatever else you want

x = 0
y = 0
while True:
        if accelerometer.was_gesture('left'):
            x += -0.1
        elif accelerometer.was_gesture('right'):
            x += 0.1
        if accelerometer.was_gesture('up'):
            y += -0.1
        elif accelerometer.was_gesture('down'):
            y += 0.1
        x = max(min(x, 2), -2)
        y = max(min(y, 2), -2)
        display.clear()
        render_dot(x, y, 9)
        sleep(100)
