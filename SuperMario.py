from pico2d import *
import game_world

# 이벤트 정의
RD, LD, UD, DD, SD,RU, LU, UU, DU, SU, SPACE = range(11)
event_name = ['RD', 'LD', 'UD', 'DD', 'SD', 'RU', 'LU', 'UU', 'DU', 'SU', 'SPACE']

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
}

# 상태의 정의
class IDLE:
    def enter(self, event):
        self.dir = 0
        self.need_frame = 1
        self.frame = 0

    def exit(self,event):
        pass


    def do(self):
        pass

    def draw(self):
        if self.face_dir == 1:
            if MARIO.small_mario:
                MARIO.right_image.clip_draw(2, 512, 50, 50, MARIO.draw_mario_x, MARIO.real_mario_y)
                MARIO.need_frames = 1
            else:
                MARIO.right_image.clip_draw(2, 306, 50, 70, MARIO.draw_mario_x, MARIO.real_mario_y)
                MARIO.need_frames = 1
        else:
            if MARIO.small_mario:
                MARIO.left_image.clip_draw(860, 512, 50, 50, MARIO.draw_mario_x,
                                           MARIO.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
                MARIO.need_frames = 1
            else:
                MARIO.left_image.clip_draw(860, 306, 50, 70, MARIO.draw_mario_x, MARIO.real_mario_y)
                MARIO.need_frames = 1


class WALK:
    def enter(self, event):
        self.dir = 0
        self.need_frame

    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass


class RUN:
    def enter(self, event):
        self.dir = 0
        self.need_frame

    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass


class JUMP:
    def enter(self, event):
        self.dir = 0
        self.need_frame

    def exit(self, event):
        pass

    def do(self):
        pass

    def draw(self):
        pass


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
        self.real_mario_y = 40
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

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    # def fire_ball(self):
    #     print('FIRE BALL')
    #     ball = Ball(self.x, self.y, self.face_dir*2)
    #     game_world.add_object(ball, 1)




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: WALK,  LU: WALK,  RD: WALK,  LD: WALK,  SPACE: JUMP},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: JUMP},
}