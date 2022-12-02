from pico2d import *
import game_framework
import game_world
import play_state
import server
import select_stage

from supermario import MARIO
from tiles import Tiles

image = None
change_stage = False

stage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]


def enter():
    global image
    image = load_image('./backgroundfiles/itemshop.png')

    server.mario = MARIO()
    server.mario.in_select_stage = True
    game_world.add_object(server.mario, 1)

    for i in range(10):
        for j in range(80):
            server.tiles.append(Tiles())

    for i in range(4):
        for j in range(40):
            server.tiles[(3-i) * 40 + j].fixed_x = j * 40 + 20
            server.tiles[(3-i) * 40 + j].x = server.tiles[(3-i) * 40 + j].fixed_x
            server.tiles[(3-i) * 40 + j].y = (3-i) * 40 + 20
            server.tiles[i * 40 + j].tile = stage[(3-i) * 40 + j]
            game_world.add_object(server.tiles[i * 40 + j], 0)

    game_world.add_collision_pairs(server.mario, server.tiles, 'mario:tiles')


def exit():
    global image, change_stage
    del image
    change_stage = False
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            if server.tiles[0].see:
                for i in range(4):
                    for j in range(40):
                        server.tiles[i * 40 + j].see = False
                server.mario.see = False
            else:
                for i in range(4):
                    for j in range(40):
                        server.tiles[i * 40 + j].see = True
                server.mario.see = True
        else:
            server.mario.handle_event(event)


def draw():
    clear_canvas()
    image.draw_to_origin(0,0,1600,800)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if change_stage:
        game_framework.change_state(play_state)

    for a, b, group in game_world.all_collision_pairs():
        if 0 <= b.x <= 1600:
            if gravity_check(a, b):
                a.handle_collision(b, group)
                b.handle_collision(a, group)

    if server.mario.sit:
        if server.mario.select_pipe:
            game_framework.change_state(select_stage)

def pause():
    pass

def resume():
    pass




def gravity_check(a,b):
    if 7 < b.tile < 12 or b.tile == 0:
        return False

    global on_block
    if b.tile == 0:
        return False
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if ta < bb: return False
    if ba > tb: return False

    if la > rb: return False
    if ra < lb: return False

    if la < lb < ra or la < rb < ra or lb < la < ra < rb:
        if ba <= tb:
            return True

def side_collide(a,b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()
    if ta < bb: return False
    if ba > tb: return False
    if bb <= ta - 20 <= tb:
        if 0 < lb - ra < 2:
            return True
        elif 0 < la - rb < 2:
            return True