class Parameters:
    def __init__(self):
        self.screen_hight = 1500 #980
        self.screen_width = 882#882
        self.screen_color = (0, 255, 255)
        self.square_hw = 20
        self.szary = (64, 64, 64)
        self.jasnoszary=(192,192,192)
        self.ciemjasnoszary=(172,172,190)
        self.biały=(255,255,255)
        self.oreng=(255,120,17)
        self.yellow=(238,231,50)
        self.jasnyblu=(153,255,255)
        self.g_paska = 2
        self.black=(0,0,0)
        self.square_count = 45
        self.lewy=(1,0,0)
    def getsquarehw(self):
        return self.square_hw

    def getjasnoszary(self):
        return self.jasnoszary
    def getszary(self):
        return self.szary
    def getoreng(self):
        return self.oreng
    def getjasnyblu(self):
        return self.jasnyblu
    def getyellow(self):
        return self.yellow
    def getblack(self):
        return self.black

