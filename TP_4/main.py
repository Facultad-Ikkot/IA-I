# https://docs.google.com/document/d/1Ocz9ZmOkIiVV7kgDguH99cpOWDKuxoKF6hwgtIv_NNQ/edit

from random import randrange, seed
import colorPrint


#seed(12313)
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
    aux = False
    for i in range(0, size):
        if (mapa[i][posY] == 1):
            aux = True
            cont = cont+1
    if (aux == True):
        cont = cont -1
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


def confrontacion(size, mapa, posX, posY, reina):
    hor = horizontal(size, mapa, posY)
    dig1 = diagonal_1(size, mapa, posX, posY)
    dig2 = diagonal_2(size, mapa, posX, posY)
    aux = dig1 + dig2+hor
    return aux


def matrizEne(size, mapa):
    mapaF = [None] * size
    for i in range(size):
        mapaF[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size):
            if (mapa[i][j] == 1):
                mapaF[i][j] = confrontacion(size, mapa, i, j, True)
            else:
                mapaF[i][j] = confrontacion(size, mapa, i, j, False)
    return mapaF


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


def comprobarReina(size, mapa,val):
    aux = 0
    for i in range(0, size):
        aux2 = False
        for j in range(0, size):
            if (val == j):
                aux2 = True
                aux = aux + confrontacion(size, mapa, i, j, True)
            elif (mapa[i][j] == 1 and aux2 == False):
                aux = aux + confrontacion(size, mapa, i, j, True)
    return aux

def comprobarReinaFin(size, mapa):
    aux = 0
    for i in range(0, size):
        for j in range(0, size):
            if (mapa[i][j] == 1):
                aux = aux + confrontacion(size, mapa, i, j, True)
    return aux


def reinaAmenaza(size, mapa):
    mapaF = [None] * size
    for i in range(size):
        mapaF[i] = [None] * size
    for i in range(0, size):
        for j in range(0, size): 
            mapTem= copiarMatriz(size,mapa,i)
            mapTem[i][j] = 1
            mapaF[i][j] = comprobarReina(size, mapTem,j)
            if (mapa[i][j]==1):
                mapaF[i][j] = 100

            
    return mapaF

def copiarMatriz(size,mapa,val):
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
    print_map2(size, mapaEn)
    (actX, actY) = minimo(size, mapaEn)
    i = buscar_reina(size, mapa, actX)
    print("coord", actX, actY, i)
    mapa[actX][i] = 0
    mapa[actX][actY] = 1
    print_map(size, mapa)
    return mapa


size = 6
mapa = crear_mapa(size)

print_map(size, mapa)
cont=0

while True:
    cont = cont +1
    mapa = think(size,mapa)
    aux = comprobarReinaFin(size,mapa)
    print(aux)
    
    if (aux == 0 or cont > 10000):
        break
