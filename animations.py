from pico2d import *
open_canvas()

class Mario:
    def __init__(self):
        self.small_mario = True
        self.mario_x = 100
        self.mario_y = 30
        self.dir_x = 0
        self.dir_y = 0
        self.image = None
        self.mario_head_right = True
        self.need_frames = 1
        self.frame = 0
        self.user_input = 0
        self.right_image = load_image('mario_right.png')
        self.left_image = load_image('mario_left.png')

    def update(self):
        self.frame = (self.frame + 1) % self.need_frames
        self.mario_x += self.dir_x * 1
        self.mario_y += self.dir_y * 1

    def draw(self):
        if self.mario_head_right:
            if self.user_input == 0:
                mario_idle_right()
            elif self.user_input == 1:
                mario_walk_right()
            elif self.user_input == 2:
                mario_run_right()
            elif self.user_input == 3:
                mario_sit_right()
            elif self.user_input == 4:
                mario_jump_right()
        else:
            if self.user_input == 0:
                mario_idle_left()
            elif self.user_input == 1:
                mario_walk_left()
            elif self.user_input == 2:
                mario_run_left()
            elif self.user_input == 3:
                mario_sit_left()
            elif self.user_input == 4:
                mario_jump_left()


def mario_idle_right():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.right_image.clip_draw(2, 512, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(2, 306, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_walk_right():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.right_image.clip_draw(mario.frame*70+2, 512, 50, 50, mario.mario_x, mario.mario_y) # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 5
    else:
        mario.right_image.clip_draw(mario.frame*70+2, 306, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 4
    update_canvas()

def mario_idle_left():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.left_image.clip_draw(860, 512, 50, 50, mario.mario_x, mario.mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 1
    else:
        mario.left_image.clip_draw(860, 306, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_walk_left():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.left_image.clip_draw(860 - mario.frame * 70, 512, 50, 50, mario.mario_x, mario.mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 5
    else:
        mario.left_image.clip_draw(860 - mario.frame * 70, 306, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 4
    update_canvas()

def mario_run_right():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.right_image.clip_draw(mario.frame * 70 + 352, 512, 50, 50, mario.mario_x, mario.mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 4
    else:
        if mario.frame == 0:
            mario.right_image.clip_draw(352, 306, 49, 70, mario.mario_x+2, mario.mario_y)
        else:
            mario.right_image.clip_draw(mario.frame * 70 + 352, 306, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 3
    update_canvas()

def mario_run_left():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.left_image.clip_draw(493 - mario.frame * 70, 512, 50, 50, mario.mario_x, mario.mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 4
    else:
        if mario.frame == 0:
            mario.left_image.clip_draw(497 - mario.frame * 70, 306, 52, 70, mario.mario_x + 2, mario.mario_y)
        else:
            mario.left_image.clip_draw(493 - mario.frame * 70, 306, 52, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 3
    update_canvas()
def mario_jump_right():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.right_image.clip_draw(355, 457, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(355, 206, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_jump_left():
    clear_canvas()
    global mario
    if mario.small_mario:
         mario.left_image.clip_draw(425, 457, 50, 50, mario.mario_x, mario.mario_y)
         mario.need_frames = 1
    else:
        mario.left_image.clip_draw(425, 206, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_fall_right():
    clear_canvas()
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(495, 206, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(494, 206, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_fall_left():
    clear_canvas()
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(285, 457, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    else:
        mario.left_image.clip_draw(285, 206, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_sit_right():
    clear_canvas()
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(772, 457, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(772, 206, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_sit_left():
    global mario
    clear_canvas()
    if mario.small_mario:
        mario.left_image.clip_draw(73, 457, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1

    else:
        mario.left_image.clip_draw(73, 206, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 1
    update_canvas()

def mario_up():
    clear_canvas()
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 403, 50, 50, mario.mario_x, mario.mario_y)
        mario.need_frames = 2
    else:
        mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 104, 50, 70, mario.mario_x, mario.mario_y)
        mario.need_frames = 2

def mario_die():
    clear_canvas()
    global mario
    if mario.frame == 1:
        mario.right_image.clip_draw(632, 104, 50, 50, mario.mario_x, mario.mario_y)
    else:
        mario.right_image.clip_draw(632, 403, 50, 50, mario.mario_x, mario.mario_y)
    mario.need_frames = 2


def handle_events():
    global mario, game_running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN and event.key == SDLK_LEFT:
                mario.mario_head_right = False
                mario.user_input = 3
            elif event.key == SDLK_DOWN and event.key == SDLK_RIGHT:
                mario.mario_head_right = True
                mario.user_input = 3

            elif event.key == SDLK_RIGHT:
                mario.mario_head_right = True
                mario.user_input = 1
                mario.dir_x = 1
            elif event.key == SDLK_LEFT:
                mario.mario_head_right = False
                mario.user_input = 1
                mario.dir_x = -1
            elif event.key == SDLK_DOWN:
                mario.user_input = 3
                if event.key == SDLK_RIGHT:
                    mario.mario_head_right = True
                elif event.key == SDLK_LEFT:
                    mario.mario_head_right = False
            elif event.key == SDLK_SPACE:
                for i in range(10):
                    if i < 5:
                        mario.user_input = 4
                        mario.mario_y += 1
                        if event.key == SDLK_RIGHT:
                            mario.mario_x += 1
                            mario.mario_head_right = True
                        elif event.key == SDLK_LEFT:
                            mario.mario_x -= 1
                            mario.mario_head_right = False
                    else:
                        mario.user_input = 4
                        mario.mario_y -= 1
                        if event.key == SDLK_RIGHT:
                            mario.mario_x += 1
                            mario.mario_head_right = True
                        elif event.key == SDLK_LEFT:
                            mario.mario_x -= 1
                            mario.mario_head_right = False

        if event.type == SDL_KEYUP:
            mario.user_input = 0
            mario.dir_x = 0


def enter():
    global mario



open_canvas()

# 사용할 전역 변수들 모음
mario = Mario()
game_running = True



while game_running:
    handle_events()

    mario.update()
    clear_canvas()

    mario.draw()
    update_canvas()


close_canvas()
