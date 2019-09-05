# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
import colorPrint


#seed(121)
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
            if (map[i][j] == 0):
                colorPrint.prCyan("0")
            else:
                print(map[i][j], end="|")
        print("")
    print("____________________________________________________________________")


def horizontal(size, mapa, posY):
    cont = 0
    for i in range(0, size):
        if (mapa[i][posY] == 1):
            cont = cont+1
    return cont


def vertical(size, mapa, posX):
    cont = 0
    for i in range(0, size):
        if (mapa[posX][i] == 1):
            cont = cont+1
    return cont


def diagonal_1(size, mapa, posX, posY):
    cont = 0
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX + 1
        posActY = posActY + 1
        if(posActX >= size-1 or posActY >= size-1):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX - 1
        posActY = posActY - 1
        if(posActX <= 0 or posActY <= 0):
            break
        if (mapa[posActX][posActY] == 1):
            cont = cont+1
    return cont


def diagonal_2(size, map, posX, posY):
    cont = 0
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX + 1
        posActY = posActY - 1
        if(posActX >= size or posActY <= 0):
            break
        if (map[posActX][posActY] == 1):
            cont = cont+1
    posActX = posX
    posActY = posY
    while True:
        posActX = posActX - 1
        posActY = posActY + 1
        if(posActX <= 0 or posActY >= size):
            break
        if (map[posActX][posActY] == 1):
            cont = cont+1
    return cont


def confrontacion(size, mapa, posX, posY):
    hor = horizontal(size, mapa, posY)
    ver = vertical(size, mapa, posX)
    dig1 = diagonal_1(size, mapa, posX, posY)
    dig2 = diagonal_2(size, mapa, posX, posY)
    aux = hor+ver+dig1+dig2
    return aux


def matrizEne(size, mapa):
    mapaF = [None] * size
    for i in range(size):
        mapaF[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size):
            mapaF[i][j] = confrontacion(size, mapa, i, j)
    return mapaF

def minimo(size,mapa):
    minimo=mapa[0][0]
    actX=0
    actY=0
    for i in range(0,size):
        for j in range(0,size):
            if (mapa[i][j] < minimo):
                minimo=mapa[i][j]
                actX=i
                actY=j
    print(minimo,"h",actX,actY)
    return (actX,actY)

def buscar_reina(size,mapa,posY):
    for i in range(0,size):
        print(mapa[posY][i])
        if (mapa[posY][i]==1):
            break
    return i

def comprobarReina(size,mapa):
    aux=0
    for i in range(0,size):
        for j in range(0,size):
            if (mapa[i][j]==1):
                aux= aux +confrontacion(size,mapa,i,j)
    return aux


def think(size,mapa):
    mapaEn=matrizEne(size, mapa)
    print_map2(size, mapaEn)
    (actX,actY)=minimo(size,mapaEn)
    i=buscar_reina(size,mapa,actX)
    print(actX,actY,i)
    mapa[actX][i] = 0
    mapa[actX][actY]=1
    print_map(size,mapa)
    return mapa





size = 6
mapa = crear_mapa(size)

print_map(size, mapa)
while True:
    mapa = think(size,mapa)
    print(comprobarReina(size,mapa))


