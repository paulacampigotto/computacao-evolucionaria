from pprint import pprint
import random

COD = ''
POP = 0
DIM = 0
Li=0
Ui=0

def leitura():
    global COD, POP, DIM, Li, Ui
    with open('entrada.txt', 'r') as f:
        linhas = f.readlines()

    for i in range(len(linhas)):
        aux = linhas[i].split("\n")
        linhas[i] = aux[0]

    COD = linhas[0].split("=")[1]
    POP = (int)(linhas[1].split("=")[1])
    DIM = (int)(linhas[2].split("=")[1])
    Li = (int)((linhas[3].split("=")[1]).split(",")[0].split("[")[1])
    Ui = (int)((linhas[3].split("=")[1]).split(",")[1].split("]")[0])


def popBinaria():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for i in range(DIM):
            cromossomo.append(random.randint(0,1))
        populacao.append(cromossomo)
    return populacao

def popInteira():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for i in range(DIM):
            cromossomo.append(random.randint(Li,Ui))
        populacao.append(cromossomo)
    return populacao

def popInteiraPerm():
    populacao = []
    for i in range(POP):
        vetor = [j for j in range(DIM)]
        cromossomo = []
        for j in range(DIM):
            rand = random.choice(vetor)
            cromossomo.append(rand)
            vetor.remove(rand)
        populacao.append(cromossomo)
    return populacao

def popReal():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for i in range(DIM):
            cromossomo.append(round(random.uniform(Li, Ui), 2))
        populacao.append(cromossomo)
    return populacao


leitura()

if(COD == 'BIN'):
    pprint(popBinaria())
elif(COD == 'INT'):
    pprint(popInteira())
elif(COD == 'REAL'):
    pprint(popReal())
else:
    pprint(popInteiraPerm())
