from agent import Agent
from random import randrange
import time


class AgentE(Agent):
    def __init__(self, env):
        Agent.__init__(self, env)
        self.poblacion = []
        self.poblacionRe = []
        self.cont = 0

    def comprobarFrontera(self, env, posActXTem, posActYTem):
        state = False
        if (env.accept_action(posActXTem+1, posActYTem)):
            aux = env.functioH(posActXTem+1, posActYTem)
            item = ((posActXTem+1, posActYTem), aux)
            if (self.poblacionRe.count(item) == 0):
                state = True
                self.poblacion.append(item)
        if (env.accept_action(posActXTem-1, posActYTem)):
            aux = env.functioH(posActXTem-1, posActYTem)
            item = ((posActXTem-1, posActYTem), aux)
            if (self.poblacionRe.count(item) == 0):
                state = True
                self.poblacion.append(item)
        if (env.accept_action(posActXTem, posActYTem+1)):
            aux = env.functioH(posActXTem, posActYTem+1)
            item = ((posActXTem, posActYTem+1), aux)
            if (self.poblacionRe.count(item) == 0):
                state = True
                self.poblacion.append(item)
        if (env.accept_action(posActXTem, posActYTem-1)):
            aux = env.functioH(posActXTem, posActYTem-1)
            item = ((posActXTem, posActYTem-1), aux)
            if (self.poblacionRe.count(item) == 0):
                state = True
                self.poblacion.append(item)
        return state

    def seleccionar(self):
        mini = 10000000000000
        for unity in self.poblacion:
            if (mini >= unity[1]):
                mini = unity[1]
                minEl = unity
        self.poblacion.remove(minEl)
        self.poblacionRe.append(minEl)
        return minEl

    def think(self, env):
        self.cont = 0
        aux = env.functioH(env.posInitX, env.posInitY)
        self.poblacionRe.append(((env.posInitX, env.posInitY), aux))
        self.comprobarFrontera(env, env.posInitX, env.posInitY)
        if (len(self.poblacion) > 0):
            poblacionFin = []
            return self.think2(env, poblacionFin)
        else:
            print("Sin resultado")
            return []

    def think2(self, env, poblacionFin):
        self.cont = self.cont+1
        ((posX, posY), costH) = self.seleccionar()
        if (not self.comprobarFrontera(env, posX, posY)):
            return []
        if (len(self.poblacion) == 0):
            print("Sin resultado")
            return []
        poblacionFin.append((posX, posY))
        if (costH == 0):
            print("Resultado")
            return poblacionFin
        return self.think2(env, poblacionFin)

    def printF(self, env, pob):
        print(self.cont)
        env.print_environment(env.posInitX, env.posInitY)
        for unity in pob:
            time.sleep(0.6)
            env.print_environment(unity[0], unity[1])

    def getPoblacion(self):
        return self.poblacion
