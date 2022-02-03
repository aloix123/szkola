


import pygame.mixer

class Music:
    def __init__(self):
        self.load=pygame.mixer.music.load('muzykaaa/Słoń - [0215] - Czerwony Rum (scratch DJ Flip) Prod. Chris Carson (online-audio-converter.com) (1).wav')
        pygame.mixer.music.play()
        self.uff=pygame.mixer.Sound('muzykaaa/UFF.wav')
    def play_uff(self):
        self.uff.play()