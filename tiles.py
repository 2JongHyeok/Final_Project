from pico2d import *
max_map_size = 3200


coin_start = 9

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
    Ground = None


    see = False

    def __init__(self):
        self.tile = 0
        self.x = 0
        self.fixed_x = 0
        self.y = 0
        self.timer = 100
        if self.Grass_Left == None:
            Tiles.Grass_Left = load_image('./tilefiles/Grass (1).png')# 1
            Tiles.Grass_Middle = load_image('./tilefiles/Grass (2).png')# 2
            Tiles.Grass_Right = load_image('./tilefiles/Grass (3).png')# 3
            Tiles.Pipe_Left_Top = load_image('./tilefiles/Pipe (1).png')# 4
            Tiles.Pipe_Right_Top = load_image('./tilefiles/Pipe (2).png')# 5
            Tiles.Pipe_Left_middle = load_image('./tilefiles/Pipe (3).png')# 6
            Tiles.Pipe_Right_middle = load_image('./tilefiles/Pipe (4).png')# 7
            Tiles.Ground = load_image('./tilefiles/Grass (4).png')# 8
            Tiles.coin_1 = load_image('./tilefiles/Coin (1).png')# 9
            Tiles.coin_2 = load_image('./tilefiles/Coin (2).png')# 10
            Tiles.coin_3 = load_image('./tilefiles/Coin (3).png')# 11
            Tiles.coin_4 = load_image('./tilefiles/Coin (4).png')# 12

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            if self.tile == coin_start:
                self.tile = coin_start + 1
            elif self.tile == coin_start + 1:
                self.tile = coin_start + 2
            elif self.tile == coin_start + 2:
                self.tile = coin_start + 3
            elif self.tile == coin_start + 3:
                self.tile = coin_start
            self.timer = 100

    def draw(self):
        global see
        if self.tile == 0:
            pass
        if self.tile == 1:
            Tiles.Grass_Left.draw(self.x,self.y, 40, 40)
        if self.tile == 2:
            Tiles.Grass_Middle.draw(self.x, self.y, 40, 40)
        if self.tile == 3:
            Tiles.Grass_Right.draw(self.x, self.y, 40, 40)
        if self.tile == 4:
            Tiles.Pipe_Left_Top.draw(self.x, self.y, 40, 40)
        if self.tile == 5:
            Tiles.Pipe_Right_Top.draw(self.x, self.y, 40, 40)
        if self.tile == 6:
            Tiles.Pipe_Left_middle.draw(self.x, self.y, 40, 40)
        if self.tile == 7:
            Tiles.Pipe_Right_middle.draw(self.x, self.y, 40, 40)
        if self.tile == 8:
            Tiles.Ground.draw(self.x, self.y, 40, 40)
        if self.tile == 9:
            Tiles.coin_1.draw(self.x, self.y, 20, 20)
        if self.tile == 10:
            Tiles.coin_2.draw(self.x, self.y, 20, 20)
        if self.tile == 11:
            Tiles.coin_3.draw(self.x, self.y, 20, 20)
        if self.tile == 12:
            Tiles.coin_4.draw(self.x, self.y, 20, 20)


        if self.see and self.tile > 0:
            if self.x >= - 50 and self.x <= 1650:
                draw_rectangle(*self.get_bb())

    def get_bb(self):
        if(self.x >= - 50  and self.x <= 1650):
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

