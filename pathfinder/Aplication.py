import pygame
from screen import Screen
from drawrect import Recttt
from clikchecker import Clik
from event import Events
from importantthings.parameters import Parameters
from fonter import Words
from classpaathstuf import Distance
from importantthings.rectcontainer import rectyyelow
class Application:
    def __init__(self):
        pygame.init()
        self.game = True
        self.scr = Screen()
        self.prm=Parameters()
        self.klik=Clik(self.scr.screen)
        self.rctStart = Recttt(980, 75, self.scr.screen, self.prm.jasnoszary, 1150, 100)
        self.events=Events()
        self.titlefont=Words(self.scr.screen,50,"Pathfinder",1150,10)

        self.spine()



    def spine(self):
        while self.game:
            self.events.checkevents()
            self.scr.screenColor()
            self.scr.drawKratki()

            self.klik.show_squers()
            self.titlefont.blit()
            self.scr.drawrectangulars()
            self.scr.drawfonts()
            self.scr.drawsmallrects()
            self.scr.returnyelowsurf()
            self.klik.showkursor()
            self.klik.position()

            pygame.display.flip()


