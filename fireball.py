from pico2d import *

import game_world

animation_names = ['FireBall']

class FireBall:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 1):
        if FireBall.image == None:
            FireBall.image = {}
            for name in animation_names:
                FireBall[name] = [load_image(".fireballfiles/" + name + " (%d)" % i + ".png") for i in range(1, 5)]
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x,self.y)


    def update(self):
        self.x += self.velocity
        if self.x < 20 or self.x > 780:
            game_world.remove_object(self)

