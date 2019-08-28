
from agentThink import AgentConMeoria, AgentAleatorio, AgentSinEstado
from environment import Environment


env1 = Environment(8, 8, 0.4)

agenMem = AgentConMeoria(env1)
agenAlea = AgentAleatorio(env1)
agenSin = AgentSinEstado(env1)

c = 1
while True:
    if(c == 1):
        aux = agenSin.think(env1)
    if(c == 2):
        aux = agenAlea.think(env1)
    if(c == 3):
        aux = agenMem.think(env1)
    if(c == 4):
        aux = agenMem.think2(env1)
    if (aux == True):
        break

print("################################ Final ################################")
env1.print_environment()
env1.get_performance()
