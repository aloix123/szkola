import pygame
from drawrect import Recttt
from importantthings.parameters import Parameters
from importantthings.rectcontainer import rectyyelow
class Clik:
    def __init__(self,screen):
        self.squares=[]
        self.screen=screen
        self.prm=Parameters()

        self.cursorcolor=self.prm.getblack()
        self.cursorect=pygame.Surface((self.prm.square_hw,self.prm.square_hw)).get_rect()



        pass
    def position(self):
        self.ifinsquareCheck()
        self.ifrectjangalschekck()

    def show_squers(self):
        for kwadracik in self.squares:
            kwadracik.drawRect()

    def changecursorcolor(self):

       pass

    def showkursor(self):
        mouse = pygame.mouse.get_pos()
        xy=10
        pygame.draw.rect(self.screen, self.cursorcolor, (mouse[0]-xy,mouse[1]-xy,self.prm.square_hw,self.prm.square_hw))
    def ifinsquareCheck(self):
        #napraw to

        mouse=pygame.mouse.get_pos()
        mouse = mouse[0] // 20, mouse[1] // 20
        print(mouse)


        if mouse[0] <= 48 and pygame.mouse.get_pressed()==(1,0,0):
            jasnublu = []
            yelow=[]
            self.squares.append(Recttt(mouse[0] * 20, mouse[1] * 20, self.screen, self.cursorcolor, self.prm.getsquarehw(), self.prm.getsquarehw()))
            for ele in self.squares:

                if ele.color==self.prm.getjasnyblu() :

                    jasnublu.append(ele)
                    if len(jasnublu)>1:
                        self.squares.remove(jasnublu[0])
                        jasnublu.pop(0)
                if ele.color==self.prm.getyellow() :

                    yelow.append(ele)
                    if len(yelow)>1:
                        self.squares.remove(yelow[0])
                        yelow.pop(0)


    def ifrectjangalschekck(self):
        mouse=pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(rectyyelow[0].rect_square ,mouse) and pygame.mouse.get_pressed() == self.prm.lewy:
            pass
            #statart algorytm
        elif pygame.Rect.collidepoint(rectyyelow[1].rect_square ,mouse) and pygame.mouse.get_pressed() == self.prm.lewy:
            self.cursorcolor=self.prm.getyellow()

        elif pygame.Rect.collidepoint(rectyyelow[2].rect_square ,mouse) and pygame.mouse.get_pressed() == self.prm.lewy:
            self.cursorcolor=self.prm.getjasnyblu()
        elif pygame.Rect.collidepoint(rectyyelow[3].rect_square ,mouse) and pygame.mouse.get_pressed() == self.prm.lewy:
            self.cursorcolor=self.prm.getblack()
        elif pygame.Rect.collidepoint(rectyyelow[4].rect_square ,mouse) and pygame.mouse.get_pressed() == self.prm.lewy:
            self.squares.clear()




