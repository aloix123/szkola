import  pygame.mixer

class M:
    def __init__(self):
        pygame.init()
        self.music=pygame.mixer.music.load('muzyka/C418-Sweden-Minecraft-Volume-Alpha.wav')
        self.jump_muzic=pygame.mixer.Sound('muzyka/8bit-jump.wav')
        self.jump_muzic.set_volume(0.20)
        self.death_muzic=pygame.mixer.Sound("muzyka/8-bit-video-game-death-sound-effect.wav")
        self.death_muzic.set_volume(0.20)
        pygame.mixer.music.set_volume(11)
        pygame.mixer.music.play()

    def czhec(self):
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
    def jumpM(self):
        self.jump_muzic.play()
    def deathM(self):
        self.death_muzic.play()