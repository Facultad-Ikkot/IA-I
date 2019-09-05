from random import randrange ,seed
import colorPrint


class Environment:
    def __init__(self, sizeX, sizeY, block_rate):
        seed( 24324 )
        self.rendimiento = 0
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

    def accept_action(self, action):
        if (action == "L"):
            if (self.posActY-1 >= 0):
                return True
            else:
                return False
        if (action == "R"):
            if (self.posActY+1 <= self.sizeY-1):
                return True
            else:
                return False
        if (action == "up"):
            if (self.posActX-1 >= 0):
                return True
            else:
                return False
        if (action == "down"):
            if (self.posActX+1 <= self.sizeX-1):
                return True
            else:
                return False

    def is_block(self):
        if (self.map[self.posActX][self.posActY] == 1):
            return True
        else:
            if (self.map[self.posActX][self.posActY] == 0):
                self.map[self.posActX][self.posActY] = 4
            return False

    def pase(self):
        self.map[self.posActX][self.posActY] = 2
        self.rendimiento = self.rendimiento + 1

    def actualizarPos(self, action):
        if (action == "L"):
            self.posActY = self.posActY-1
        elif (action == "R"):
            self.posActY = self.posActY+1
        elif (action == "up"):
            self.posActX = self.posActX-1
        elif (action == "down"):
            self.posActX = self.posActX+1
        else:
            pass

    def get_performance(self):
        print(self.rendimiento)
        return self.rendimiento

    def print_environment(self):
        print("____________________________________________________________________")
        for i in range(0, self.sizeX):
            print("|", end="")
            for j in range(0, self.sizeY):
                if (i == self.posActX and j == self.posActY):
                    print("\033[91m#\033[00m", end="|")
                else:
                    if (self.map[i][j] == 2):
                        colorPrint.prCyan("0")
                    elif (self.map[i][j] == 4):
                        colorPrint.prPurple("0")
                    else:
                        print(self.map[i][j], end="|")
            print("")
        print("____________________________________________________________________")

    def posX(self):
        return self.posActX

    def posY(self):
        return self.posActY