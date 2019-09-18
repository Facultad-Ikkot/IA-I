from random import randrange, seed
from other import *


def generar(size,cantidad):
    cont = 0
    poblacion= []
    fit=[]
    while True:
        vect= crear_vector(size)
        fit = diagonal(vect)
        poblacion.append((fit,vect))
        if (cont == cantidad):
            break
        cont=cont+1
    return (poblacion)
    


def enterecruzar(padre1, padre2):
    cont = 0
    longitud = len(padre1)
    hijo = crear_vector(longitud)
    cantidada = randrange(int(longitud/2)+1)
    pos = randrange(longitud-cantidada)
    print(pos)
    for i in range(0, longitud):
        if(i > pos and cont <= cantidada):
            hijo[i] = padre1[i]
            cont = cont + 1
        else:
            hijo[i] = -1
    for i in range(0, longitud):
        if (hijo[i]==-1):
            while True:
                valor = padre2.pop(0)
                aux = hijo.count(valor)
                if(aux == 0):
                    hijo[i] = valor
                    break
    return hijo


def mutar(individuo):
    longitud = len(individuo)
    pos1 = randrange(longitud)
    pos2 = randrange(longitud)
    aux = individuo[pos1]
    individuo[pos1] = individuo[pos2]
    individuo[pos2] = aux
    return individuo


def printMatriz(matriz):
    for i in range ( 0,len(matriz)):
        print(matriz[i])
        

def diagonal(vector):
    return randrange(len(vector))

def seleccionar(pob):
    new_pob=[]
    for j in range(0,5):
        i = randrange(len(pob))
        new_pob.append(pob[i])
    return new_pob
    
 
size = 8
poblacion=generar(size,10)
printMatriz(poblacion)


while True:
    poblacion = seleccionar(poblacion)
    print("")
    printMatriz(poblacion)
    #aux =  think(size,10)
    #printMatriz(aux)
    break
