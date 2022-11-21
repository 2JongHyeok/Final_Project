from pico2d import *
import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

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

animation_name = ['Idle', 'Walk']

class Goomba:
    image = None
    see = False

    def load_images(self):
        if self.image == None:
            Goomba.image = {}
            for name in animation_name:
                Goomba.image[name] = [load_image("./goombafiles/"+ name + " (%d)" % i + ".png") for i in range(1,3)]

    def prepare_patrol_points(self):
        positions = [(80,970)]  # 좌표 획득시, 기본 위치가 왼쪽 위
        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], 1024 - p[1]))  # pico2d 상의 좌표계를 이용하도록 변경.
    def __init__(self):
        self.prepare_patrol_points()
        self.patrol_order = 1
        self.x, self.y = self.patrol_points[0]
        self.load_images()
        self.dir = random.randint(-1, 2)  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.frame = 0
        self.build_behavior_tree()
        self.HP = 100


    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 10.0
            self.dir = random.randint(-2, 2) # 방향을 라디안 값으로 설정
            print('Wander Success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.SUCCESS
        # else:
        #     return BehaviorTree.RUNNING


    def handle_collision(self, other, group):
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)

        self.bt = BehaviorTree(wander_node)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        self.bt.run()
        # print(self.dir)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * self.dir * game_framework.frame_time
        self.x = clamp(50, self.x, 3600 - 50)
        self.y = clamp(50, self.y, 800 - 50)


    def draw(self):
        if math.cos(self.dir) > 0:
            if self.speed == 0:
                Goomba.image['Walk'][1].composite_draw(0, 'h', self.x, self.y, 40,40)
            else:
                Goomba.image['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 40, 40)
        else:
            if self.speed == 0:
                Goomba.image['Walk'][1].draw(self.x, self.y, 40,40)
            else:
                Goomba.image['Walk'][int(self.frame)].draw(self.x, self.y, 40, 40)
        global see
        if self.see and self.tile > 0:
            draw_rectangle(*self.get_bb())

    def handle_event(self):
        pass


FRAMES_PER_ACTION = 2
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
PIXEL_PER_METER = 10/0.3

RUN_SPEED_KMPH = 40
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

WALK_SPEED_KMPH = 20
WALK_SPEED_MPM = WALK_SPEED_KMPH * 1000 / 60
WALK_SPEED_MPS = WALK_SPEED_MPM / 60
WALK_SPEED_PPS = WALK_SPEED_MPS * PIXEL_PER_METER
