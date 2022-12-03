from pico2d import *
import random
import math
import game_framework
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import server

import server

max_map_size = 3200



PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_name = ['Walk']

class Bowser:
    image = None
    see = False
    hp_bar = None

    def load_images(self):
        if self.image == None:
            Bowser.image = {}
            for name in animation_name:
                Bowser.image[name] = [load_image("./bowserfiles/"+ name + " (%d)" % i + ".png") for i in range(1,18)]
                Bowser.hp_bar = load_image("./bowserfiles/Hp_Bar.png")


    def __init__(self):
        # self.fixed_x = random.randint(100, 2800)

        self.fixed_x = 1000
        self.y = 300
        self.x = self.fixed_x
        self.load_images()
        self.dir = -1
        self.speed = 100
        self.frame = 0
        self.HP = 1000
        self.FALLING = True
        self.y_gravity = 1
        self.y_velocity = 0
        self.first = True


    def handle_collision(self, other, group):
        pass


    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def update(self):
        if self.HP > 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
            self.fixed_x += self.dir * WALK_SPEED_PPS * game_framework.frame_time
            if 800 < server.mario.real_mario_x < 2800:
                self.x = self.fixed_x - server.mario.real_mario_x + 800
            else:
                self.x = self.fixed_x
            for i in server.tiles:
                if side_collide(self, i):
                    self.dir = -self.dir
            if self.fixed_x + self.dir < 100 or self.fixed_x + self.dir > 3500:
                self.dir = -self.dir
            if self.FALLING:
                self.y += self.y_velocity * 0.2
                self.y_velocity -= self.y_gravity * 0.15

            self.FALLING = False
            for i in server.tiles:
                if gravity_check(self, i):
                    self.Falling = False
                    self.y_velocity = 0
                    self.y = i.y + 120
            else:
                self.FALLING = True
            for fire in server.fireball:
                if fire_ball_collision(self, fire):
                    for i in game_world.all_objects():
                        if i == fire:
                            game_world.remove_object(fire)
                    self.HP -= server.Mario_Att
                    server.fireball.remove(fire)
        else:
            if self.first:
                server.clear = True
                server.Mario_Coin += 10000
                self.first = False




    def draw(self):
        if self.HP > 0:
            if self.dir == -1:
                Bowser.image['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 200, 200)
            else:
                Bowser.image['Walk'][int(self.frame)].draw(self.x, self.y, 200, 200)
            Bowser.hp_bar.draw(self.x, self.y + 130, self.HP, 30)
            global see
            if self.see and self.tile > 0:
                draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass


FRAMES_PER_ACTION = 2
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
PIXEL_PER_METER = 10/0.3

WALK_SPEED_KMPH = 5
WALK_SPEED_MPM = WALK_SPEED_KMPH * 1000 / 60
WALK_SPEED_MPS = WALK_SPEED_MPM / 60
WALK_SPEED_PPS = WALK_SPEED_MPS * PIXEL_PER_METER

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


def gravity_check(a,b):
    if 7 < b.tile < 12 or b.tile == 0:
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

def fire_ball_collision(a,b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if ta < bb: return False
    if ba > tb: return False
    if la > rb: return False
    if ra < lb: return False
    return True

