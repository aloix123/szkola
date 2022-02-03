import pygame


class Obstacle:
    def __init__(self,screen):
        pygame.init()
        self.screen=screen
        self.block_1_hight=30
        self.block_1_weidh=30

        self.only_poz_x=570
        self.start_poz_y=400
        self.block_1 = pygame.Rect(self.start_poz_y, self.only_poz_x, self.block_1_hight, self.block_1_hight)
    def draw_obstacle(self):
        pygame.draw.rect(self.screen,(0,0,0),self.block_1)
    def obstacle_run(self):
        self.block_1.x-=3

