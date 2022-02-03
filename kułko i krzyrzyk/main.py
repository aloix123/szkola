import   sys,time,quit_int
import pygame
from font_graczy import Font_graczy
from score_board import Scoreboard
from muzyka import Music
#todo , score board ogarni j  błą i sub klase
class Main:
    def __init__(self):
        """""
        najważniejsze zmienne 
        obrazy itd....
        """""
        self.flag=True
        self.red_score = 0
        self.blue_score = 0
        pygame.init()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.ffoonntt=Font_graczy("Gracz1", "Gracz2")
        self.winner='?'#pożyjemy zobaczymy
        self.tura = 'x'
        self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#hehe
        print(self.m[0])
        print(self.m[1])
        print(self.m[2])
        pygame.init()
        self.x=15
        self.y=15
        self.hight_screen = 606#wysokość ekranu
        self.widh_screen= 1000
        self.screen = pygame.display.set_mode((self.widh_screen, self.hight_screen))#ekran
        self.image_red = pygame.image.load('obrazki/czerwony_krzyrzyk.gif')#czewony krzyż
        self.image_blue = pygame.image.load('obrazki/niebieskie kułeczko.gif')# niebieskie kułko
        self.title_icon=pygame.image.load('obrazki/ikona_gry.gif')
        self.title = pygame.display.set_caption("Kółko i krzyrzyk")
        pygame.display.set_caption("Kółko i krzyrzyk")
        pygame.display.set_icon(self.title_icon)
        self.music=Music()

    def screeen(self):


        self.color_screen=(152,255,204)
        self.screen.fill(self.color_screen)


    def blitred(self):
        "rysuje czerwoney 'x'"
        self.screen.blit(self.image_red,[self.x,self.y])
    def blitblue(self):
        "rysuje niebieski 'y'"
        self.screen.blit(self.image_blue,[self.x,self.y])

    def events(self):
        #kliknięcia i takie tam
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_int.hwdp()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()==(1,0,0):
                    self.clik_search()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    quit_int.hwdp()
                if event.key==pygame.K_e:

                    self.flag=True
                if event.key==pygame.K_r:
                    self.flag=False


    def kratki(self):
        """""
        widzisz tutaj moduł odpowiadająca za rysowanie planszy do gry
        """""
        self.color_kratek=(0,0,0)
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((0,200,606,2)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((0,400,606,2)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((200,0,2,606)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((400,0,2,606)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((606,0,2,606)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((0,0,2,606)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((0,604,606,606)))
        pygame.draw.rect(self.screen,self.color_kratek,pygame.Rect((0,0,606,2)))
    def turn(self):
        """""
        moduł odpowiada za  wyświetlanie obrazków 
        i ciągłą zmiane rund
        """""
        if self.tura=='x':
            self.tura='y'
            self.blitred()
        else:
            self.tura='x'
            self.blitblue()
    def check_game(self):
        """""
        ten kod odpowiada za wyszukanie wszystkich możliwych pozycji wygranej dla niebieskiego oraz czerwonego ,
        tych pozycji jest 8 i każdy kod wyłapuje pozycję z macierzy 'x' i 'y' , sprawdza czy występują w tabelce i wyłania zwycięzce
        """
        if self.tura=='y':
            self.winner='czerwony'
        elif self.tura=='x':
            self.winner='niebieski'
        if (self.m[0][0]=='x' and self.m[1][0]=='x' and self.m[2][0]=='x') or(self.m[0][0]=='y' and self.m[1][0]=='y' and self.m[2][0]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[0][1]=='x' and self.m[1][1]=='x' and self.m[2][1]=='x') or(self.m[0][1]=='y' and self.m[1][1]=='y' and self.m[2][1]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[0][2]=='x' and self.m[1][2]=='x' and self.m[2][2]=='x') or(self.m[0][2]=='y' and self.m[1][2]=='y' and self.m[2][2]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[0][0]=='x' and self.m[1][1]=='x' and self.m[2][2]=='x') or(self.m[0][0]=='y' and self.m[1][1]=='y' and self.m[2][2]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[0][2]=='x' and self.m[1][1]=='x' and self.m[2][0]=='x') or(self.m[0][2]=='y' and self.m[1][1]=='y' and self.m[2][0]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[0][0]=='x' and self.m[0][1]=='x' and self.m[0][2]=='x') or(self.m[0][0]=='y' and self.m[0][1]=='y' and self.m[0][2]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[1][0]=='x' and self.m[1][1]=='x' and self.m[1][2]=='x') or(self.m[1][0]=='y' and self.m[1][1]=='y' and self.m[1][2]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif (self.m[2][0]=='x' and self.m[2][1]=='x' and self.m[2][2]=='x') or(self.m[2][0]=='y' and self.m[2][1]=='y' and self.m[2][2]=='y'):
            if self.winner=='czerwony':
                self.red_score+=1
            else:
                self.blue_score+=1
            time.sleep(1)
            print(f"wygrał {self.winner}")
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
        elif self.m[0][0]!=0 and self.m[0][1]!=0 and self.m[0][2]!=0 and self.m[1][0]!=0 and self.m[1][1]!=0 and self.m[1][2]!=0 and self.m[2][0]!=0 and self.m[2][1]!=0 and self.m[2][2]!=0:
            time.sleep(1)
            self.m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # hehe
            self.screeen()
            self.kratki()
            print("remis")





    def run_game(self):
        """""
        tutaj jest start gry, niezbędne funkcje 
        
        """""


        self.screeen()
        self.kratki()

        while True:
            self.events()
            self.actual_points()
            self.ffoonntt.draw_font(self.screen)

            pygame.display.flip()
            self.check_game()


    def clik_search(self):
        """""
        sprawdza pozycję klikniętej myszy , wyłania z niej liczbę całkowitą
        oraz rysuje odpowiedni obrazek w zalerzności od tury
        """""

        position_mouse = pygame.mouse.get_pos()

        print(position_mouse)
        position_mouse = position_mouse[0] // 202, position_mouse[1] // 202

        self.pos1=position_mouse[0]
        self.pos2=position_mouse[1]
        self.x = 15 +self.pos1*202
        self.y = 15 +self.pos2*202

        #zeruwićki

        if position_mouse==(0,0):
            self.music.play_uff()
            if self.m[0][0]==0:
                self.m[0][0] = self.tura
                self.turn()

        elif position_mouse==(1,0):
            self.music.play_uff()
            if self.m[0][1]==0:
                self.m[0][1] = self.tura
                self.turn()

        elif position_mouse==(2,0):
            self.music.play_uff()
            if self.m[0][2]==0:
                self.m[0][2] = self.tura
                self.turn()

        #jedinićki
        elif position_mouse==(0,1):
            self.music.play_uff()
            if self.m[1][0]==0:
                self.m[1][0] = self.tura
                self.turn()

        elif position_mouse==(1,1):
            self.music.play_uff()
            if self.m[1][1]==0:
                self.m[1][1] = self.tura
                self.turn()

        elif position_mouse==(2,1):
            self.music.play_uff()
            if self.m[1][2]==0:
                self.m[1][2] = self.tura
                self.turn()

        #dwuićki
        elif position_mouse==(0,2):
            self.music.play_uff()
            if self.m[2][0]==0:
                self.m[2][0] = self.tura
                self.turn()

        elif position_mouse == (1, 2):
            self.music.play_uff()
            if self.m[2][1] == 0:
                self.m[2][1] = self.tura
                self.turn()

        elif position_mouse == (2, 2):
            self.music.play_uff()
            if self.m[2][2] == 0:
                self.m[2][2] = self.tura
                self.turn()
        #te printy nie są potrzebne , lecz są przydatne i fajnie informuja o pozycji jej

        print(self.m[0])
        print(self.m[1])
        print(self.m[2])
    def actual_points(self):
        self.score_text=f'{self.red_score}:{self.blue_score}'
        self.scoreoero = Scoreboard(self.red_score, self.blue_score,self.score_text)
        self.scoreoero.draw_score(self.screen)




#odpalanie gry
if __name__=='__main__':
    game=Main()
    game.run_game()