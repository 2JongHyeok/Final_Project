from pico2d import *
import game_framework
import select_stage
import server

image = None

def enter():
    global image
    if server.clear:
        image = load_image('./backgroundfiles/clear.png')
    else:
        image = load_image('./backgroundfiles/title.png')

def exit():
    global image
    del image

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            if server.Mario_Hp > 0:
                game_framework.change_state(select_stage)
            else:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if server.cleartime == 5:
                game_framework.quit()
            if server.Mario_Hp > 0:
                game_framework.change_state(select_stage)
            elif server.clear:
                game_framework.quit()
            else:
                game_framework.quit()
def draw():
    clear_canvas()
    image.draw_to_origin(0,0,1600,800)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






