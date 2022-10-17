from pico2d import *
import game_framework
import title_state
import random

class Mario:
    def __init__(self):
        self.small_mario = True
        self.draw_mario_x = 100
        self.draw_mario_y = 30
        self.real_mario_x = 100
        self.real_mario_y = 30
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
        if self.real_mario_x > 31 and self.real_mario_x < 800:
            self.draw_mario_x += self.dir_x * 0.5
        elif self.real_mario_x >= 2400 and self.real_mario_x < 3170:
            self.draw_mario_x += self.dir_x * 0.5

        if self.real_mario_x + self.dir_x * 0.5 >= 30 and self.real_mario_x + self.dir_x * 0.5 <= 3170:
            self.real_mario_x += self.dir_x * 0.5
        self.draw_mario_y += self.dir_y * 0.5


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


class Background():
    def __init__(self):
        self.starmap_1 = load_image('star_map_1.png')
        self.starmap_2 = load_image('star_map_2.png')
        self.starmap_3 = load_image('star_map_3.png')
        self.mansion_1 = load_image('mansion_1.png')
        self.mansion_2 = load_image('mansion_2.png')
        self.stage = 1
        self.frame = 0
        self.need_frame = 0
        self.play_x = 0

    def update(self, x):
        if self.stage == 0:
            self.need_frame = 0
            self.frame = 0
        elif self.stage == 1:
            self.need_frame = 600
        elif self.stage == 2:
            self.need_frame = 400
        self.frame = (self.frame + 1) % self.need_frame
        self.play_x = x

    def draw(self):
        if self.frame <= 200:
            if self.stage == 1:
                self.draw_star_1()
            elif self.stage == 2:
                self.draw_mansion_1()
        elif self.frame > 200 and self.frame <= 400:
            if self.stage == 1:
                self.draw_star_2()
            elif self.stage == 2:
                self.draw_mansion_2()
        elif self.frame > 400 and self.frame <= 600:
            if self.stage == 1:
                self.draw_star_3()

    def draw_mansion_1(self):
        for i in range(0, 11):
            self.mansion_1.draw_to_origin((1600 * i)-self.play_x, 0, 1600, 800)

    def draw_mansion_2(self):
        self.mansion_2.draw_to_origin(- self.play_x, 0, 1600, 800)
        self.mansion_2.draw_to_origin(1600 - self.play_x, 0, 1600, 800)

    def draw_star_1(self):
        for i in range(0, 11):
            self.starmap_1.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)

    def draw_star_2(self):
        for i in range(0, 11):
            self.starmap_2.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)

    def draw_star_3(self):
        for i in range(0, 11):
            self.starmap_3.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)


def pause():
    pass

def resume():
    pass

def mario_idle_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(2, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(2, 306, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_walk_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(mario.frame*70+2, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y) # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 5
    else:
        mario.right_image.clip_draw(mario.frame*70+2, 306, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 4

def mario_idle_left():
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(860, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 1
    else:
        mario.left_image.clip_draw(860, 306, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_walk_left():
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(860 - mario.frame * 70, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 5
    else:
        mario.left_image.clip_draw(860 - mario.frame * 70, 306, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 4

def mario_run_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(mario.frame * 70 + 352, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 4
    else:
        if mario.frame == 0:
            mario.right_image.clip_draw(352, 306, 49, 70, mario.draw_mario_x+2, mario.draw_mario_y)
        else:
            mario.right_image.clip_draw(mario.frame * 70 + 352, 306, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 3

def mario_run_left():
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(493 - mario.frame * 70, 512, 50, 50, mario.draw_mario_x, mario.draw_mario_y)  # frame = 1~2 번갈아 가면서 사용
        mario.need_frames = 4
    else:
        if mario.frame == 0:
            mario.left_image.clip_draw(497 - mario.frame * 70, 306, 52, 70, mario.draw_mario_x + 2, mario.draw_mario_y)
        else:
            mario.left_image.clip_draw(493 - mario.frame * 70, 306, 52, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 3

def mario_jump_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(355, 457, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(355, 206, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_jump_left():
    global mario
    if mario.small_mario:
         mario.left_image.clip_draw(425, 457, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
         mario.need_frames = 1
    else:
        mario.left_image.clip_draw(425, 206, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_fall_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(495, 206, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(494, 206, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_fall_left():
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(285, 457, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1
    else:
        mario.left_image.clip_draw(285, 206, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_sit_right():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw(772, 457, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1
    else:
        mario.right_image.clip_draw(772, 206, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_sit_left():
    global mario
    if mario.small_mario:
        mario.left_image.clip_draw(73, 457, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

    else:
        mario.left_image.clip_draw(73, 206, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 1

def mario_up():
    global mario
    if mario.small_mario:
        mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 403, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 2
    else:
        mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 104, 50, 70, mario.draw_mario_x, mario.draw_mario_y)
        mario.need_frames = 2

def mario_die():
    global mario
    if mario.frame == 1:
        mario.right_image.clip_draw(632, 104, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
    else:
        mario.right_image.clip_draw(632, 403, 50, 50, mario.draw_mario_x, mario.draw_mario_y)
    mario.need_frames = 2


def handle_events():
    global mario, game_running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
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




# 사용할 전역 변수들 모음
mario = None
background = None
game_running = None

def enter():
    global mario, game_running, background
    mario = Mario()
    background = Background()
    game_running = True

def exit():
    global mario, background
    del mario
    del background

def update():
    global mario, background
    mario.update()
    background.update(mario.real_mario_x)

def draw_world():
    global mario, background
    background.draw()
    mario.draw()


def draw():
    global mario
    clear_canvas()
    draw_world()
    print(mario.real_mario_x)
    update_canvas()


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(1600,800)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()