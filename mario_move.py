from pico2d import *
class Mario:
    def __init__(self):
        self.mario_x = 100
        self.mario_y = 30
        self.image = None
        self.mario_head_right = True
        self.image = animations.mario_idle_right()

    def draw(self):
        self.image.draw(self.mario_x,self.mario_y)

mario = Mario()
game_running = True









