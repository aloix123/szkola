import pygame,sys

class Events:
    def __init__(self):
        pass
    def checkevents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False
                sys.exit()