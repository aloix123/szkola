
import pygame
class Off:
    def __init__(self,screen):
        self.screen=screen
        self.image_off=pygame.image.load('zdjęcia/menu/OFF.png')
        self.on_pozx = 241
        self.on_pozy = 156
        self.off_rect = self.image_off.get_rect()
    def blit(self):
        self.screen.blit(self.image_off,(self.on_pozx,self.on_pozy))
