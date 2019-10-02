# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed,random
from other import *
import threading
import time
from math import exp


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
    deltaE=enemigosMap-enemigosMapTem;
    if(enemigosMap>enemigosMapTem):
        return True 
    else:
        aux= random()
        h=funcionProbabilidad(contador,deltaE)
        if (aux<h ):
            return True
        else:
            return False 

def funcionProbabilidad(x,delta):
    t = (intentos-x+2)/intentos
    y = exp(delta/t)
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
intentos= 20000
cont2= 0
total=0
timeIn=time.time()
for i in range(0,30):
    mapa = crear_mapa(size)
    cont = 0
    timeInT=time.time()
    while True:
        cont = cont + 1
        mapa = think(size, mapa,cont)
        aux = comprobarReinaFin(size, mapa) 
        if (aux == 0 or cont > intentos):
            #print_map(size, mapa)
            #print(aux)
            timeEnT=time.time()
            print("Estados:", cont,"; time:",timeEnT-timeInT)
            if (aux == 0):
                total=total+cont
                cont2=cont2+1
            break    
timeEn=time.time()
print("-------------------")
print("Resultados correctos:", cont2,"; time final:",timeEn-timeIn)
print("Estados total:",total)


