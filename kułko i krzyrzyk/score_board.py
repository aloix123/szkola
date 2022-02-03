
import pygame
from font_graczy import Font_graczy

class Scoreboard(Font_graczy):
    def __init__(self,red_score,blue_score,scoretext):
        Font_graczy.__init__(self)
        pygame.init()

        self.red_score=red_score
        self.blue_score=blue_score
        self.scoretext=scoretext
        self.score_sth= pygame.font.SysFont(None, 25)
        self.score_image=self.score_sth.render(self.scoretext, True, self.font_kolor, self.tło)

    def draw_score(self,screen):
        self.screen=screen
        self.screen.blit(self.score_image,(789,47))