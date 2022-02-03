import pygame

class Words:
    def __init__(self,screen,hight,text,x,y):
        self.screen=screen
        self.hight= hight
        self.text=text
        self.x=x
        self.y=y
        self.words=pygame.font.SysFont("paweł",self.hight)
        self.render=self.words.render(self.text,True,(0,0,0))
    def blit(self):
        self.screen.blit(self.render,(self.x,self.y))
