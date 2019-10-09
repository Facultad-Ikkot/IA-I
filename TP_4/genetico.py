from random import randrange, seed
from other import *
import time
import csv

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
    if (costX == costY):
        return True
    else:
        return False


def confrontacionF(vec):
    cont = 0
    for i in range(0, len(vec)-1):
        aux = (i, vec[i])
        for j in range(i+1, len(vec)):
            aux2 = (j, vec[j])
            if (diagonal(aux, aux2)):
                cont = cont+1
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
    padre2 = padre2Tem.copy()
    for i in range(0, longitud):
        if (hijo[i] == -1):
            while True:
                valor = padre2.pop(0)
                aux = hijo.count(valor)
                if(aux == 0):
                    hijo[i] = valor
                    break
    fit = confrontacionF(hijo)
    return (fit, hijo)


def mutar(individuo):
    longitud = len(individuo)
    pos1 = randrange(longitud)
    pos2 = randrange(longitud)
    aux = individuo[pos1]
    individuo[pos1] = individuo[pos2]
    individuo[pos2] = aux
    fit = confrontacionF(individuo)
    return (fit, individuo)


def printMatriz(matriz):
    for i in range(0, len(matriz)):
        print(matriz[i])
    print("________________________________")


def print_environment(self, posActXTem, posActYTem):
    print("____________________________________________________________________")
    for i in range(0, self.sizeX):
        print("|", end="")
        for j in range(0, self.sizeY):
            if (i == posActXTem and j == posActYTem):
                print("\033[91m#\033[00m", end="|")
            else:
                if (self.map[i][j] == 1):
                    colorPrint.prCyan("/")
                elif (self.map[i][j] == 4):
                    colorPrint.prPurple("S")
                elif (self.map[i][j] == 5):
                    colorPrint.prPurple("E")
                else:
                    print(self.map[i][j], end="|")
        print("")
    print("____________________________________________________________________")


def printMatrizVec(vec):
    si = len(vec)
    print("____________________________________________________________________")
    for i in range(0, si):
        print("|", end="")
        for j in range(0, si):
            if (i == vec[j]):
                print("\033[91m#\033[00m", end="|")
            else:
                print("0", end="|")
        print("")
    print("____________________________________________________________________")


def seleccionar(pob):
    new_pob = []
    for j in range(0, sizeH):
        i = randrange(len(pob))
        new_pob.append(pob[i])
    return new_pob


def think(poblacionTem):
    poblacionAct = seleccionar(poblacionTem)
    for i in range(0, sizeH):
        ran1 = randrange(sizeH)
        ran2 = randrange(sizeH)
        hijo = enterecruzar(poblacionAct[ran1][1], poblacionAct[ran2][1])
        poblacionAct.append(hijo)
    for i in range(0, mut):
        ran1 = randrange(sizeH)
        aux = poblacionAct[ran1]
        poblacionAct.remove(aux)
        hijo = mutar(aux[1])
        poblacionAct.append(hijo)
    return poblacionAct


def minFit(pobl):
    minFi = 1000000000000000000
    for ele in pobl:
        if (ele[0] < minFi):
            minFi = ele[0]
            minEl = ele[1]
    return (minFi, minEl)


def genetico():
    state = False
    for j in range(0,2000):
        contTot= contTot +1
        poblacion = think(poblacion)
        (minF, eleF) = minFit(poblacion)
        if (minF == 0):
            state=True
            print(eleF)
            break
    return state


size = 15
poblacionSize = 200
poblacion = generar(size, poblacionSize)
sizeH = poblacionSize//2
mut = poblacionSize//100
resultados = 0
contTot=0
timeIn=time.time()
listaEl = []
listaT = []
for i in range(0,30):
    poblacion = generar(size, poblacionSize)
    state = False
    timeInT=time.time()
    print(i)
    for j in range(0,4000):
        contTot= contTot +1;
        poblacion = think(poblacion)
        (minF, eleF) = minFit(poblacion)
        timeEnT=time.time()
        if (minF == 0):
            state=True
            #printMatriz(poblacion)
            #print(eleF)
            
            #print(j)

            #print(timeEnT-timeInT)
            #printMatrizVec(eleF)
            break
    if (state==True):
        resultados = resultados +1
    listaEl.append((j,timeEnT-timeInT))
 


print("---------------------------------------")
timeEn=time.time()

print("Resultados correctos:", resultados,"; time final:",timeEn-timeIn)
print("Estados total:",contTot)

print(listaEl)
print("---------------------------------------")
for i in range(0,30):
    print(listaEl[i][0])

print("---------------------------------------")
for i in range(0,30):
    print(listaEl[i][1])

