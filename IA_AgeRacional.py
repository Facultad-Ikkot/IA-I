# https://docs.google.com/document/d/1eP3aCyTWuTCbYMwf3inNHd7AIIpYHyb_PEj-aXYc1xU/edit


from random import randrange
import time

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

    def accept_action(self, action):  # si la accion que va a realizar es valida , up down , I ,D  
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
        if (self.map[self.posActX][self.posActY]==1):
            return True
        else:
            return False

    def clean(self):
        self.map[self.posActX][self.posActY]=0
        self.rendimiento = self.rendimiento +1

    def actualizarPos(self,x,y):
        self.posActX = x
        self.posActY = y

    def get_performance(self):
        print(self.rendimiento)
        return self.rendimiento

    def print_environment(self):
        print("-----------------------------")
        for i in range(0, self.sizeX):
            print("|",end="")
            for j in range(0, self.sizeY):
                if (i== self.posActX and j == self.posActY):
                    print("#",end="|")
                else:
                    print(self.map[i][j],end="|")
            print("")

#####################################################################
class Agent:
    sleepTime = 0.1           
    def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
        self.posX = env.posInitX
        self.posY = env.posInitY
        self.sizeX = env.sizeX
        self.sizeY = env.sizeY
        self.periodo = 1000
        
    def left(self,env):
        self.posY = self.posY-1
        self.periodo = self.periodo -1
        env.actualizarPos(self.posX,self.posY)

    def right(self,env):
        self.posY = self.posY+1  
        self.periodo = self.periodo -1
        env.actualizarPos(self.posX,self.posY)
         
    def up(self,env):
        self.posX = self.posX-1
        self.periodo = self.periodo -1
        env.actualizarPos(self.posX,self.posY)

    def down(self,env):
        self.posX = self.posX+1
        self.periodo = self.periodo -1
        env.actualizarPos(self.posX,self.posY)
        
    def suck(self,env): # Limpia
        env.clean()
        self.periodo = self.periodo -1
        
    def idle(self): # no hace nada
        print("Nada")

    def prespective(self,env): #sensa el entorno si esta sucio y en que pocicion esta 
        if (env.is_dirty()):
            print("Esta sucio")
            return True
        else:
            print("Esta limpio")
            return False

    def think(self,env): # implementa las acciones a seguir por el agente
        while True:
            if (self.prespective(env)):
                self.suck(env)
            if (env.accept_action("up")):
                self.up(env)
            else:
                if (env.accept_action("L")):
                    self.left(env)
                else:
                    while True:
                        while True:
                            if (self.periodo<0):
                                break
                            env.print_environment()
                            time.sleep(self.sleepTime)
                            if (self.prespective(env)):
                                self.suck(env)
                            if (env.accept_action("R")):
                                self.right(env)
                            else:
                                break
                        if (self.periodo<0):
                            break    
                        env.print_environment()
                        time.sleep(self.sleepTime)
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break   

                        while True:
                            if (self.periodo<0):
                                break
                            env.print_environment()
                            time.sleep(self.sleepTime)
                            if (self.prespective(env)):
                                self.suck(env)
                            if (env.accept_action("L")):
                                self.left(env)
                            else:
                                break  
                        if (self.periodo<0):
                            break
                        env.print_environment()
                        time.sleep(self.sleepTime)
                        if (env.accept_action("down")):
                            self.down(env)
                        else:
                            break 
                        if (self.periodo<0):
                            break
            env.print_environment()
            time.sleep(self.sleepTime)
            if (self.periodo<0):
                break



env1 = Environment(30,30,0.5)
A= Agent(env1)

A.think(env1)
print("############## Final ################")
env1.print_environment()
env1.get_performance()

