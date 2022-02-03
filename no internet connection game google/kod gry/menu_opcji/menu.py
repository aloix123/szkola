
import pygame
class Menu:
    def __init__(self,screen):
        self.screen=screen
        self.menu_image=pygame.image.load('zdjęcia/menu/menu.png')
        self.surf_menu=self.menu_image.get_rect()
    def blit(self):
        self.screen.blit(self.menu_image,(101,100))