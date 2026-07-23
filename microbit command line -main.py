# Imports go at the top
from microbit import *
import math

def matrix_to_leds(matrix):
    for y in range(0, 5):
        for x in range(0, 5):
            display.set_pixel(x, y, matrix[y][x])

def enter_command_line():
    is_quicka = False
    is_quicka_reverse = False
    command = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    render = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    target_pixel = 0
    target_x = 0
    target_y = 0
    target_pixel_polarity = 0
    time_buttona_ignore = 0
    time_buttona_reverse_ignore = 0
    time_buttonb_ignore = 0
    while not pin_logo.is_touched():
        if button_a.is_pressed() and time_buttona_ignore <= 0:
            target_pixel += 1
            if target_pixel > 24:
                    target_pixel = 0
            if is_quicka:
                time_buttona_ignore = 250
            else:
                time_buttona_ignore = 750
        if time_buttona_ignore > 0:
            if button_a.is_pressed():
                time_buttona_ignore -= 1
                if button_a.is_pressed() and time_buttona_ignore <= 0:
                    is_quicka = True
            else:
                time_buttona_ignore = 0
                is_quicka = False
        if button_a.is_pressed() and time_buttona_ignore > 0 and time_buttona_reverse_ignore <= 0:
            target_pixel -= 1
            if target_pixel < 0:
                target_pixel = 24
            time_buttona_ignore = 750
            time_buttona_reverse_ignore = 750
        target_x = int(target_pixel % 5)
        target_y = int((target_pixel - (target_pixel % 5)) / 5)
        target_pixel_polarity = command[target_y][target_x]
        if target_pixel_polarity == 1:
            target_pixel_polarity = 1
        else:
            target_pixel_polarity = 0
        if button_b.is_pressed() and time_buttonb_ignore <= 0:
            if target_pixel_polarity == 1:
                command[target_y][target_x] = 0
            else:
                command[target_y][target_x] = 1
            time_buttonb_ignore = 1000
        if time_buttonb_ignore > 0:
            if button_b.is_pressed():
                time_buttonb_ignore -= 1
            else:
                time_buttonb_ignore = 0
        if time_buttona_reverse_ignore > 0:
            if button_a.is_pressed():
                time_buttona_reverse_ignore -= 1
            else:
                time_buttona_reverse_ignore = 0
        for y in range(0, 5):
            for x in range(0,5):
                if command[y][x] == 1:
                    if target_x == x and target_y == y:
                        render[y][x] = 9
                    else:
                        render[y][x] = 6
                else:
                    if target_x == x and target_y == y:
                        render[y][x] = 3
                    else:
                        render[y][x] = 0
        matrix_to_leds(render)
        sleep(1)

while True:
    enter_command_line()
    sleep(5000)