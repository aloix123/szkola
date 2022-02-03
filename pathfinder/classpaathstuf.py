

class Distance:
    def calkdistance(self,r1,r2):
        self.r1=r1
        self.r2=r2
        print(abs(self.r1.x-self.r2.x)+abs(self.r1-self.r2))
        return abs(self.r1.x-self.r2.x)+abs(self.r1-self.r2)