import pygame

class gameOver:
    def __init__(self,screen):
        self.screen=screen
        self.image_tekst=pygame.image.load('zdjęcia/Game-over.gif')
        self.tekst_x=300
        self.tekst_y=300
    def blit_tekst(self):
        self.screen.blit(self.image_tekst,(self.tekst_x,self.tekst_y))

