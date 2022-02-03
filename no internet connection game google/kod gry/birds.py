
import pygame

class Bird:
    def __init__(self,screen):
        self.screen=screen
        self.image_upu=pygame.image.load('zdjęcia/bird_wings_up.gif')
        self.image_downu=pygame.image.load('zdjęcia/bird_wings_down.gif')
      #  print(self.image_downu.get_rect())
        self.bird_pozx=520
        self.bird_pozy=530
    def blit_up(self):
        self.screen.blit(self.image_upu,(self.bird_pozx,self.bird_pozy))
    def blit_down(self):
        self.screen.blit(self.image_downu,(self.bird_pozx,self.bird_pozy))
    def bird_run(self):
        self.bird_pozx-=3
