import pygame,sys,time # różne importy

from settings import Settings
from paletka import Paletka
from ball import Ball
from Scoreboard  import SScoreboard
from Sounds_or_music import sound_music
from Button import buton
""""ostatni pracowałem przy przycisku , stworzyłem liste do sprawdzenia czy chłop ją wcisnoł"""
class Gra(Settings):
    def __init__(self):# różne klasy, zmienne itd
        pygame.init()
        self.important_objects()
    def run_Gra(self):#sama gra
        while True:
            self.Tlo()
            self.events()
            self.game_activer()
            pygame.display.flip()
            time.sleep(0.005)  # speed
    def Tlo(self):# tło, kolor tła,rysunki o obiekty na nim umieszczone
        """tutaj powstaje tło ,kolor okna,i jego parametry"""
        self.screen.fill(self.szary) # wypełnia tło szarym kolorem
        self.f.draw_paletka()# blituje paletki
        self.ball.draw_ball()# blituje piłkE
        if self.active == False:
            self.baton.button_draw()
    def events(self):# funkcja odpowiadająca za wciśnięte kalwisze i ich reakcje na otoczenie
        for event in pygame.event.get():
            if event.type==pygame.QUIT:# czy chłop wcisnoł iksik w prawym górnym rogu ekranu
                sys.exit()# program się wyłącza
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q or event.key==pygame.K_ESCAPE:# jeśli chłop wciśnie q lub escape
                    sys.exit()# wyłącz grę
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()==(1,0,0):
                    positin=pygame.mouse.get_pos()
                    if self.baton.hihi_buton.collidepoint(positin):
                        pygame.mouse.set_visible(False)
                        pygame.mouse.set_system_cursor( pygame.SYSTEM_CURSOR_HAND)
                        self.active=True
    def events_pressed(self):# funkcja odpowiada za posuszanie się paletek po ekranie , tryb poruszania się to WS i up down
        if self.f.rect1.y>1:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.f.rect1.y-=self.opcje.paletka_speed
                self.f.gps1-=self.opcje.paletka_speed
        if self.f.rect1.y<600:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.f.rect1.y+=self.opcje.paletka_speed
                self.f.gps1 += self.opcje.paletka_speed
        """"" Sprawdza czy chłop wciska WS"""""
        if self.f.rect2.y>1:
            if pygame.key.get_pressed()[pygame.K_w]:
                self.f.rect2.y-=self.opcje.paletka_speed
                self.f.gps2 -= self.opcje.paletka_speed
        if self.f.rect2.y<600:
            if pygame.key.get_pressed()[pygame.K_s]:
                self.f.rect2.y+=self.opcje.paletka_speed
                self.f.gps2 += self.opcje.paletka_speed
    def backend(self):# ruch piłki
        self.ball.ball_run()
        self.listadesunia_deskalewa()
        self.listadesunia_deskaprawa()
        self.ball_check()
        self.check_points()
        self.actual_points()
        self.scoreboard.show_score(self.screen)#liczba punktów
        self.allmusic.background_setmusic()
        #self.cursor()
    def listadesunia_deskalewa(self):#kolejna lista
        self.hag_lista = [i for i in range(-self.opcje.ball_size,self.opcje.deska_height+self.opcje.ball_size)]
        self.lista = list(map(lambda x: x + self.f.gps1, self.hag_lista))

    def listadesunia_deskaprawa(self):#lista
        self.hag_listas = [i for i in range(-self.opcje.ball_size,self.opcje.deska_height+self.opcje.ball_size)]
        self.listas = list(map(lambda x: x + self.f.gps2, self.hag_listas))
    def ball_check(self):
        """"""" ta funkcja odbija piłke od paletki"""""""
        if  self.ball.bal_rect.x==self.opcje.gps_height1-10 and  self.ball.bal_rect.y in self.lista:# jeśli piłka przed niebieską paletką i w liście
            self.ball.a=-self.ball.a # odbij

        if  self.ball.bal_rect.x==self.opcje.gps_height2+10 and  self.ball.bal_rect.y in self.listas:# jeśli piłka przed  czerwoną paletką i w liście

            self.ball.a=-self.ball.a #odbij w przeciwna stronę
    def check_points(self):
        if self.ball.bal_rect.x==0: # jeśli piłka uderzy lewą ściankę
            self.allmusic.run_UFF() # UFF
            self.ball.bal_rect.y=350
            self.ball.bal_rect.x = 500
            self.ball.a = -1
            self.score[0]+=1# PLUS JEDEN PUNKT DLA PRZECIWNIKA
        if self.ball.bal_rect.x == 990:# jeśli piłka uderzy prawA ściankę
            self.allmusic.run_UFF()# UFF
            self.ball.bal_rect.y = 350
            self.ball.bal_rect.x = 500
            self.ball.a=1
            self.score[1]+=1# PLUS JEDEN PUNKT DLA PRZECIWNIKA
    def actual_points(self):# aktualizuje liczbę punktów
        self.final_score=f'{self.score[0]}:{self.score[1]}'
        self.scoreboard = SScoreboard(self.final_score, self.szary)
    def game_activer(self):# jeśli gra jest aktywna
        if self.active:
            self.backend()
            self.events_pressed()
    def important_objects(self):
        """""najwarzniejsze zmienne definiujące tło,wysokość i szerokość tła , tytuł gry i jego ikonę"""""
        self.screen_height = 700
        self.screen_widh = 1000
        self.screen = pygame.display.set_mode((self.screen_widh, self.screen_height))  # okno
        pygame.display.set_caption('Pingpong 2D')
        pygame.display.set_icon(pygame.image.load('512x512bb.jpg'))
        self.szary = (160, 160, 160)
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)  # kursor ma taką łapkę fajną
        """""lewa i prawa paletka 2d"""""
        self.f = Paletka(self.screen)
        """inne objekty"""
        self.allmusic = sound_music()# odpowiada za muzyke w tle i za dźwięk uderzenia UFF
        self.baton = buton(self.screen)# tworzy przycisk aktywujący grę
        self.score = [0, 0] # startowy wynik gry
        self.ball = Ball(self.screen, self.f.gps1) # sama piłka
        self.active = False # aktywacja gry( na początku jest wyłączona a po wciśn ięciu przycisku się aktywuje)
        self.opcje = Settings() # opcje
        """""
    def cursor(self):
        positin = pygame.mouse.get_pos()
        if self.baton.hihi_buton.colliderect(positin):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)  # kursor ma taką łapkę fajn
        """""



if __name__=='__main__':# sprawdza czy się coś nie pierdoli z kodem
    d=Gra()
    d.run_Gra()