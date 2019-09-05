from random import randrange ,seed
import colorPrint


class Environment:
    def __init__(self, sizeX, sizeY):
        seed( 24324 )
        self.rendimiento = 0
        self.map = [None] * sizeX
        for i in range(sizeX):
            self.map[i] = [None] * sizeY
        self.sizeX = sizeX
        self.sizeY = sizeY
        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                self.map[i][j] = 0
 

    def is_dirty(self):
        if (self.map[self.posActX][self.posActY] == 1):
            return True
        else:
            if (self.map[self.posActX][self.posActY] == 0):
                self.map[self.posActX][self.posActY] = 4
            return False
 

    def get_performance(self):
        print(self.rendimiento)
        return self.rendimiento

    def print_environment(self):
        print("____________________________________________________________________")
        for i in range(0, self.sizeX):
            print("|", end="")
            for j in range(0, self.sizeY):
                    if (self.map[i][j] == 2):
                        colorPrint.prCyan("0")
                    elif (self.map[i][j] == 4):
                        colorPrint.prPurple("0")
                    else:
                        print(self.map[i][j], end="|")
            print("")
        print("____________________________________________________________________")
