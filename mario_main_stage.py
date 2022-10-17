from pico2d import *

play_x = 0
x = 0

open_canvas(1600,800)
class Map:
    def __init__(self):
        self.mansion_1 = load_image('mansion_1.png')
        self.mansion_2 = load_image('mansion_2.png')
        self.star_1 = load_image('star_map_1.png')
        self.star_2 = load_image('star_map_2.png')
        self.star_3 = load_image('star_map_3.png')

    def draw_mansion_1(self):
        self.mansion_1.draw_to_origin(-play_x, 0, 1600, 800)
        self.mansion_1.draw_to_origin(1600 - play_x, 0, 1600, 800)

    def draw_mansion_2(self):
        self.mansion_2.draw_to_origin(-play_x, 0, 1600, 800)
        self.mansion_2.draw_to_origin(1600-play_x, 0, 1600, 800)

    def draw_star_1(self):
        self.star_1.draw_to_origin(-play_x, 0, 1600, 800)
        self.star_1.draw_to_origin(1600 - play_x, 0, 1600, 800)

    def draw_star_2(self):
        self.star_2.draw_to_origin(-play_x, 0, 1600, 800)
        self.star_2.draw_to_origin(1600 - play_x, 0, 1600, 800)

    def draw_star_3(self):
        self.star_3.draw_to_origin(-play_x, 0, 1600, 800)
        self.star_3.draw_to_origin(1600 - play_x, 0, 1600, 800)

mansion = Map()

def draw_mansion():
    global play_x
    global x
    while True:
        clear_canvas()
        mansion.draw_mansion_1()
        delay(0.05)
        update_canvas()
        clear_canvas()
        mansion.draw_mansion_2()
        delay(0.05)
        update_canvas()
        x += 1
        if x % 3 == 0:
            play_x += 10
        if play_x > 1600:
            play_x = 0


def draw_star():
    global play_x, x
    while True:
        clear_canvas()
        mansion.draw_star_1()
        delay(0.5)
        update_canvas()
        clear_canvas()
        mansion.draw_star_2()
        delay(0.5)
        update_canvas()
        clear_canvas()
        mansion.draw_star_3()
        delay(0.5)
        update_canvas()
        clear_canvas()
        mansion.draw_star_2()
        delay(0.5)
        update_canvas()
        play_x += 1
        if play_x > 1600:
            play_x = 0

# draw_mansion()
draw_star()
close_canvas()
