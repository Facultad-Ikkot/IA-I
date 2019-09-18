# https://docs.google.com/document/d/1I-4UuCsW-cr8ttmY0VJ82_s-EDc_nKbG6IoroZT_Uq4/edit

from agentThink import AgentE
from environment import Environment

env1 = Environment(18, 18, 0.3)

agenE = AgentE(env1)
aux = agenE.think(env1)
agenE.printF(env1, aux)


print("______________________________________________________________________________________")
