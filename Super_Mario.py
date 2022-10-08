from pico2d import *
open_canvas()
frame = 0

mario_right_image = load_image('mario_right.png')
mario_left_image = load_image('mario_left.png')

# 사용할 지역 변수들 모음
small_mario = False # 초기 마리오는 작은 마리오, 만약 체력 LEVEL 이 10이 넘어가면 큰 마리오로 바뀜
mario_x = 100
mario_y = 100
need_frames = 0


def mario_idle_right():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_right_image.clip_draw(2, 512, 50, 50, mario_x, mario_y)
        need_frames = 1
    else:
        mario_right_image.clip_draw(2, 306, 50, 70, mario_x, mario_y)
        need_frames = 1
    update_canvas()

def mario_walk_right():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_right_image.clip_draw(frame*70+2, 512, 50, 50, mario_x, mario_y) # frame = 1~2 번갈아 가면서 사용
        need_frames = 5
    else:
        mario_right_image.clip_draw(frame*70+2, 306, 50, 70, mario_x, mario_y)
        need_frames = 4
    update_canvas()

def mario_idle_left():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_left_image.clip_draw(860, 512, 50, 50, mario_x, mario_y)  # frame = 1~2 번갈아 가면서 사용
        need_frames = 1
    else:
        mario_left_image.clip_draw(860, 306, 50, 70, mario_x, mario_y)
        need_frames = 1
    update_canvas()

def mario_walk_left():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_left_image.clip_draw(860 - frame * 70, 512, 50, 50, mario_x, mario_y)  # frame = 1~2 번갈아 가면서 사용
        need_frames = 5
    else:
        mario_left_image.clip_draw(860 - frame * 70, 306, 50, 70, mario_x, mario_y)
        need_frames = 4
    update_canvas()

def mario_run_right():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_right_image.clip_draw(frame * 70 + 352, 512, 50, 50, mario_x, mario_y)  # frame = 1~2 번갈아 가면서 사용
        need_frames = 4
    else:
        if frame == 0:
            mario_right_image.clip_draw(352, 306, 49, 70, mario_x+2, mario_y)
        else:
            mario_right_image.clip_draw(frame * 70 + 352, 306, 50, 70, mario_x, mario_y)
        need_frames = 3
    update_canvas()

def mario_run_left():
    global need_frames
    clear_canvas()
    if small_mario:
        mario_left_image.clip_draw(493 - frame * 70, 512, 50, 50, mario_x, mario_y)  # frame = 1~2 번갈아 가면서 사용
        need_frames = 4
    else:
        if frame == 0:
            mario_left_image.clip_draw(497 - frame * 70, 306, 52, 70, mario_x + 2, mario_y)
        else:
            mario_left_image.clip_draw(493 - frame * 70, 306, 52, 70, mario_x, mario_y)
        need_frames = 3
    update_canvas()
def mario_jump_right():
    global need_frames
    if small_mario:
        pass
    else:
        pass

def mario_jump_left():
    global need_frames
    if small_mario:
        pass
    else:
        pass

def mario_sit_right():
    global need_frames
    if small_mario:
        pass
    else:
        pass

def mario_sit_left():
    global need_frames
    if small_mario:
        pass
    else:
        pass

def mario_up():
    if small_mario:
        global need_frames
        pass
    else:
        pass

def mario_die():
    global need_frames
    if small_mario:
        pass
    else:
        pass

def main():
    global need_frames
    global frame
    i = 0
    while i < 100:
        mario_run_left()
        delay(0.1)
        frame = i % need_frames
        i += 1
    close_canvas()


main()