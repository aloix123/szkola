import time,pygame.mixer

"""""klasa , gdzie jest przechowywana muzyczka na starcie """""
class sound_music:
    def __init__(self):
        pygame.mixer.init()
        self.background_music=pygame.mixer.music.load('Cartoon - Why We Lose (feat. Coleman Trapp) [NCS Release] (online-audio-converter.com).wav')
        pygame.mixer.music.play()
        self.f = pygame.mixer.Sound('UFF.wav')
        time.sleep(1)
    def run_UFF(self):
        self.f.play()
        time.sleep(1)
    def background_setmusic(self):
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.play()