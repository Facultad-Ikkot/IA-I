# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
from other import *

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


def copiarMatriz(size, mapa, val):
    mapaF = [None] * size
    for i in range(size):
        mapaF[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size):
            if (i == val):
                mapaF[i][j] = 0
            else:
                mapaF[i][j] = mapa[i][j]
    return mapaF


def think(size, mapa):
    mapaEn = reinaAmenaza(size, mapa)
    (actX, actY) = minimo(size, mapaEn)
    i = buscar_reina(size, mapa, actX)
    mapa[actX][i] = 0
    mapa[actX][actY] = 1
    return mapa


size = 6
mapa = crear_mapa(size)
cont = 0

while True:
    cont = cont + 1
    mapa = think(size, mapa)
    aux = comprobarReinaFin(size, mapa) 
    if (aux == 0 or cont > 1000):
        print(cont)
        print_map(size, mapa)
        print(aux)
        break
