
import pygame

class buton():
    def __init__(self,screen):
        self.screen=screen
        self.przycisk=pygame.image.load('pryzcisk.jpg')
        self.button_gps1=350
        self.button_gps2=450
        self.hihi_buton=pygame.Rect((self.button_gps2,self.button_gps1,100,75))
    def button_draw(self):
        self.screen.blit(self.przycisk,(self.button_gps2,self.button_gps1))
