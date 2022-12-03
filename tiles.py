from pico2d import *

import server

max_map_size = 3200


coin_start = 9
hp_start = 23
att_start = 28

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
    Select_Stage_Right_Pipe = None
    Select_Stage_Left_Pipe = None
    Shop_Right_Pipe = None
    Shop_Left_Pipe = None
    Stage_1_Right_Pipe = None
    Stage_1_Left_Pipe = None
    Stage_2_Right_Pipe = None
    Stage_2_Left_Pipe = None
    Stage_3_Right_Pipe = None
    Stage_3_Left_Pipe = None
    Hp_block_1 = None
    Hp_block_2 = None
    Hp_block_3 = None
    Hp_block_4 = None
    Hp_block_5 = None
    Att_block_1 = None
    Att_block_2 = None
    Att_block_3 = None
    Att_block_4 = None
    Att_block_5 = None


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
            Tiles.Select_Stage_Left_Pipe = load_image('./tilefiles/Pipe (1).png')  # 13
            Tiles.Select_Stage_Right_Pipe = load_image('./tilefiles/Pipe (2).png')  # 14
            Tiles.Shop_Left_Pipe = load_image('./tilefiles/Pipe (1).png')  # 15
            Tiles.Shop_Right_Pipe = load_image('./tilefiles/Pipe (2).png')  # 16
            Tiles.Stage_1_Left_Pipe = load_image('./tilefiles/Pipe (1).png')  # 17
            Tiles.Stage_1_Right_Pipe = load_image('./tilefiles/Pipe (2).png')  # 18
            Tiles.Stage_2_Left_Pipe = load_image('./tilefiles/Pipe (1).png')  # 19
            Tiles.Stage_2_Right_Pipe = load_image('./tilefiles/Pipe (2).png')  # 20
            Tiles.Stage_3_Left_Pipe = load_image('./tilefiles/Pipe (1).png')  # 21
            Tiles.Stage_3_Right_Pipe = load_image('./tilefiles/Pipe (2).png')  # 22
            Tiles.Hp_block_1 = load_image('./tilefiles/Item_Block (1).png') # 23
            Tiles.Hp_block_2 = load_image('./tilefiles/Item_Block (2).png') # 24
            Tiles.Hp_block_3 = load_image('./tilefiles/Item_Block (3).png') # 25
            Tiles.Hp_block_4 = load_image('./tilefiles/Item_Block (4).png') # 26
            Tiles.Hp_block_5 = load_image('./tilefiles/Item_Block (5).png') # 27
            Tiles.Att_block_1 = load_image('./tilefiles/Item_Block (1).png') # 28
            Tiles.Att_block_2 = load_image('./tilefiles/Item_Block (2).png') # 29
            Tiles.Att_block_3 = load_image('./tilefiles/Item_Block (3).png') # 30
            Tiles.Att_block_4 = load_image('./tilefiles/Item_Block (4).png') # 31
            Tiles.Att_block_5 = load_image('./tilefiles/Item_Block (5).png') # 32

    def update(self):
        if server.Hp_Need_Money > server.Mario_Coin:
            if hp_start <= self.tile <= hp_start + 3:
                self.tile = hp_start + 4
        if server.Att_Need_Money > server.Mario_Coin:
            if att_start <= self.tile <= att_start + 3:
                self.tile = att_start + 4
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
            elif self.tile == hp_start:
                self.tile = hp_start + 1
            elif self.tile == hp_start + 1:
                self.tile = hp_start + 2
            elif self.tile == hp_start + 2:
                self.tile = hp_start + 3
            elif self.tile == hp_start + 3:
                self.tile = hp_start
            elif self.tile == att_start:
                self.tile = att_start + 1
            elif self.tile == att_start + 1:
                self.tile = att_start + 2
            elif self.tile == att_start + 2:
                self.tile = att_start + 3
            elif self.tile == att_start + 3:
                self.tile = att_start
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
        if self.tile == 13:
            Tiles.Select_Stage_Left_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 14:
            Tiles.Select_Stage_Right_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 15:
            Tiles.Shop_Left_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 16:
            Tiles.Shop_Right_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 17:
            Tiles.Stage_1_Left_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 18:
            Tiles.Stage_1_Right_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 19:
            Tiles.Stage_2_Left_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 20:
            Tiles.Stage_2_Right_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 21:
            Tiles.Stage_3_Left_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 22:
            Tiles.Stage_3_Right_Pipe.draw(self.x, self.y, 40, 40)
        if self.tile == 23:
            Tiles.Hp_block_1.draw(self.x, self.y, 40, 40)
        if self.tile == 24:
            Tiles.Hp_block_2.draw(self.x, self.y, 40, 40)
        if self.tile == 25:
            Tiles.Hp_block_3.draw(self.x, self.y, 40, 40)
        if self.tile == 26:
            Tiles.Hp_block_4.draw(self.x, self.y, 40, 40)
        if self.tile == 27:
            Tiles.Hp_block_5.draw(self.x, self.y, 40, 40)
        if self.tile == 28:
            Tiles.Att_block_1.draw(self.x, self.y, 40, 40)
        if self.tile == 29:
            Tiles.Att_block_2.draw(self.x, self.y, 40, 40)
        if self.tile == 30:
            Tiles.Att_block_3.draw(self.x, self.y, 40, 40)
        if self.tile == 31:
            Tiles.Att_block_4.draw(self.x, self.y, 40, 40)
        if self.tile == 32:
            Tiles.Att_block_5.draw(self.x, self.y, 40, 40)

        if self.see and self.tile > 0:
            if self.x >= - 50 and self.x <= 1650:
                draw_rectangle(*self.get_bb())

    def get_bb(self):
        if(self.x >= - 50  and self.x <= 1650):
            return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        pass

