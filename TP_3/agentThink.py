from agent import Agent
from random import randrange


class AgentConMeoria(Agent):
    def __init__(self, env):
        Agent.__init__(self, env)
    
    def comprobarFrontera(self,env):
        if (env.accept_action("L")):
            if(self.prespective(env)):
                 
        env.accept_action("R")
        env.accept_action("up")
        env.accept_action("down")

        

    def think(self,recorridos,acumulado):
        print("hola")

    def heuristica(self):
        print("hola")
    
    def distanciaOjetivo(self):
        None

    
        


    

