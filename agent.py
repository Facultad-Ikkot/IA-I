import time

class Agent:
    sleepTime = 0.5

    def __init__(self, env):
        self.periodo = 10000

    def left(self, env):
        self.periodo = self.periodo - 1
        env.actualizarPos("L")

    def right(self, env):
        self.periodo = self.periodo - 1
        env.actualizarPos("R")

    def up(self, env):
        self.periodo = self.periodo - 1
        env.actualizarPos("up")

    def down(self, env):
        self.periodo = self.periodo - 1
        env.actualizarPos("down")

    def suck(self, env):
        env.clean()
        self.periodo = self.periodo - 1

    def idle(self):
        print("Nada")

    def prespective(self, env):
        if (env.is_dirty()):
            return True
        else:
            return False

    def prespectivePosX(self, env):
        return env.posActX

    def prespectivePosY(self, env):
        return env.posActY

    def prespectiveSizeX(self, env):
        return env.sizeX

    def prespectiveSizeY(self, env):
        return env.sizeY

    def thinkAux(self, env):
        if (self.prespective(env)):
            self.suck(env)
        env.print_environment()
        time.sleep(self.sleepTime)
        if (self.periodo < 0):
            return True
        else:
            return False
