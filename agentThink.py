from agent import Agent
from random import randrange


class AgentConMeoria(Agent):
    def __init__(self, env):
        Agent.__init__(self, env)

    def think(self, env):
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
        return True

    def think2(self, env):
        if (self.prespective(env)):
            self.suck(env)
        while True:
            if (self.prespectivePosX(env) >= 1):
                self.up(env)
            else:
                if (self.prespectivePosY(env) >= 1):
                    self.left(env)
                else:
                    while True:
                        while True:
                            if (self.prespectivePosY(env) != self.prespectiveSizeY(env)-1):
                                self.right(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break
                        if (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                        while True:
                            if (self.prespectivePosY(env) != 0):
                                self.left(env)
                            else:
                                break
                            if (self.thinkAux(env)):
                                break
                        if (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
                            self.down(env)
                        else:
                            break
                        if (self.thinkAux(env)):
                            break
                    break
            if (self.thinkAux(env)):
                break
        return True


class AgentAleatorio(Agent):
    def __init__(self, env):
        Agent.__init__(self, env)

    def think(self, env):
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
        return self.thinkAux(env)


class AgentSinEstado(Agent):
    def __init__(self, env):
        Agent.__init__(self, env)

    def think(self, env):
        if (self.prespectivePosY(env) != self.prespectiveSizeY(env)-1 and (self.prespectivePosX(env) % 2) == 1):
            self.right(env)
        elif ((self.prespectivePosX(env) == self.prespectiveSizeX(env)-1) and (self.prespectivePosY(env) == self.prespectiveSizeY(env)-1)):
            self.idle()
        elif ((self.prespectivePosX(env) % 2) == 1):
            self.down(env)
        elif (self.prespectivePosY(env) != 0):
            self.left(env)
        elif (self.prespectivePosX(env) != self.prespectiveSizeX(env)-1):
            self.down(env)
        return self.thinkAux(env)

