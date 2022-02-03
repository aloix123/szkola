import pygame

class oppcje:
    def __init__(self,screen):
        self.screen=screen
        self.po_image=pygame.image.load('zdjęcia/opp_buton.gif')
        self.surf_po_image=self.po_image.get_rect()
        print(self.surf_po_image)
    def blit(self):
        self.screen.blit(self.po_image,(0,0))