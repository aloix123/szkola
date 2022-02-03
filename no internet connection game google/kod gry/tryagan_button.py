import pygame
class Przycisk:
    def __init__(self,screen):
        self.screen=screen
        self.pp=pygame.image.load('zdjęcia/try_agan_button.gif')
        self.tekst_xx = 370
        self.tekst_yy = 320
        self.rect_pp=pygame.Rect((self.tekst_xx,self.tekst_yy,50,50))
    def blit_baton(self):
        self.screen.blit(self.pp,(self.tekst_xx,self.tekst_yy))