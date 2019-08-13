# https://docs.google.com/document/d/1eP3aCyTWuTCbYMwf3inNHd7AIIpYHyb_PEj-aXYc1xU/edit


from random import randrange

class Environment:

    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):

        self.map = [range(sizeX) for i in range(sizeY)]
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

        if (action == "up"):
            map[i][j-1]
        if (action == "down"):
            map[i][j+1]
            
        if (action == "D"):
            map[i-1][j]
        if (action == "I"):
            map[i+1][j]


        if (i<= self.sizeX and j <= self.sizeY):
            return True
        else:
            return False

    def is_dirty(self):
        if (map[i][j]==1):
            return True
        else:
            return False
    def get_performance(self):
        
        print()
    def print_environment(self):
        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                print(self.map[i][j])



class Agent:           
    def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    def up(self):
        
    def down(self):  
    def left(self):
    def right(self):
    def suck(self): # Limpia
    def idle(self): # no hace nada
    def prespective(self,env): #sensa el entorno si esta sucio y en que pocicion esta 
    def think(self): # implementa las acciones a seguir por el agente
        

x = Environment(10,10,1,1,0.5)
x.print_environment()
