# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
from other import *



def evaluacion(size, mapa):
    i = randrange(size)
    j = randrange(size)
    if (mapa[i][j] == 0):
        return (i, j)
    else:
        return evaluacion(size,mapa)

def probabilidad(mapa,mapaTem,contador):
    enemigosMap=comprobarReinaFin(size, mapa)
    enemigosMapTem=comprobarReinaFin(size, mapaTem)
    if(enemigosMap>enemigosMapTem):
        return True 
    else:
        aux= randrange(100)
        if (aux<funcionProbabilidad(contador)):
            return True
        else:
            return False 

def funcionProbabilidad(x):
    y = (10000-x)/100
    return y

def buscar_reina(size, mapa, posY):
    for i in range(0, size):
        if (mapa[posY][i] == 1):
            break
    return i


def comprobarReinaFin(size, mapa):
    aux = 0
    for i in range(0, size):
        for j in range(0, size):
            if (mapa[i][j] == 1):
                aux = aux + confrontacion(size, mapa, i, j)
    return aux


def think(size, mapa,contador):
    (actX, actY) = evaluacion(size, mapa)
    mapTem = copiarMatriz(size, mapa, actX)
    i = buscar_reina(size, mapa, actX)
    mapTem[actX][i] = 0
    mapTem[actX][actY] = 1
    if (probabilidad(mapa,mapTem,contador)):
        return mapTem
    else:
        return mapa

size = 8
cont2= 0
for i in range(0,100):
    mapa = crear_mapa(size)
    cont = 0
    while True:
        cont = cont + 1
        mapa = think(size, mapa,cont)
        aux = comprobarReinaFin(size, mapa) 
        if (aux == 0 or cont > 10000):
            #print(cont)
            #print_map(size, mapa)
            #print(aux)
            if (aux == 0):
                cont2=cont2+1
            break  
        
print(cont2)

