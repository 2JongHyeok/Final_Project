from pico2d import *
import game_framework
import game_world
import play_state
import server
import select_stage
import tiles

from supermario import MARIO
from tiles import Tiles

image = None
change_stage = False
font = None

stage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]


def enter():
    global image, font
    image = load_image('./backgroundfiles/itemshop.png')

    server.mario = MARIO()
    server.mario.in_shop = True
    server.mario.in_select_stage = True
    game_world.add_object(server.mario, 1)

    for i in range(10):
        for j in range(80):
            server.tiles.append(Tiles())

    for i in range(6):
        for j in range(40):
            server.tiles[(5-i) * 40 + j].fixed_x = j * 40 + 20
            server.tiles[(5-i) * 40 + j].x = server.tiles[(5-i) * 40 + j].fixed_x
            server.tiles[(5-i) * 40 + j].y = (5-i) * 40 + 20
            server.tiles[i * 40 + j].tile = stage[(5-i) * 40 + j]
            game_world.add_object(server.tiles[i * 40 + j], 0)

    game_world.add_collision_pairs(server.mario, server.tiles, 'mario:tiles')
    font = load_font('ENCR10B.TTF', 40)

def exit():
    global image, change_stage, font
    del image, font
    change_stage = False
    server.mario.in_shop = False
    server.goomba = []
    server.mario = []
    server.bowser = None
    server.tiles = []
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
                for i in range(6):
                    for j in range(40):
                        server.tiles[i * 40 + j].see = False
                server.mario.see = False
            else:
                for i in range(6):
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
    if server.Hp_Need_Money > server.Mario_Coin:
        font.draw(500, 350, '(Need Money : %d)' % server.Hp_Need_Money, (255, 0, 0))
    else:
        font.draw(500, 350, '(Need Money : %d)' % server.Hp_Need_Money, (255, 255, 0))
    font.draw(600, 300, 'HP UP', (255, 255, 0))
    font.draw(620, 270, '+ 10', (255, 255, 0))
    if server.Att_Need_Money > server.Mario_Coin:
        font.draw(900, 350, '(Need Money : %d)' % server.Att_Need_Money, (255, 0, 0))
    else:
        font.draw(900, 350, '(Need Money : %d)' % server.Att_Need_Money, (255, 255, 0))
    font.draw(990, 300, 'ATT UP', (255, 255, 0))
    font.draw(1030, 270, '+ 5', (255, 255, 0))
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

def head_collide(a,b):
    if 23 <= b.tile <= 32:
        pass
    else:
        return False
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if ta < bb: return False
    if ba > tb: return False
    if lb < ra - 15 < rb:
        if -2 <= bb - ta <= 0:
            server.mario.head_collision = True
            if tiles.hp_start <= b.tile <= tiles.hp_start + 3:
                server.Max_Hp += 5
                server.Mario_Hp = server.Max_Hp
                server.Mario_Coin -= server.Hp_Need_Money
                server.Hp_Need_Money += 5
            elif tiles.att_start <= b.tile <= tiles.att_start +3:
                server.Mario_Att += 5
                server.Mario_Coin -= server.Att_Need_Money
                server.Att_Need_Money += 7
            return True