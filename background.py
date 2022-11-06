from pico2d import *

max_map_size = 3200

class BackGround:
    def __init__(self):
        self.starmap_1 = load_image('star_map_1.png')
        self.starmap_2 = load_image('star_map_2.png')
        self.starmap_3 = load_image('star_map_3.png')
        self.mansion_1 = load_image('mansion_1.png')
        self.mansion_2 = load_image('mansion_2.png')
        self.stage = 1
        self.frame = 0
        self.need_frame = 0
        self.play_x = 0
        self.max_map = max_map_size // 1600 # for문안에 넣어서 총 몇개의 화면을 출력할지 출력

    def update(self,x):
        if self.stage == 0:
            self.need_frame = 0
            self.frame = 0
        elif self.stage == 1:
            self.need_frame = 600
        elif self.stage == 2:
            self.need_frame = 400
        self.frame = (self.frame + 1) % self.need_frame
        if x >= 800 and x <= max_map_size - 800:
            self.play_x = x

    def draw(self):
        if self.frame <= 200:
            if self.stage == 1:
                self.draw_star_1()
            elif self.stage == 2:
                self.draw_mansion_1()
        elif self.frame > 200 and self.frame <= 400:
            if self.stage == 1:
                self.draw_star_2()
            elif self.stage == 2:
                self.draw_mansion_2()
        elif self.frame > 400 and self.frame <= 600:
            if self.stage == 1:
                self.draw_star_3()

    def draw_mansion_1(self):
        for i in range(0, self.max_map + 1):
            self.mansion_1.draw_to_origin((1600 * i)-self.play_x, 0, 1600, 800)

    def draw_mansion_2(self):
        for i in range(0, self.max_map + 1):
            self.mansion_2.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)

    def draw_star_1(self):
        for i in range(0, self.max_map + 1):
            self.starmap_1.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)

    def draw_star_2(self):
        for i in range(0, self.max_map + 1):
            self.starmap_2.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)

    def draw_star_3(self):
        for i in range(0, self.max_map + 1):
            self.starmap_3.draw_to_origin((1600 * i) - self.play_x, 0, 1600, 800)