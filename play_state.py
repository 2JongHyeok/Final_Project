from pico2d import *
import game_framework
import game_world

from background import BackGround
from supermario import MARIO


mario = None
background = []
ball = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            MARIO.handle_event(event)


# 초기화
def enter():
    global MARIO, BackGround
    mario = MARIO()

    background.append(BackGround())
    game_world.add_object(background,0)
    game_world.add_object(mario,1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()






# from pico2d import *
# import game_framework
# import title_state
# import random
#
# max_map_size = 3200
#
# class Tiles:
#     def __init__(self):
#         self.tile = 0 # 0 : 왼쪽풀, 1: 가운데풀, 2: 오른쪽풀
#         self.x = 0
#         self.y = 0
#         self.image = None
#         self.image_flag = 1
#
#     def update(self):
#         if self.image_flag:
#             if self.tile == 0:
#                 self.image = load_image('grass_left.png')
#             elif self.tile == 1:
#                 self.image = load_image('grass_middle.png')
#             elif self.tile == 2:
#                 self.image = load_image('grass_right.png')
#             elif self.tile == 3:
#                 self.image = load_image('pipe_left_top.png')
#             elif self.tile == 4:
#                 self.image = load_image('pipe_right_top.png')
#             self.image_flag = 0
#
#     def draw(self):
#         if self.tile >=0 and self.tile <= 2:
#             self.image.clip_draw_to_origin(0,0,16,16,self.x,self.y, 20,20)
#
#
# class Mario:
#     def __init__(self):
#         self.small_mario = True
#         self.draw_mario_x = 100
#         self.real_mario_x = 100
#         self.real_mario_y = 40
#         self.dir_x = 0
#         self.dir_y = 0
#         self.image = None
#         self.mario_head_right = True
#         self.need_frames = 1
#         self.frame = 0
#         self.mario_animation_frame = 0
#         self.mario_animation_count = 0
#         self.right = False
#         self.left = False
#         self.run_r = False
#         self.run_l = False
#         self.jump = False
#         self.fall = False
#         self.attack = False
#         self.sit = False
#         self.up = False
#         self.idle = True
#         self.user_input = 0
#         self.right_image = load_image('mario_right.png')
#         self.left_image = load_image('mario_left.png')
#         self.y_gravity = 1
#         self.jump_height = 15
#         self.y_velocity = self.jump_height
#         self.pre_y = self.real_mario_y
#         SDL_IntersectRect
#
#
#
#     def update(self):
#         self.mario_animation_frame = self.need_frames * 30
#         if self.mario_animation_count == self.mario_animation_frame:
#             self.mario_animation_count = 0
#         self.mario_animation_count += 1
#         if self.mario_animation_count % 30 == 0:
#             self.frame = (self.frame + 1) % self.need_frames
#
#         if self.right:
#             if self.run_r:
#                 self.dir_x = 2
#             else:
#                 self.dir_x = 1
#             if self.sit:
#                 self.dir_x = 0
#         elif self.left:
#             if self.run_l:
#                 self.dir_x = -2
#             else:
#                 self.dir_x = -1
#             if self.sit:
#                 self.dir_x = 0
#         elif self.idle:
#             self.dir_x = 0
#         # elif self.sit:
#         #     self.dir_x = 0
#
#
#         # if self.real_mario_x > 30 and self.real_mario_x < 800:
#         #     self.draw_mario_x += self.dir_x
#         # elif self.real_mario_x >= max_map_size - 800 and self.real_mario_x < max_map_size - 31:
#         #     self.draw_mario_x += self.dir_x
#
#
#         if self.real_mario_x + self.dir_x >= 30 and self.real_mario_x + self.dir_x <= max_map_size - 30:
#             self.real_mario_x += self.dir_x
#
#         if self.real_mario_x < 800:
#             self.draw_mario_x = self.real_mario_x
#         elif self.real_mario_x > max_map_size - 800:
#             self.draw_mario_x = 1600 - (max_map_size - self.real_mario_x)
#
#         if self.jump:
#             self.real_mario_y += self.y_velocity * 0.2
#             self.y_velocity -= self.y_gravity *0.15
#             if self.y_velocity <= 0:
#                 self.fall = True
#             if self.y_velocity < - self.jump_height:
#                 self.real_mario_y = self.pre_y
#                 self.jump = False
#                 self.fall = False
#                 self.y_velocity = self.jump_height
#                 self.idle = True
#
#     def draw(self):
#         if self.mario_head_right:
#             if self.idle:
#                 mario_idle_right()
#             elif self.right:
#                 if self.jump:
#                     if self.fall:
#                         mario_fall_right()
#                     else:
#                         mario_jump_right()
#                 elif self.sit:
#                     mario.right = False
#                 elif self.run_r:
#                     mario_run_right()
#                 else:
#                     mario_walk_right()
#             elif self.sit:
#                 mario_sit_right()
#                 if self.right:
#                     mario_sit_right()
#                 elif self.left:
#                     mario_sit_left()
#                     self.mario_head_right = False
#             elif self.jump:
#                 if self.y_velocity <= 0:
#                     if self.left:
#                         mario_fall_left()
#                     else:
#                         mario_fall_right()
#                 else:
#                     if self.left:
#                         mario_jump_left()
#                     else:
#                         mario_jump_right()
#             elif self.run_r:
#                 mario_run_right()
#
#
#         else:
#             if self.idle:
#                 mario_idle_left()
#             elif self.left:
#                 if self.jump:
#                     if self.fall:
#                         mario_fall_left()
#                     else:
#                         mario_jump_left()
#                 elif self.sit:
#                     self.left = False
#                 elif self.run_l:
#                     mario_run_left()
#                 else:
#                     mario_walk_left()
#             elif self.sit:
#                 mario_sit_left()
#                 if self.right:
#                     mario_sit_right()
#                     self.mario_head_right = True
#                 elif self.left:
#                     mario_sit_left()
#             elif self.jump:
#                 if self.y_velocity <= 0:
#                     if self.right:
#                         mario_fall_right()
#                     else:
#                         mario_fall_left()
#                 else:
#                     if self.right:
#                         mario_jump_right()
#                     else:
#                         mario_jump_left()
#             elif self.run_l:
#                 mario_run_left()
#
#
#
# class Background():
#     def __init__(self):
#         self.starmap_1 = load_image('star_map_1.png')
#         self.starmap_2 = load_image('star_map_2.png')
#         self.starmap_3 = load_image('star_map_3.png')
#         self.mansion_1 = load_image('mansion_1.png')
#         self.mansion_2 = load_image('mansion_2.png')
#         self.stage = 1
#         self.frame = 0
#         self.need_frame = 0
#         self.play_x = 0
#         self.max_map = max_map_size // 1600 # for문안에 넣어서 총 몇개의 화면을 출력할지 출력
#
#     def update(self, x):
#         if self.stage == 0:
#             self.need_frame = 0
#             self.frame = 0
#         elif self.stage == 1:
#             self.need_frame = 600
#         elif self.stage == 2:
#             self.need_frame = 400
#         self.frame = (self.frame + 1) % self.need_frame
#         if x >= 800 and x <= max_map_size - 800:
#             self.play_x = x
#
#
#     def draw(self):
#         if self.frame <= 200:
#             if self.stage == 1:
#                 self.draw_star_1()
#             elif self.stage == 2:
#                 self.draw_mansion_1()
#         elif self.frame > 200 and self.frame <= 400:
#             if self.stage == 1:
#                 self.draw_star_2()
#             elif self.stage == 2:
#                 self.draw_mansion_2()
#         elif self.frame > 400 and self.frame <= 600:
#             if self.stage == 1:
#                 self.draw_star_3()
#
#     def draw_mansion_1(self):
#         for i in range(0, self.max_map + 1):
#             self.mansion_1.draw_to_origin((1600 * i)-self.play_x, 0, 1600, 800)
#
#     def draw_mansion_2(self):
#         for i in range(0, self.max_map + 1):
#             self.mansion_2.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)
#
#     def draw_star_1(self):
#         for i in range(0, self.max_map + 1):
#             self.starmap_1.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)
#
#     def draw_star_2(self):
#         for i in range(0, self.max_map + 1):
#             self.starmap_2.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)
#
#     def draw_star_3(self):
#         for i in range(0, self.max_map + 1):
#             self.starmap_3.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)
#
#
# def pause():
#     pass
#
# def resume():
#     pass
#
# def mario_idle_right():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw(2, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#     else:
#         mario.right_image.clip_draw(2, 306, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_walk_right():
#     global mario
#     if mario.small_mario: # frame = 1~2 번갈아 가면서 사용
#         mario.right_image.clip_draw(mario.frame*70+2, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 5
#     else:
#         mario.right_image.clip_draw(mario.frame*70+2, 306, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 4
#
# def mario_idle_left():
#     global mario
#     if mario.small_mario:
#         mario.left_image.clip_draw(860, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
#         mario.need_frames = 1
#     else:
#         mario.left_image.clip_draw(860, 306, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_walk_left():
#     global mario
#     if mario.small_mario:
#         mario.left_image.clip_draw(860 - mario.frame * 70, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
#         mario.need_frames = 5
#     else:
#         mario.left_image.clip_draw(860 - mario.frame * 70, 306, 50, 70, mario.draw_mario_x, mario.real_mario_y+8)
#         mario.need_frames = 4
#
# def mario_run_right():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw(mario.frame * 70 + 352, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
#         mario.need_frames = 2
#     else:
#         if mario.frame == 0:
#             mario.right_image.clip_draw(352, 306, 49, 70, mario.draw_mario_x+2, mario.real_mario_y)
#         else:
#             mario.right_image.clip_draw(mario.frame * 70 + 352, 306, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 3
#
# def mario_run_left():
#     global mario
#     if mario.small_mario:
#         mario.left_image.clip_draw(510 - mario.frame * 70, 512, 50, 50, mario.draw_mario_x, mario.real_mario_y)  # frame = 1~2 번갈아 가면서 사용
#         mario.need_frames = 4
#     else:
#         if mario.frame == 0:
#             mario.left_image.clip_draw(505 - mario.frame * 70, 306, 52, 70, mario.draw_mario_x + 2, mario.real_mario_y)
#         else:
#             mario.left_image.clip_draw(505 - mario.frame * 70, 306, 52, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 3
#
# def mario_jump_right():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw(355, 457, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#     else:
#         mario.right_image.clip_draw(355, 206, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_jump_left():
#     global mario
#     if mario.small_mario:
#          mario.left_image.clip_draw(435, 457, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#          mario.need_frames = 1
#     else:
#         mario.left_image.clip_draw(425, 206, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_fall_right():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw(495, 457, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#     else:
#         mario.right_image.clip_draw(494, 206, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_fall_left():
#     global mario
#     if mario.small_mario:
#         mario.left_image.clip_draw(300, 457, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#     else:
#         mario.left_image.clip_draw(285, 206, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_sit_right():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw(772, 457, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#     else:
#         mario.right_image.clip_draw(772, 206, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_sit_left():
#     global mario
#     if mario.small_mario:
#         mario.left_image.clip_draw(93, 457, 40, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
#     else:
#         mario.left_image.clip_draw(73, 206, 40, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 1
#
# def mario_up():
#     global mario
#     if mario.small_mario:
#         mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 403, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 2
#     else:
#         mario.right_image.clip_draw((mario.frame + 6) * 70 + 15, 104, 50, 70, mario.draw_mario_x, mario.real_mario_y)
#         mario.need_frames = 2
#
# def mario_die():
#     global mario
#     if mario.frame == 1:
#         mario.right_image.clip_draw(632, 104, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#     else:
#         mario.right_image.clip_draw(632, 403, 50, 50, mario.draw_mario_x, mario.real_mario_y)
#     mario.need_frames = 2
#
#
# def handle_events():
#     global mario, game_running
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN:
#             mario.idle = False
#             if event.key == SDLK_RIGHT:
#                 mario.user_input = 1
#                 mario.mario_head_right = True
#                 mario.left = False
#                 mario.right = True
#                 mario.dir_x = -1
#             if event.key == SDLK_LEFT:
#                 mario.user_input = 1
#                 mario.mario_head_right = False
#                 mario.right = False
#                 mario.left = True
#                 mario.dir_x = 1
#             if event.key == SDLK_DOWN:
#                 mario.user_input = 1
#                 mario.sit = True
#                 if mario.right:
#                     mario.right = False
#                 if mario.left:
#                     mario.left = False
#             if event.key == SDLK_SPACE:
#                 mario.jump = True
#             if event.key == SDLK_LSHIFT:
#                 mario.run_r = True
#                 mario.run_l = True
#             if event.key == SDLK_i:
#                 if mario.small_mario:
#                     mario.small_mario = False
#                 else:
#                     mario.small_mario = True
#
#         if event.type == SDL_KEYUP:
#             if event.key == SDLK_RIGHT:
#                 mario.right = False
#
#             if event.key == SDLK_LEFT:
#                 mario.left = False
#
#             if event.key == SDLK_DOWN:
#                 mario.sit = False
#             if event.key == SDLK_LSHIFT:
#                 mario.run_r = False
#                 mario.run_l = False
#             if not mario.right and not mario.left and not mario.sit and not mario.jump and not mario.fall and not mario.run_r and not mario.run_l:
#                 mario.idle = True
#             mario.dir_x = 0
#
#
#
#
#
# # 사용할 전역 변수들 모음
# max_x = 3600
# max_y = 800
# rows = 200
# cols = 900
#
# # World_tiles = [[0 for j in range(cols)] for i in range(rows)]
# #
# # for i in range(rows):
# #     for j in range(cols):
# #         World_tiles[i][j] = Tiles()
#
#
#
# mario = None
# background = None
# game_running = None
# # tiles = Tiles()
# # tiles.tile = 1
# tiles = None
#
# def enter():
#     global mario, game_running, background,tiles
#     mario = Mario()
#     tiles = []
#     for n in range(0,800):
#         tiles.append(Tiles())
#         if n % 2 == 0:
#             tiles[n].tile = 0
#         else:
#             tiles[n].tile = 2
#         tiles[n].x = n * 20
#         tiles[n].update()
#     background = Background()
#     game_running = True
#
# def exit():
#     global mario, background
#     del mario
#     del background
#
# def update():
#     global mario, background,tiles
#     mario.update()
#     background.update(mario.real_mario_x)
#
# def draw_world():
#     global mario, background, tiles
#     background.draw()
#     if len(tiles) > 1:
#         for n in range(0,800):
#             tiles[n].draw()
#     mario.draw()
#
#
#
# def draw():
#     global mario
#     clear_canvas()
#     draw_world()
#     update_canvas()
#     print(mario.real_mario_y)
#
#
# def test_self():
#     import sys
#     this_module = sys.modules['__main__']
#     pico2d.open_canvas(1600,800)
#     game_framework.run(this_module)
#     pico2d.close_canvas()
#
# print(__name__)
# if __name__ == '__main__':
#     test_self()
#
