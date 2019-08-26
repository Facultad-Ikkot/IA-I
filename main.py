
from agentes import *

######################################################################################
######################################################################################

env1 = Environment(8, 8, 0.4)

agenMem = AgentConMeoria(env1)
agenAlea = AgentAleatorio(env1)
agenSin = AgentSinEstado(env1)


while True:
    #aux=agenSin.thinkSinMem(env1)
    #aux=agenAlea.thinkAleatorio(env1)
    aux=agenMem.think(env1)
    #aux=agenMem.think2(env1)
    if (aux == True):
        break


print("################################ Final ################################")
env1.print_environment()
env1.get_performance()