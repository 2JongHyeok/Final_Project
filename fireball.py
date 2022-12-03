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
        self.BOUNCING = False
        self.y_gravity = 1
        self.jump_height = 5
        self.y_velocity = self.jump_height
        game_world.add_object(self, 1)


    def draw(self):
        self.image.draw(self.x,self.y)


    def update(self):
        self.x += self.velocity * 1.5
        if self.BOUNCING:
            self.y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15
            if self.y_velocity <= 0:
                self.BOUNCING = False
        else:
            self.y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15








        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
        if side_collide():
            game_world.remove_object(self)

