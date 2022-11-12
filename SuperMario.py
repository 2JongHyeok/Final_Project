from pico2d import *

import game_framework
from background import BackGround
import game_world

# 이벤트 정의
RD, LD, UD, DD, SD,RU, LU, UU, DU, SU, SPACE, K1, K2= range(13)
event_name = ['RD', 'LD', 'UD', 'DD', 'SD', 'RU', 'LU', 'UU', 'DU', 'SU', 'SPACE', 'K1', 'K2']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD, # 오른쪽 키 눌렸을 때
    (SDL_KEYDOWN, SDLK_LEFT): LD, # 왼쪽 키 눌렸을 때
    (SDL_KEYDOWN, SDLK_UP): UD, # 위쪽 키 눌렸을 때
    (SDL_KEYDOWN, SDLK_DOWN): DD, # 아래쪽 키 눌렸을 때
    (SDL_KEYDOWN, SDLK_LSHIFT): SD, # 왼쪽 쉬프트 키 눌렸을 때
    (SDL_KEYDOWN, SDLK_SPACE): SPACE, # 스페이스바 키 눌렸을 때
    (SDL_KEYUP, SDLK_RIGHT): RU, # 오른쪽 키 땠을 때
    (SDL_KEYUP, SDLK_LEFT): LU, # 왼쪽 키 땠을 때
    (SDL_KEYUP, SDLK_UP): UU, # 위쪽 키 땠을 때
    (SDL_KEYUP, SDLK_DOWN): DU, # 아래쪽 키 땠을 때
    (SDL_KEYUP, SDLK_LSHIFT): SU, # 왼쪽 쉬프트 키 땠을 때
    (SDL_KEYDOWN, SDLK_1) : K1,
    (SDL_KEYDOWN, SDLK_2) : K2,
}

# 상태의 정의
class IDLE:
    def enter(self, event):
        global need_frame
        print('ENTER IDLE')
        if self.dir == 1:
            if self.small_mario:
                need_frame = 5
            else:
                need_frame = 4
        elif self.dir == -1:
            if self.small_mario:
                need_frame = 5
            else:
                need_frame = 4
        if event == K1:
            self.small_mario = True
        elif event == K2:
            self.small_mario = False
        self.dir = 0

    def exit(self,event):
        global need_frame, see
        print('EXIT IDLE')
        if event == SPACE:
            self.JUMPING = True
        if event == SD:
            self.RUNNING = True
        if event == SU:
            self.RUNNING = False

    def do(self):
        global need_frame
        # print('DO IDLE')
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % need_frame
        if self.JUMPING:
            self.real_mario_y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity *0.15
            if self.y_velocity <= 0:
                self.FALLING = True
                self.JUMPING = False
        if self.FALLING:
            self.real_mario_y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15
            if self.y_velocity < - self.jump_height:
                self.real_mario_y = self.pre_y
                self.FALLING = False
                self.y_velocity = self.jump_height
        pass

    def draw(self):
        global need_frame
        # print('DRAW IDLE')
        if self.JUMPING:
            if self.face_dir == 1:
                if self.small_mario:
                    self.right_image.clip_draw(355, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.right_image.clip_draw(355, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
            elif self.face_dir == -1:
                if self.small_mario:
                     self.left_image.clip_draw(435, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.left_image.clip_draw(425, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
        elif self.FALLING:
            if self.face_dir == 1:
                if self.small_mario:
                    self.right_image.clip_draw(495, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.right_image.clip_draw(494, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
            elif self.face_dir == -1:
                if self.small_mario:
                    self.left_image.clip_draw(300, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.left_image.clip_draw(285, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
        else:
            if self.face_dir == 1:
                if self.small_mario:
                    self.right_image.clip_draw(10, 510, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.right_image.clip_draw(10, 306, 50, 70, self.draw_mario_x, self.real_mario_y)
            else:
                if self.small_mario:
                    self.right_image.clip_composite_draw(10, 510, 50, 50, 0,'h',self.draw_mario_x, self.real_mario_y,50,50)
                else:
                    self.right_image.clip_composite_draw(10, 306, 50, 70, 0, 'h', self.draw_mario_x, self.real_mario_y,50,70)

class WALK:
    def enter(self, event):
        global need_frame
        print('ENTER WALK')
        if event == SD:
            self.RUNNING = True
        if event == SU:
            self.RUNNING = False
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        if self.dir == 1:
            if self.small_mario:
                need_frame = 5
            else:
                need_frame = 4
        elif self.dir == -1:
            if self.small_mario:
                need_frame = 5
            else:
                need_frame = 4

    def exit(self, event):
        print('EXIT WALK')
        self.face_dir = self.dir
        if event == SPACE:
            self.JUMPING = True
        if event == SD:
            self.RUNNING = True
        if event == SU:
            self.RUNNING = False


    def do(self):
        global need_frame
        # print('DO WALK')
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % need_frame
        if self.RUNNING:
            self.real_mario_x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.real_mario_x += self.dir * WALK_SPEED_PPS * game_framework.frame_time
        self.real_mario_x = clamp(30, self.real_mario_x, 3170)
        if self.real_mario_x < 800:
            self.draw_mario_x = self.real_mario_x
        elif self.real_mario_x > 2370:
            self.draw_mario_x = self.real_mario_x - 1600
        if self.JUMPING:
            self.real_mario_y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity *0.15
            if self.y_velocity <= 0:
                self.FALLING = True
                self.JUMPING = False
        if self.FALLING:
            self.real_mario_y += self.y_velocity * 0.2
            self.y_velocity -= self.y_gravity * 0.15
            if self.y_velocity < - self.jump_height:
                self.real_mario_y = self.pre_y
                self.FALLING = False
                self.y_velocity = self.jump_height

    def draw(self):
        global need_frame
        # print('DRAW WALK')
        if self.JUMPING:
            if self.dir == 1:
                if self.small_mario:
                    self.right_image.clip_draw(355, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.right_image.clip_draw(355, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
            elif self.dir == -1:
                if self.small_mario:
                     self.left_image.clip_draw(435, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.left_image.clip_draw(425, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
        elif self.FALLING:
            if self.dir == 1:
                if self.small_mario:
                    self.right_image.clip_draw(495, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.right_image.clip_draw(494, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
            elif self.dir == -1:
                if self.small_mario:
                    self.left_image.clip_draw(300, 457, 50, 50, self.draw_mario_x, self.real_mario_y)
                else:
                    self.left_image.clip_draw(285, 206, 50, 70, self.draw_mario_x, self.real_mario_y)
        else:
            if self.RUNNING:
                if self.dir == 1:
                    if self.small_mario:
                        self.right_image.clip_draw(int(self.frame) * 70 + 352, 512, 50, 50, self.draw_mario_x, self.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
                        self.need_frames = 2
                    else:
                        if int(self.frame) == 0:
                            self.right_image.clip_draw(352, 306, 49, 70, self.draw_mario_x+2, self.real_mario_y)
                        else:
                            self.right_image.clip_draw(int(self.frame) * 70 + 352, 306, 50, 70, self.draw_mario_x, self.real_mario_y)
                        self.need_frames = 3
                elif self.dir == -1:
                    if self.small_mario:
                        self.left_image.clip_draw(510 - int(self.frame) * 70, 512, 50, 50, self.draw_mario_x, self.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
                        self.need_frames = 4
                    else:
                        if int(self.frame) == 0:
                            self.left_image.clip_draw(505 - int(self.frame) * 70, 306, 52, 70, self.draw_mario_x + 2, self.real_mario_y)
                        else:
                            self.left_image.clip_draw(505 - int(self.frame) * 70, 306, 52, 70, self.draw_mario_x, self.real_mario_y)
                        self.need_frames = 3
            else:
                if self.dir == 1:
                    if self.small_mario:  # frame = 1~2 번갈아 가면서 사용
                        self.right_image.clip_draw(int(self.frame)*70+2, 512, 50, 50, self.draw_mario_x, self.real_mario_y)
                        # need_frame = 5
                    else:
                        self.right_image.clip_draw(int(self.frame)*70+2, 306, 50, 70, self.draw_mario_x, self.real_mario_y)
                        # need_frame = 4
                elif self.dir == -1:
                    if self.small_mario:  # frame = 1~2 번갈아 가면서 사용
                        self .right_image.clip_composite_draw(int(self.frame)*70+2, 512, 50, 50, 0, 'h', self.draw_mario_x, self.real_mario_y, 50, 50)
                        # need_frame = 5
                    else:
                        self.right_image.clip_composite_draw(int(self.frame)*70+2, 306, 50, 70, 0, 'h', self.draw_mario_x, self.real_mario_y, 50, 70)
                        # need_frame = 4


class SIT:
    def enter(self, event):
        self.dir = 0
        self.need_frame

    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass


class SHOOT:
    def enter(self, event):
        self.dir = 0
        self.need_frame

    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass


class MARIO:
    def __init__(self):
        self.frame = 0
        self.draw_mario_x = 100
        self.real_mario_x = 100
        self.real_mario_y = 60
        self.dir, self.face_dir = 0, 1
        self.right_image = load_image('mario_right.png')
        self.left_image = load_image('mario_left.png')
        self.y_gravity = 1
        self.jump_height = 15
        self.y_velocity = self.jump_height
        self.pre_y = self.real_mario_y
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.small_mario = True
        self.a_count = 0
        self.JUMPING = False
        self.FALLING = False
        self.RUNNING = False
        self.see = False



    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR', {self.cur_state.__name__}, '  ', event_name[event])
            self.cur_state.enter(self, event)
        self.a_count += 1


    def draw(self):
        self.cur_state.draw(self)
        if self.see:
            draw_rectangle(*self.get_rect())
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        if self.small_mario:
            return self.real_mario_x - 15, self.real_mario_y - 25, self.real_mario_x+ 15, self.real_mario_y+ 25
        else:
            return self.real_mario_x - 10, self.real_mario_y - 20, self.real_mario_x+ 10, self.real_mario_y+ 20
    def get_rect(self):
        if self.small_mario:
            return self.draw_mario_x - 15, self.real_mario_y - 25, self.draw_mario_x+ 15, self.real_mario_y+ 25
        else:
            return self.draw_mario_x - 10, self.real_mario_y - 20, self.draw_mario_x+ 10, self.real_mario_y+ 20


    # def fire_ball(self):
    #     print('FIRE BALL')
    #     ball = Ball(self.x, self.y, self.face_dir*2)
    #     game_world.add_object(ball, 1)




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: WALK,  LU: WALK,  RD: WALK,  LD: WALK, SPACE: IDLE, SU: IDLE, SD: IDLE},
    WALK: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: WALK, SU: WALK, SD: WALK}
}

FRAMES_PER_ACTION = 8
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

need_frame = 5
move_back_grounds = 0

