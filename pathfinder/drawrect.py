import pygame
from importantthings.parameters import Parameters



class Recttt:
    def __init__(self,x,y,screen,color,hight,width):
        self.screen=screen
        self.x=x
        self.y=y
        self.color=color
        self.hight=hight
        self.width=width
        self.pmt = Parameters()
        self.rect_square = pygame.Rect(self.x ,self.y, self.hight,
                                       self.width)

    def drawRect(self):
        pygame.draw.rect(self.screen, self.color, self.rect_square)
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getrect(self):
        return self.rect_square
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def getColor(self):
        return self.color
    def setColor(self,c):
        self.color=c
