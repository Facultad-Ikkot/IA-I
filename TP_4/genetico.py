from random import randrange, seed
from other import *


def generar(size, cantidad):
    cont = 0
    poblacion = []
    fit = []
    while True:
        vect = crear_vector(size)
        fit = confrontacionF(vect)
        poblacion.append((fit, vect))
        if (cont == cantidad):
            break
        cont = cont+1
    return (poblacion)


def diagonal(reina1, reina2):
    costX = abs(reina1[0]-reina2[0])
    costY = abs(reina1[1]-reina2[1])
    if (costX==costY):
        return True
    else:
        return False

def confrontacionF(vec):
    cont=0
    for i in range (0,len(vec)-1):
        aux=(i,vec[i])
        for j in range(i+1,len(vec)):
            aux2=(j,vec[j])
            if (diagonal(aux,aux2)):
                cont=cont+1
    return cont


def enterecruzar(padre1, padre2Tem):
    cont = 0
    longitud = len(padre1)
    hijo = crear_vector(longitud)
    cantidada = randrange(int(longitud/2)+1)
    pos = randrange(longitud-cantidada)
    for i in range(0, longitud):
        if(i > pos and cont <= cantidada):
            hijo[i] = padre1[i]
            cont = cont + 1
        else:
            hijo[i] = -1
    padre2=padre2Tem.copy()        
    for i in range(0, longitud):
        if (hijo[i] == -1):
            while True:
                valor = padre2.pop(0)
                aux = hijo.count(valor)
                if(aux == 0):
                    hijo[i] = valor
                    break
    fit = confrontacionF(hijo)
    return (fit,hijo)


def mutar(individuo):
    longitud = len(individuo)
    pos1 = randrange(longitud)
    pos2 = randrange(longitud)
    aux = individuo[pos1]
    individuo[pos1] = individuo[pos2]
    individuo[pos2] = aux
    fit = confrontacionF(individuo)
    return (fit,individuo)


def printMatriz(matriz):
    for i in range(0, len(matriz)):
        print(matriz[i])
    print("________________________________")


def seleccionar(pob):
    new_pob = []
    for j in range(0, sizeH):
        i = randrange(len(pob))
        new_pob.append(pob[i])
    return new_pob

def think(poblacionTem):
    poblacionAct = seleccionar(poblacionTem)
    for i in range(0,sizeH):
        ran1=randrange(sizeH)
        ran2=randrange(sizeH)
        hijo=enterecruzar(poblacionAct[ran1][1],poblacionAct[ran2][1])
        poblacionAct.append(hijo)
    for i in range(0,mut):
        ran1=randrange(sizeH)
        aux=poblacionAct[ran1]
        poblacionAct.remove(aux)
        hijo=mutar(aux[1])
        poblacionAct.append(hijo)
    return poblacionAct

def minFit(pobl):
    minFi=100000000000000000000
    for ele in pobl:
        if (ele[0]<minFi):
            minFi=ele[0]
    return minFi


size = 10
poblacion = generar(size, 10)
printMatriz(poblacion)
sizeH= 5
mut=1 


while True:
    poblacion= think(poblacion)
    if (minFit(poblacion)==0):
        printMatriz(poblacion)
        break

