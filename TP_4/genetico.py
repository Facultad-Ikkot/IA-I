from random import randrange, seed
from other import *


def think():

    None


def enterecruzar(padre1,padre2):
    
    cont=0
    longitud= len(padre1)
    hijo = crear_vector(longitud)
    pos = randrange(longitud)
    cantidada = randrange(int(longitud/2)+1)
    for i in range(0,longitud):
        comt= cont +1
        if(i<pos and cont <=cantidad):
            hijo[i] = padre1[i]
        else:
            hijo[i] = -1
    for j in range(0,longitud):
        if (hijo[j]==-1):
            hijo[j]= padre1[j]
        else:
            pass

    return hijo

        





size = 8
padre1 = crear_vector(size)
padre2 = crear_vector(size)
hijo=enterecruzar(padre1,padre2)

while True:

    think()
    break
