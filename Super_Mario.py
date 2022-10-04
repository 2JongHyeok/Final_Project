from pico2d import *
open_canvas()
frame = 0

mario_right_image = load_image('mario_right.png')
mario_left_image = load_image('mario_left.png')

def mario_idle_right():
    clear_canvas()
    mario_right_image.clip_draw(2,512,50,50,100,100)
    update_canvas()
    pass

def mario_walk_right():
    clear_canvas()
    mario_right_image.clip_draw(frame*70+2, 512,50,50,100,100) # frame = 1~2 번갈아 가면서 사용
    update_canvas()
    pass

def mario_idle_left():
    clear_canvas()
    mario_left_image.clip_draw(860, 512, 50, 50, 100, 100)  # frame = 1~2 번갈아 가면서 사용
    update_canvas()
    pass

def mario_walk_left():
    clear_canvas()
    mario_left_image.clip_draw(860 - frame * 70, 512, 50, 50, 100, 100)  # frame = 1~2 번갈아 가면서 사용
    update_canvas()

close_canvas()