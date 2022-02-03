import pygame, sys, time, random
from dinozarek import Dragon
from blok import Obstacle
from cloud import Cloud
from birds import Bird
from game_over import gameOver
from tryagan_button import Przycisk
from potions_button import oppcje
from menu_opcji.menu import Menu
from menu_opcji.X import XXX
from menu_opcji.on import On
from menu_opcji.off import Off
from muzyka.muzykaWtle import M
from tekst import *

class Mejn:
    def __init__(self):
        self.run_gejm = True  # przyda się do włączania i wyłączania gry
        self.game = True
        self.jumping = False
        self.hight_screen = 600
        self.weight_screen = 800
        self.window_type=pygame.RESIZABLE
        self.screen = pygame.display.set_mode((self.weight_screen, self.hight_screen), self.window_type)
        self.title = pygame.display.set_caption('T-rex game')
        self.color_screen = (255, 255, 255)
        # rzeczy do skakania
        self.vel_x = 14
        self.vel_y = 14
        # rzeczy do skakania
        self.smok = Dragon(self.screen)  # smoczek
        self.objekts = []  # lista chodzących bloczków
        self.dist_list = []  # kasuje bloczki
        self.clok = time.time()  # niuewiem po jaki chuj to jest xd
        self.flag = True
        self.pozition_y = 538
        self.pozition_x = 200
        self.only_poz_x = 570
        self.start_poz_y = 400
        self.rect_list = []
        self.can_jump = True
        self.key = -1
        self.jump_clok = time.time()
        #
        self.cloud_key = False
        self.chmura = Cloud(self.screen)
        self.chmura_time = time.time()
        self.clouds_list = []
        #
        self.klucyk = -1
        self.k = -1
        self.czss = time.time()
        #
        self.patn_opcje = oppcje(self.screen)
        self.bolrun = True
        self.bant_mmenu = Menu(self.screen)
        #
        self.iks = XXX(self.screen)
        self.on = On(self.screen)
        self.off = Off(self.screen)
        self.flagaPrzycis = 1
        self.w=Doc()
        self.OnOffRect = pygame.Rect(241, 156, 48, 39)
        #
        self.muzyczka=M()

    def ifOnOffClik(self):
        mo = pygame.mouse.get_pressed()
        if mo == (1, 0, 0):
            mm = pygame.mouse.get_pos()

            if self.OnOffRect.collidepoint(mm):
                self.flagaPrzycis = self.flagaPrzycis * -1
                l = open("windowType.txt", "+")
                l.
                l.close()
                if self.flagaPrzycis==1:
                    self.screen = pygame.display.set_mode((self.weight_screen, self.hight_screen),pygame.FULLSCREEN)

                elif self.flagaPrzycis==-1:
                    self.screen = pygame.display.set_mode((self.weight_screen, self.hight_screen), pygame.RESIZABLE,pygame.WINDOWEVENT_FOCUS_GAINED  )

                pygame.time.wait(100)

    def if_x_clik(self):

        m = pygame.mouse.get_pos()

        if self.iks.x_rekt.collidepoint(m):
            self.bolrun *= -1

    def MENUU(self):

        self.bant_mmenu.blit()
        if self.flagaPrzycis == 1:
            self.on.blit()
        elif self.flagaPrzycis == -1:
            self.off.blit()

    def gejmołwer(self):
        self.h = gameOver(self.screen)
        self.h.blit_tekst()

    def batn(self):
        self.hwdp = Przycisk(self.screen)
        self.hwdp.blit_baton()
        self.hwdp_rect = self.hwdp.pp.get_rect()

    def stop_game(self):
        if self.bolrun == 1:
            self.run_blocks()
            self.create_blocks()
            self.rects()
            self.dragon_type()
            self.if_space_clik()
            self.jump()
            self.create_blocks()
            self.lista_doblitowania()
        else:
            self.ifOnOffClik()
            self.MENUU()
            self.smok.blit_dragon_up()
            self.lista_doblitowania()
            self.iks.blit()




    def lista_doblitowania(self):

        for i in self.objekts:
            if type(i) == Bird:
                self.bird_anime(i)
            elif type(i) == Obstacle:
                i.draw_obstacle()

    def run_blocks(self):
        for element in self.objekts:
            if type(element) == Bird:
                element.bird_run()
            else:
                element.obstacle_run()
        for chmurka in self.clouds_list:
            chmurka.cloud_pozx -= 1

    def remove_blocks(self):

        self.nessery_list = [i for i in range(-50, -30)]
        for ele in self.objekts:
            if type(ele) == Bird:
                if ele.bird_pozx in self.nessery_list:
                    self.objekts.remove(ele)
            else:
                if ele.block_1.x in self.nessery_list:
                    self.objekts.remove(ele)

    def screeen(self):
        self.screen.fill(self.color_screen)

        self.remove_blocks()
        self.stop_game()

        self.patn_opcje.blit()

    def run_mejn(self):
        self.helpfull_create_func()
        self.help_birdfujhuj()
        while self.run_gejm:
            self.events()
            if self.game:
                self.screeen()
                self.colid_blocks()
                self.clouds()
                self.clouds_show()
                self.reset_list()
                self.clouds_delete()
            else:
                self.gejmołwer()
                self.batn()
                self.if_reset()
            self.muzyczka.czhec()
            pygame.display.flip()
            pygame.time.delay(7)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit(0)
                if event.key == pygame.K_r:
                    self.reset_game()
                    self.game = True
            elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:

                self.if_reset()
                self.if_poklik()

                self.if_x_clik()
                self.ifOnOffClik()
    def if_poklik(self):
        m_poz = pygame.mouse.get_pos()

        if self.rect_op.collidepoint(m_poz):
            self.bolrun *= -1
            self.bant_mmenu.blit()

    def jump(self):
        if time.time() - self.jump_clok > 0.01:
            if self.jumping:
                self.smok.pozition_y -= self.vel_y
                self.smok.down_poz_y -= self.vel_y
                self.vel_y -= 1
                if self.vel_y < -14:
                    self.jumping = False
                    self.vel_y = 14
            self.jump_clok = time.time()

    def if_space_clik(self):
        if self.can_jump:
            przycisk = pygame.key.get_pressed()
            if (przycisk[pygame.K_SPACE] or przycisk[pygame.K_UP]) and self.jumping is False:  # jeżeli kliknie spacj
                self.jumping = True  # skakanie się aktywuje
                self.jump()  # skacze
                self.muzyczka.jumpM()

    def helpfull_create_func(self):
        self.czas = time.time()
        self.n1 = 4
        self.n2 = 11
        self.r_n = random.randint(self.n1, self.n2) / 10

    def create_blocks(self):
        if time.time() - self.clok > self.r_n:
            number_distanse = random.randint(150, 300)
            self.rr = random.randint(0, 4)
            if self.rr == 3:
                new_obj = Bird(self.screen)
                self.dist_list.append(number_distanse)
                new_obj.bird_pozx += sum(self.dist_list)
                self.objekts.append(new_obj)

            else:
                new_obj = Obstacle(self.screen)
                self.dist_list.append(number_distanse)
                new_obj.block_1.x += sum(self.dist_list)
                self.objekts.append(new_obj)
            self.clok = time.time()
            self.r_n = random.randint(self.n1, self.n2) / 10

    def rects(self):
        self.rect_op = self.patn_opcje.po_image.get_rect()
        self.rect_list.append(self.rect_op)

        for ahh in self.objekts:
            if type(ahh) == Obstacle:
                self.block_rect = pygame.Rect(ahh.block_1.x, ahh.block_1.y, 30, 30)
                self.rect_list.append(self.block_rect)
            elif type(ahh) == Bird:
                self.block_rect = pygame.Rect(ahh.bird_pozx, ahh.bird_pozy, 41, 26)
                self.rect_list.append(self.block_rect)

    def colid_blocks(self):

        for blok in self.rect_list:
            if self.dinozar_rect.colliderect(blok):
                self.smok.blit_uffdragon()
                self.muzyczka.deathM()
                self.game = False
        # jeśli  blok styknie się ze smokiem

    def reset_list(self):
        self.rect_list = []

    def dragon_type(self):
        if self.jumping:
            self.smok.blit_dragon_up()
            self.dinozar_rect = pygame.Rect(self.smok.pozition_x, self.smok.pozition_y, 55, 62)
        elif pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            self.anime_normal_down()
            self.can_jump = False
            self.dinozar_rect = pygame.Rect(self.smok.pozition_x, self.smok.down_poz_y, 55, 34)
        else:
            self.anime_normal_up()
            self.can_jump = True
            self.dinozar_rect = pygame.Rect(self.smok.pozition_x, self.smok.pozition_y, 55, 62)

    def help_birdfujhuj(self):
        self.czs = time.time()

    def bird_anime(self, ptak):
        self.ptak = ptak
        if time.time() - self.czs > 0.5:
            self.key *= -1
            self.czs = time.time()
        if self.key == -1:
            self.ptak.blit_down()
        else:
            self.ptak.blit_up()

    def clouds_create(self):
        self.crap = 200
        self.chmura = Cloud(self.screen)
        self.chmura.cloud_pozx += self.crap
        self.clouds_list.append(self.chmura)

    def clouds_show(self):
        for hmurka in self.clouds_list:
            hmurka.draw_cloud()

    def clouds(self):
        if self.cloud_key:
            self.clouds_create()
            self.cloud_key = False
        if time.time() - self.chmura_time > 7:
            self.cloud_key = True
            self.chmura_time = time.time()

    def clouds_delete(self):
        for hh in self.clouds_list:
            if hh.cloud_pozx == -100:
                self.clouds_list.remove(hh)

    def anime_normal_up(self):
        if time.time() - self.czss > 0.1:
            self.klucyk *= -1
            self.czss = time.time()
        if self.klucyk == -1:
            self.smok.blit_up_up()
        else:
            self.smok.blit_up_down()

    def anime_normal_down(self):
        if time.time() - self.czss > 0.1:
            self.k *= -1
            self.czss = time.time()
        if self.k == -1:
            self.smok.blit_down_up()
        else:
            self.smok.blit_down_down()

    def reset_game(self):
        self.clouds_list.clear()
        self.reset_list()
        self.dist_list.clear()
        self.objekts.clear()
        self.smok.pozition_y = 538
        self.smok.pozition_x = 200
        self.vel_x = 14
        self.vel_y = 14
        self.smok.down_poz_y = 566

    def if_reset(self):
        p = pygame.mouse.get_pressed()
        if p == (1, 0, 0):
            mouse = pygame.mouse.get_pos()
            print(mouse)
            try:
                if self.hwdp.rect_pp.collidepoint(mouse):
                    self.reset_game()
                    self.game = True
            except AttributeError:
                return None


# todo
# zamień bloki na drzewka
# dodaj dłuższe i mniejsze drzewka
# menu gry( w tym opcje itp..)
# dodaj muzykę
# dodaj skrut na pulpicie do tej gry
# wes kurwa ogarnij ten kod bo jest fatalny, klasa mejn jest tak kurwa przeciążona że to jest jakiś szok


if __name__ == '__main__':
    game = Mejn()
    game.run_mejn()
