from pico2d import *

max_map_size = 3200

class BackGround:
    starmap_1 = None
    def __init__(self):
        if self.starmap_1 == None:
            self.starmap_1 = load_image('./backgroundfiles/Star (1).png')
            self.starmap_2 = load_image('./backgroundfiles/Star (2).png')
            self.starmap_3 = load_image('./backgroundfiles/Star (3).png')
            self.mansion_1 = load_image('./backgroundfiles/Mansion (1).png')
            self.mansion_2 = load_image('./backgroundfiles/Mansion (2).png')
        self.stage = 1
        self.frame = 0
        self.need_frame = 0
        self.play_x = 0
        self.max_map = max_map_size // 1600 # for문안에 넣어서 총 몇개의 화면을 출력할지 출력
        if self.stage == 0:
            self.need_frame = 0
            self.frame = 0
        elif self.stage == 1:
            self.need_frame = 600
        elif self.stage == 2:
            self.need_frame = 400


    def update(self):
        pass


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