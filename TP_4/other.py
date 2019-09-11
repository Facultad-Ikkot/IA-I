# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
import colorPrint

def crear_mapa(size):
    map = [None] * size
    for i in range(size):
        map[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size):
            map[i][j] = 0
    for i in range(0, size):
        val = randrange(size)
        map[i][val] = 1
    return map



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


def print_map(size, map):
    print("____________________________________________________________________")
    for i in range(0, size):
        print("|", end="")
        for j in range(0, size):
            if (map[i][j] == 1):
                colorPrint.prCyan("#")
            else:
                print(map[i][j], end="|")
        print("")
    print("____________________________________________________________________")


def print_map2(size, map):
    print("____________________________________________________________________")
    for i in range(0, size):
        print("|", end="")
        for j in range(0, size):
            print(map[i][j], end="|")
        print("")
    print("____________________________________________________________________")


def horizontal(size, mapa, posY):
    cont = 0
    aux = False
    for i in range(0, size):
        if (mapa[i][posY] == 1):
            aux = True
            cont = cont+1
    if (aux == True):
        cont = cont - 1
    return cont


def diagonal_1(size, mapa, posX, posY):
    cont = 0
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX + 1
        posActY = posActY + 1
        if(posActX >= size or posActY >= size):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX - 1
        posActY = posActY - 1
        if(posActX < 0 or posActY < 0):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    return cont


def diagonal_2(size, mapa, posX, posY):
    cont = 0
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX + 1
        posActY = posActY - 1
        if(posActX >= size or posActY < 0):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX - 1
        posActY = posActY + 1
        if(posActX < 0 or posActY >= size):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    return cont


def confrontacion(size, mapa, posX, posY):
    hor = horizontal(size, mapa, posY)
    dig1 = diagonal_1(size, mapa, posX, posY)
    dig2 = diagonal_2(size, mapa, posX, posY)
    aux = dig1 + dig2 + hor
    return aux