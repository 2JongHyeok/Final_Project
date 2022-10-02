from pico2d import *
open_canvas()
frame = 0

mario_image = load_image('mario.png')

def mario_idle():
    clear_canvas()
    mario_image.clip_draw(frame*60+2,3,60,90,100,100)
    update_canvas()
    pass


mario_idle()
frame =1
mario_idle()
delay(3)






close_canvas()