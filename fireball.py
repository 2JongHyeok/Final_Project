from pico2d import *

import game_world
import game_framework
import server

animation_names = ['FireBall']

class FireBall:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 2):
        if FireBall.image == None:
            FireBall.image = {}
            for name in animation_names:
                FireBall.image[name] = [load_image("./fireballfiles/" + name + " (%d)" % i + ".png") for i in range(1, 5)]
        self.fixed_x, self.y, self.velocity = x, y, velocity
        self.x = self.fixed_x
        if velocity < 0:
            self.velocity = -2
        else:
            self.velocity = 2

        self.BOUNCING = False
        self.y_gravity = 1
        self.jump_height = 5
        self.y_velocity = self.jump_height
        self.frame = 0
        server.fireball.append(self)


    def draw(self):
        FireBall.image['FireBall'][int(self.frame)].draw(self.x, self.y, 10, 10)


    def update(self):
        if 800 <= server.mario.real_mario_x <= 2400:
            self.x = self.fixed_x - server.mario.real_mario_x + 800
        else:
            self.x = self.fixed_x
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.fixed_x += self.velocity
        if self.BOUNCING:
            self.y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15
            if self.y_velocity <= 0:
                self.BOUNCING = False
        else:
            self.y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15


        for block in server.tiles:
            if 0 < block.tile < 8 or 12 < block.tile:
                if 0 <= block.x <= 3200:
                    if side_collide(self, block):
                        for i in game_world.all_objects():
                            if i == self:
                                game_world.remove_object(self)

        for block in server.tiles:
            if 0 <= block.x <= 3200:
                if gravity_check(self, block):
                    self.y_velocity = self.jump_height
                    self.real_mario_y = block.y + 42
                    self.BOUNCING = True



        if self.x < 25 or self.x > 3200 - 25:
            game_world.remove_object(self)



    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5



def gravity_check(a,b):
    if 7 < b.tile < 12 or b.tile == 0:
        return False

    global on_block
    if b.tile == 0:
        return False
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if ta < bb: return False
    if ba > tb: return False

    if la > rb: return False
    if ra < lb: return False

    if la < lb < ra or la < rb < ra or lb < la < ra < rb:
        if ba <= tb:
            return True
    # return True

def side_collide(a,b):
    if b.tile == 0:
        return False
    if b == None:
        return False
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if ta < bb: return False
    if ba > tb: return False
    if bb <= ta - 20 <= tb:
        if 0 < lb - ra < 2:
            return True
        elif 0 < la - rb < 2:
            return True

FRAMES_PER_ACTION = 4
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
PIXEL_PER_METER = 10/0.3
