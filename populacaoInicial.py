import random
import sys

POP = 10
DIM = 10

DOMINIO_INFERIOR_INT = -5
DOMINIO_SUPERIOR_INT = 10

DOMINIO_INFERIOR_FLOAT = -10
DOMINIO_SUPERIOR_FLOAT = 10


def prettyprint(matriz):
    for i in matriz:
        print(i)

def binaria():
    cromossomo = []
    for i in range(DIM):
        cromossomo.append(random.randint(0,1))
    return cromossomo

def inteira():
    cromossomo = []
    for i in range(DIM):
        cromossomo.append(random.randint(DOMINIO_INFERIOR_INT,DOMINIO_SUPERIOR_INT))
    return cromossomo

def real():
    cromossomo = []
    for i in range(DIM):
        cromossomo.append(round(random.uniform(DOMINIO_INFERIOR_FLOAT, DOMINIO_SUPERIOR_FLOAT), 2))
    return cromossomo


populacaoBi = []
for i in range(POP):
    populacaoBi.append(binaria())
prettyprint(populacaoBi)

print()

populacaoInt = []
for i in range(POP):
    populacaoInt.append(inteira())
prettyprint(populacaoInt)

print()

populacaoReal = []
for i in range(POP):
    populacaoReal.append(real())
prettyprint(populacaoReal)
