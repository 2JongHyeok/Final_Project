from pico2d import *
import game_framework
import random
from background import BackGround
import game_world

# 이벤트 정의
RD, LD, UD, DD, SD, RU, LU, UU, DU, SU, SPACE, K1, K2 = range(13)
event_name = ['RD', 'LD', 'UD', 'DD', 'SD', 'RU', 'LU', 'UU', 'DU', 'SU', 'SPACE', 'K1', 'K2']
animation_names = ['Idle', 'Walk', 'Run', 'Die', 'Sit', 'Jump', 'Fall']
sm_w = 30 # 작은 마리오 가로
sm_h = 40 # 작은 마리오 세로
bm_w = 30 # 큰 마리오 가로
bm_h = 50 # 큰 마리오 세로

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
        # print('EXIT IDLE')
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


    def draw(self):
        global need_frame
        if self.JUMPING:
            if self.face_dir == 1:
                if self.small_mario:
                    MARIO.small_image['Jump'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Jump'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            elif self.face_dir == -1:
                if self.small_mario:
                    MARIO.small_image['Jump'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Jump'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
        elif self.FALLING:
            if self.face_dir == 1:
                if self.small_mario:
                    MARIO.small_image['Fall'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Fall'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            elif self.face_dir == -1:
                if self.small_mario:
                    MARIO.small_image['Fall'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Fall'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
        else:
            if self.face_dir == 1:
                if self.small_mario:
                    MARIO.small_image['Idle'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Idle'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            else:
                if self.small_mario:
                    MARIO.small_image['Idle'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Idle'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)

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
        if self.JUMPING:
            if self.dir == 1:
                if self.small_mario:
                    MARIO.small_image['Jump'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Jump'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            elif self.dir == -1:
                if self.small_mario:
                    MARIO.small_image['Jump'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Jump'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
        elif self.FALLING:
            if self.dir == 1:
                if self.small_mario:
                    MARIO.small_image['Fall'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Fall'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            elif self.dir == -1:
                if self.small_mario:
                    MARIO.small_image['Fall'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                else:
                    MARIO.big_image['Fall'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
        else:
            if self.RUNNING:
                if self.dir == 1:
                    if self.small_mario:
                        MARIO.small_image['Run'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                    else:
                        MARIO.big_image['Run'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
                elif self.dir == -1:
                    if self.small_mario:
                        MARIO.small_image['Run'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                    else:
                        MARIO.big_image['Run'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
            else:
                if self.dir == 1:
                    if self.small_mario:  # frame = 1~2 번갈아 가면서 사용
                        MARIO.small_image['Walk'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                    else:
                        MARIO.big_image['Walk'][int(self.frame)].draw(self.draw_mario_x, self.real_mario_y, bm_w, bm_h)
                elif self.dir == -1:
                    if self.small_mario:  # frame = 1~2 번갈아 가면서 사용
                        MARIO.small_image['Walk'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, sm_w, sm_h)
                    else:
                        MARIO.big_image['Walk'][int(self.frame)].composite_draw(0, 'h', self.draw_mario_x, self.real_mario_y, bm_w, bm_h)



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
    small_image = None
    big_image = None

    def load_images(self):
        if MARIO.small_image == None:
            MARIO.small_image = {}
            MARIO.big_image = {}
            for name in animation_names:
                MARIO.small_image[name] = [load_image("./mariofiles/smallmario/" + name + " (%d)" % i + ".png") for i in range(1, 5)]
                MARIO.big_image[name] = [load_image("./mariofiles/bigmario/" + name + " (%d)" % i + ".png") for i in range(1, 5)]

    def __init__(self):
        self.frame = 0
        self.load_images()
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
        self.RUNNING = False
        self.see = False
        self.FALLING = True
        self.floor = False



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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.FALLING:
            self.y_velocity = 0
            self.y_velocity -= self.y_gravity * 0.15
            self.real_mario_y += self.y_velocity * 0.2
            if self.floor:
                self.y_velocity = self.jump_height
                self.FALLING = False




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
            return self.draw_mario_x - 15, self.real_mario_y - 20, self.draw_mario_x+ 15, self.real_mario_y+ 20
        else:
            return self.draw_mario_x - 15, self.real_mario_y - 25, self.draw_mario_x+ 15, self.real_mario_y+ 25
    def get_rect(self):
        if self.small_mario:
            return self.draw_mario_x - 15, self.real_mario_y - 20, self.draw_mario_x+ 15, self.real_mario_y+ 20
        else:
            return self.draw_mario_x - 15, self.real_mario_y - 25, self.draw_mario_x+ 15, self.real_mario_y+ 25
    def handle_collision(self, other, group):
        self.floor = True


    # def fire_ball(self):
    #     print('FIRE BALL')
    #     ball = Ball(self.x, self.y, self.face_dir*2)
    #     game_world.add_object(ball, 1)




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: WALK,  LU: WALK,  RD: WALK,  LD: WALK, SPACE: IDLE, SU: IDLE, SD: IDLE},
    WALK: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: WALK, SU: WALK, SD: WALK}
}

FRAMES_PER_ACTION = 4
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

