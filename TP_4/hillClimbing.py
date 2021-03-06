# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
from other import *
import time 



def minimo(size, mapa):
    minimo = mapa[0][0]
    actX = 0
    actY = 0
    i = randrange(size)
    for j in range(0, size):
        if (mapa[i][j] <= minimo):
            minimo = mapa[i][j]
            actX = i
            actY = j
    return (actX, actY)


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


def reinaAmenaza(size, mapa):
    mapaF = [None] * size
    for i in range(size):
        mapaF[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size):
            mapTem = copiarMatriz(size, mapa, i)
            mapTem[i][j] = 1
            mapaF[i][j] = comprobarReinaFin(size, mapTem)
            if (mapa[i][j] == 1):
                mapaF[i][j] = size*size*size
    return mapaF



def think(size, mapa):
    mapaEn = reinaAmenaza(size, mapa)
    (actX, actY) = minimo(size, mapaEn)
    i = buscar_reina(size, mapa, actX)
    mapa[actX][i] = 0
    mapa[actX][actY] = 1
    return mapa

size = 15
cont2= 0
total=0
timeIn=time.time()
listaEl = []
print(size)
for i in range(0,30):
    timeInT=time.time()
    mapa = crear_mapa(size)
    cont = 0
    print(i)
    while True:
        cont = cont + 1
        mapa = think(size, mapa)
        aux = comprobarReinaFin(size, mapa) 
        if (aux == 0 or cont > 5000):
            #print_map(size, mapa)
            timeEnT=time.time()
            listaEl.append((cont,timeEnT-timeInT))
            print(cont)
            if (aux == 0):
                total=total+cont
                cont2=cont2+1
                break
            break  
timeEn=time.time()

print("-------------------")
print("Resultados correctos:", cont2,"; time final:",timeEn-timeIn)
print("Estados total:",total)


print("---------------------------------------")
for i in range(0,30):
    print(listaEl[i][0])

print("---------------------------------------")
for i in range(0,30):
    print(listaEl[i][1])


