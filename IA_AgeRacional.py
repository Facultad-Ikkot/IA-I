# https://docs.google.com/document/d/1eP3aCyTWuTCbYMwf3inNHd7AIIpYHyb_PEj-aXYc1xU/edit

from random import randrange
import time
import colorPrint


class Environment:

    def __init__(self, sizeX, sizeY, dirt_rate):
        self.rendimiento = 0
        self.posInitX = randrange(sizeX)
        self.posInitY = randrange(sizeY)
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
                if (aux < (dirt_rate*100)):
                    self.map[i][j] = 1
                else:
                    self.map[i][j] = 0

    # si la accion que va a realizar es valida , up down , I ,D
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

    def is_dirty(self):
        if (self.map[self.posActX][self.posActY] == 1):
            return True
        else:
            if (self.map[self.posActX][self.posActY] == 0):
                self.map[self.posActX][self.posActY] = 4
            return False

    def clean(self):
        self.map[self.posActX][self.posActY] = 2
        self.rendimiento = self.rendimiento + 1

    def actualizarPos(self, x, y):
        self.posActX = x
        self.posActY = y

    def get_performance(self):
        print(self.rendimiento)
        return self.rendimiento

    def print_environment(self):
        print("____________________________________________________________________")
        for i in range(0, self.sizeX):
            print("|", end="")
            for j in range(0, self.sizeY):
                if (i == self.posActX and j == self.posActY):
                    print("\033[91m#\033[00m" , end="|") 
                else:
                    if (self.map[i][j] == 2):
                        colorPrint.prCyan("0")
                    elif (self.map[i][j] == 4):
                        colorPrint.prPurple("0")
                    else:
                        print(self.map[i][j], end="|")
            print("")
        print("____________________________________________________________________")
   
        
######################################################################################

class Agent:
    sleepTime = 0.6
    def __init__(self, env):  # recibe como parámetro un objeto de la clase Environment
        self.posX = env.posInitX
        self.posY = env.posInitY
        self.sizeX = env.sizeX
        self.sizeY = env.sizeY
        self.periodo = 1000

    def left(self, env):
        self.posY = self.posY-1
        self.periodo = self.periodo - 1
        env.actualizarPos(self.posX, self.posY)

    def right(self, env):
        self.posY = self.posY+1
        self.periodo = self.periodo - 1
        env.actualizarPos(self.posX, self.posY)

    def up(self, env):
        self.posX = self.posX-1
        self.periodo = self.periodo - 1
        env.actualizarPos(self.posX, self.posY)

    def down(self, env):
        self.posX = self.posX+1
        self.periodo = self.periodo - 1
        env.actualizarPos(self.posX, self.posY)

    def suck(self, env):  # Limpia
        env.clean()
        self.periodo = self.periodo - 1

    def idle(self):  # no hace nada
        print("Nada")

    def prespective(self, env):  # sensa el entorno si esta sucio y en que pocicion esta
        if (env.is_dirty()):
            return True
        else:
            return False

    def think(self, env):  # implementa las acciones a seguir por el agente
        if (self.prespective(env)):
            self.suck(env)
        while True:
            if (env.accept_action("up")):
                self.up(env)
            else:
                if (env.accept_action("L")):
                    self.left(env)
                else:
                    while True:
                        while True:
                            if (env.accept_action("R")):
                                self.right(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                        while True:
                            if (env.accept_action("L")):
                                self.left(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break                    
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                    break
            if (self.thinkAux(env)):
                break

    def thinkAux(self,env):
        if (self.prespective(env)):
            self.suck(env)
        env.print_environment()
        time.sleep(self.sleepTime)
        if (self.periodo < 0):
            return True 
        else:
            return False

    def thinkAleatorio(self, env):
        while True:
            aux = randrange(4)
            if (aux == 0):
                if (env.accept_action("up")):
                    self.up(env)
            if (aux == 1):
                if (env.accept_action("down")):
                    self.down(env)
            if (aux == 2):
                if (env.accept_action("R")):
                    self.right(env)
            if (aux == 3):
                if (env.accept_action("L")):
                    self.left(env)
            if (self.thinkAux(env)):
                break



        
######################################################################################
######################################################################################

env1 = Environment(5, 5, 0.4)
A = Agent(env1)

#A.thinkAleatorio(env1)
A.think(env1)


print("################################ Final ################################")
env1.print_environment()
env1.get_performance()
