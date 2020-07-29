from pprint import pprint
from random import randint, uniform, choice

COD = ''
POP = 0
DIM = 0
Li=0
Ui=0

def leitura():
    global COD, POP, DIM, Li, Ui
    f = open('entrada.txt', 'r')
    linhas = f.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].split("\n")[0]

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
            cromossomo.append(randint(0,1))
        populacao.append(cromossomo)
    return populacao

def popInteira():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for i in range(DIM):
            cromossomo.append(randint(Li,Ui))
        populacao.append(cromossomo)
    return populacao

def popInteiraPerm():
    populacao = []
    for i in range(POP):
        vetor = [j for j in range(DIM)]
        cromossomo = []
        for j in range(DIM):
            rand = choice(vetor)
            cromossomo.append(rand)
            vetor.remove(rand)
        populacao.append(cromossomo)
    return populacao

def popReal():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for i in range(DIM):
            cromossomo.append(round(uniform(Li, Ui), 2))
        populacao.append(cromossomo)
    return populacao

def fitness(vetor):
    colisoes = 0
    for i in range(DIM):
        for k in range(i+1,DIM):
            if k-i == vetor[k]-vetor[i] or i-k == vetor[k]-vetor[i]:
                colisoes += 1
    return colisoes

def tabuleiro(vetor):
    for i in range(DIM):
        print('.\t'*vetor[i],end='R\t')
        print('.\t'*(DIM-1-vetor[i]))
        print()


def main():


    leitura()

    if(COD == 'BIN'):
        populacao = popBinaria()
    elif(COD == 'INT'):
        populacao = popInteira()
    elif(COD == 'REAL'):
        populacao = popReal()
    else:
        populacao = popInteiraPerm()

    populacao.sort(key=fitness)
    (pior, melhor) = (populacao[0], populacao[-1])

    pprint(populacao)
    print('Pior indivíduo:')
    tabuleiro(pior)
    print('Fitness:' + str(fitness(pior)))
    print('Melhor indivíduo:')
    tabuleiro(melhor)
    print('Fitness:' + str(fitness(melhor)))

    pior_caso = [0,1,2,3,4,5,6,7]
    print(fitness(pior_caso))


if __name__ == "__main__":
    main()
