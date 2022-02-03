import pygame

class XXX:
    def __init__(self,screen):
        self.screen=screen
        self.x_image=pygame.image.load('zdjęcia/menu/menu_iksde.gif')
        self.x_pozx=357
        self.x_pozy=101
        self.x_rekt=pygame.Rect(self.x_pozx,self.x_pozy,76,68)
    def blit(self):
        self.screen.blit(self.x_image ,(self.x_pozx, self.x_pozy))