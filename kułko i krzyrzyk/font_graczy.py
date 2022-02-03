
import pygame.font

class Font_graczy:
    def __init__(self,gracz1="gracz1",gracz2="gracz2"):
        pygame.init()
        self.score_pozition=(643,20)
        self.tło=(152,255,204)
        self.gracz1=gracz1
        self.gracz2=gracz2
        self.tekst_font=f'{gracz1}(czerwony) vs {gracz2}(niebieski)'
        self.wielkość_czcionki=10
        self.font_kolor=(0,0,255)
        self.ffont=pygame.font.SysFont(None ,25)
        self.font_image=self.ffont.render(self.tekst_font, True, self.font_kolor, self.tło)
    def draw_font(self,screen):
        self.screen = screen
        self.screen.blit(self.font_image,self.score_pozition)