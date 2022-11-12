from pico2d import *

max_map_size = 3200



class Tiles:
    Grass_Left = None
    Grass_Middle = None
    Grass_Right = None
    Pipe_Left_Top = None
    Pipe_Right_Top = None
    see = False

    def __init__(self):
        self.tile = 0 # 0 : 왼쪽풀, 1: 가운데풀, 2: 오른쪽풀
        self.x = 0
        self.y = 0
        if self.Grass_Left == None:
            Tiles.Grass_Left = load_image('grass_left.png')
            Tiles.Grass_Middle = load_image('grass_middle.png')
            Tiles.Grass_Right = load_image('grass_right.png')
            Tiles.Pipe_Left_Top = load_image('pipe_left_top.png')
            Tiles.Pipe_Right_Top = load_image('pipe_right_top.png')

    def update(self):
        pass

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


        if self.see and self.tile > 0:
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
