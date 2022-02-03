import pygame

class Cloud:
    def __init__(self,screen):
        self.screen=screen
        self.cloud_image=pygame.image.load('zdjęcia/wwwcloud_ready.gif')
        self.cloud_pozx=500
        self.cloud_pozy=30
    def draw_cloud(self):
        self.screen.blit(self.cloud_image,(self.cloud_pozx,self.cloud_pozy))