

import pygame

class Dragon:
    def __init__(self,screen):
        pygame.init()
        self.klucyk=-1
        self.screen=screen
        self.image_up_normal=pygame.image.load("zdjęcia/real_dinozar.gif")
        self.image_up_up=pygame.image.load('zdjęcia/real_dinozar_leg_up.gif')
        self.image_up_down=pygame.image.load('zdjęcia/real_dinozar_leg_down.gif')
        self.image_down_up=pygame.image.load('zdjęcia/real_sit dinozar_leg_up.gif')
        self.image_down_down=pygame.image.load('zdjęcia/real_sit dinozar_leg_down.gif')
        self.uf_dinozar=pygame.image.load('zdjęcia/uf_dinozar.gif')
        self.image_surface=self.image_up_normal.get_rect()
        self.pozition_y=538
        self.pozition_x=200
        self.down_poz_y=566
        #standardowy smok
    def blit_dragon_up(self):
        self.screen.blit(self.image_up_normal, (self.pozition_x, self.pozition_y))
        #tup tup tup
    def blit_up_up(self):
        self.screen.blit(self.image_up_up,(self.pozition_x, self.pozition_y))
    def blit_up_down(self):
        self.screen.blit(self.image_up_down,(self.pozition_x, self.pozition_y))
    def blit_down_up(self):
        self.screen.blit(self.image_down_up, (self.pozition_x, self.down_poz_y))
    def blit_down_down(self):
        self.screen.blit(self.image_down_down, (self.pozition_x, self.down_poz_y))
    def blit_uffdragon(self):
        self.screen.blit(self.uf_dinozar, (self.pozition_x, self.pozition_y))
    def blitnoraml(self):
        self.screen.blit(self.image_up_normal, (self.pozition_x, self.pozition_y))
