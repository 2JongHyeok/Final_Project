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
        self.need_frame

    def exit(self,event):
        pass


    def do(self):
        pass

    def draw(self):
        pass


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
        self.x, self.y = 100, 40
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.right_image = load_image('mario_right.png')
        self.left_image = load_image('mario_left.png')
        self.y_gravity = 1
        self.jump_height = 15
        self.y_velocity = self.jump_height
        self.pre_y = self.real_mario_y
        self.event_que = []
        




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: WALK,  LU: WALK,  RD: WALK,  LD: WALK,  SPACE: JUMP},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: JUMP},
}