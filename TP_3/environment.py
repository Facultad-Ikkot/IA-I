from random import randrange, seed
import colorPrint


class Environment:
    def __init__(self, sizeX, sizeY, block_rate):
        seed(2124324)
        self.rendimiento = 0
        self.functionH = 0
        self.posInitX = randrange(sizeX)
        self.posInitY = randrange(sizeY)
        self.posEndX = randrange(sizeX)
        self.posEndY = randrange(sizeY)
        self.posActX = self.posInitX
        self.posActY = self.posInitY
        self.map = [None] * sizeX
        for i in range(sizeX):
            self.map[i] = [None] * sizeY
        self.sizeX = sizeX
        self.sizeY = sizeY
        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                aux = randrange(100)
                if (aux < (block_rate*100)):
                    self.map[i][j] = 1
                else:
                    self.map[i][j] = 0
                if (self.posInitX == i and self.posInitY == j):
                    self.map[i][j] = 4
                if (self.posEndX == i and self.posEndY == j):
                    self.map[i][j] = 5

    def accept_action(self, posActXTem, posActYTem):
        if ((posActYTem >= 0) and (posActYTem <= self.sizeY-1) and (posActXTem >= 0) and (posActXTem <= self.sizeX-1)):
            if (self.is_block(posActXTem, posActYTem)):
                return False
            else:
                return True
        else:
            return False

    def is_block(self, posActXTem, posActYTem):
        if (self.map[posActXTem][posActYTem] == 1):
            return True
        else:
            return False

    def functioH(self, posActXTem, posActYTem):
        costX = abs(posActXTem-self.posEndX)
        costY = abs(posActYTem-self.posEndY)
        costT = costX + costY
        return costT

    def print_environment(self, posActXTem, posActYTem):
        print("____________________________________________________________________")
        for i in range(0, self.sizeX):
            print("|", end="")
            for j in range(0, self.sizeY):
                if (i == posActXTem and j == posActYTem):
                    print("\033[91m#\033[00m", end="|")
                else:
                    if (self.map[i][j] == 1):
                        colorPrint.prCyan("/")
                    elif (self.map[i][j] == 4):
                        colorPrint.prPurple("S")
                    elif (self.map[i][j] == 5):
                        colorPrint.prPurple("E")
                    else:
                        print(self.map[i][j], end="|")
            print("")
        print("____________________________________________________________________")
