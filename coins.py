from pico2d import *
import game_world

max_map_size = 3200



class Tiles:
    Grass_Left = None
    Grass_Middle = None
    Grass_Right = None
    Pipe_Left_Top = None
    Pipe_Right_Top = None
    Pipe_Left_middle = None
    Pipe_Right_middle = None
    coin_1 = None
    coin_2 = None
    coin_3 = None
    coin_4 = None


    see = False

    def __init__(self):
        self.tile = 0 # 0 : 왼쪽풀, 1: 가운데풀, 2: 오른쪽풀
        self.x = 0
        self.y = 0
        self.timer = 100
        if self.Grass_Left == None:
            Tiles.Grass_Left = load_image('grass_left.png')
            Tiles.Grass_Middle = load_image('grass_middle.png')
            Tiles.Grass_Right = load_image('grass_right.png')
            Tiles.Pipe_Left_Top = load_image('pipe_left_top.png')
            Tiles.Pipe_Right_Top = load_image('pipe_right_top.png')
            Tiles.Pipe_Left_middle = load_image('pipe_left_middle.png')
            Tiles.Pipe_Right_middle = load_image('pipe_right_middle.png')
            Tiles.coin_1 = load_image('coin_1.png')
            Tiles.coin_2 = load_image('coin_2.png')
            Tiles.coin_3 = load_image('coin_3.png')
            Tiles.coin_4 = load_image('coin_4.png')

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            if self.tile == 8:
                self.tile = 9
            elif self.tile == 9:
                self.tile = 10
            elif self.tile == 10:
                self.tile = 11
            elif self.tile == 11:
                self.tile = 8
            self.timer = 100

    def draw(self):
        global see
        if self.tile == 0:
            pass
        if self.tile == 1:
            Tiles.Grass_Left.clip_composite_draw(0,0,16,16,0,'',self.x,self.y, 40,40)
        if self.tile == 2:
            Tiles.Grass_Middle.clip_composite_draw(0,0,16,16,0,'',self.x,self.y, 40,40)
        if self.tile == 3:
            Tiles.Grass_Right.clip_composite_draw(0,0,16,16,0,'',self.x,self.y, 40,40)
        if self.tile == 4:
            Tiles.Pipe_Left_Top.clip_composite_draw(0,0,16,16,0,'',self.x,self.y, 40,40)
        if self.tile == 5:
            Tiles.Pipe_Right_Top.clip_composite_draw(0,0,16,16,0,'',self.x,self.y, 40,40)
        if self.tile == 6:
            Tiles.Pipe_Left_middle.clip_composite_draw(0,0,15,16,0,'',self.x,self.y, 40,40)
        if self.tile == 7:
            Tiles.Pipe_Right_middle.clip_composite_draw(0,0,15,16,0,'',self.x, self.y, 40, 40)
        if self.tile == 8:
            Tiles.coin_1.clip_composite_draw(0,0,12,16,0,'',self.x, self.y, 20, 20)
        if self.tile == 9:
            Tiles.coin_2.clip_composite_draw(0,0,8,16,0,'',self.x, self.y, 20, 20)
        if self.tile == 10:
            Tiles.coin_3.clip_composite_draw(0,0,6, 16,0,'',self.x, self.y, 20, 20)
        if self.tile == 11:
            Tiles.coin_4.clip_composite_draw(0,0,8,16,0,'',self.x, self.y, 20, 20)


        if self.see and self.tile > 0:
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        print('ball disappear')
        if group == 'boy:ball':
            game_world.remove_object(self)

