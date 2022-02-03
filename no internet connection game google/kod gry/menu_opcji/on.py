import pygame

class On:
    def __init__(self,screen):
        self.screen=screen
        self.on_image=pygame.image.load('zdjęcia/menu/ON.png')
        self.on_pozx=241
        self.on_pozy=156
        self.on_rect=self.on_image.get_rect()
    def blit(self):
        self.screen.blit(self.on_image, (self.on_pozx, self.on_pozy))