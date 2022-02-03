import pygame

from importantthings.parameters import Parameters
from drawrect import Recttt
from fonter import Words
from importantthings.rectcontainer import rectyyelow
class Screen():

    def __init__(self):
        pygame.init()
        self.pr = Parameters()
        self.screen = pygame.display.set_mode((self.pr.screen_hight, self.pr.screen_width))





    def screenColor(self):
        self.screen.fill(self.pr.biały)

    def drawKratki(self):
        self.pasek_rect1 = pygame.Rect(0, 0, 980, self.pr.g_paska)
        self.pasek_rect2 = pygame.Rect(0, 0, self.pr.g_paska, 980)
        for i in range(self.pr.square_count + 2):
            pygame.draw.rect(self.screen, (0, 0, 0), self.pasek_rect1)
            self.pasek_rect1.y += 20
            if self.pasek_rect1.y>980:
                break
        for i in range(self.pr.square_count + 5):
            pygame.draw.rect(self.screen, (0, 0, 0), self.pasek_rect2)
            self.pasek_rect2.x += 20
            if self.pasek_rect2.x>980:
                break
    def drawrectangulars(self):
        ile=0
        coile=150
        self.rectangulars=[]
        while ile<=4:
            self.rectangulars.append(Recttt(980, 75 + coile * ile, self.screen, self.pr.jasnoszary, 1150, 100))
            ile+=1
        for rects in self.rectangulars:
            rects.drawRect()

    def returnyelowsurf(self):
        for re in self.rectangulars:
            rectyyelow.append(re)

    def drawfonts(self):
        ile=0
        coile=150
        fonty=[]
        tekst=["Start","yellow(end)","blue(start)","czarny(wals)","Clear"]
        hight=[100,50,50,50,50]
        ahh=1200

        x=[1161,ahh,ahh,ahh,ahh]
        beka=[90,100,100,100,100]

        while ile<=4:
            fonty.append(Words(self.screen,hight[ile],tekst[ile],x[ile],beka[ile]+ile*coile))
            ile+=1
        for font in fonty:
            font.blit()
    def drawsmallrects(self):
        colors=[self.pr.yellow,self.pr.jasnyblu,self.pr.black]
        ile=0
        coile=150
        rekty=[]
        while ile<=2:
            rekty.append(Recttt(1000, 234 + coile * ile, self.screen, colors[ile], 80, 80))
            ile+=1
        for reck in rekty:
            reck.drawRect()