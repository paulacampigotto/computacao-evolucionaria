from pprint import pprint
from random import uniform, random, randint, choice
from math import cos
from scipy.interpolate import interp1d
import itertools
import copy
import matplotlib.pyplot as plt
import numpy as np
from entrada import *


class Populacao:
    id = itertools.count()

    def __init__(self, individuos):
        self.id = next(Populacao.id)
        self.individuos = individuos
        self.melhor = self.melhor_pior_individuo()[0]
        self.pior = self.melhor_pior_individuo()[1]
        self.somaFitness = self.somafits()

    def somafits(self):
        soma = 0
        for i in self.individuos:
            soma+=i.fitness
        return soma

    def melhor_pior_individuo(self):
        melhorFitness = -100
        piorFitness = 100
        for i in self.individuos:
            if(i.fitness > melhorFitness):
                melhorFitness = i.fitness
                melhorIndividuo = i
            if(i.fitness < piorFitness):
                piorFitness = i.fitness
                piorIndividuo = i
        if MAXIMIZAR:
            return (melhorIndividuo, piorIndividuo)
        else:
            return (piorIndividuo, melhorIndividuo)

    def printa(self):
        for i in self.individuos:
            print('----- Indivíduo', i.getId(), '-----')
            print('Cromossomo: ', i.cromossomo)
            print('Fitness: ', i.fitness)
            print()
            
    def retorna_ind_pelo_cromossomo(self,cromossomo):
        for ind in self.individuos:
            if(cromossomo == ind.cromossomo):
                return ind
                    

class Individuo:
    id = itertools.count()

    def __init__(self, cromossomo):
        self.id = next(Individuo.id)
        self.cromossomo = cromossomo
        self.fitness = self.fitnessFunc()

    def getId(self):
        return self.id

    def fitnessFunc(self):
        colisoes = 0
        vetor = self.cromossomo
        for i in range(DIM):
            ok = False
            for j in range(DIM):
                colunaA = i
                colunaB = j
                linhaA = vetor[i]
                linhaB = vetor[j]
                if(abs(colunaA-colunaB) == (abs(linhaA-linhaB)) and i != j):
                    ok = True
                    break
            if ok:
                colisoes+=1
        return (DIM*(DIM-colisoes))/(DIM*DIM) 

    def printaTabuleiro(self):
        vetor = self.cromossomo
        for i in range(DIM):
            print('.\t'*vetor[i],end='R\t')
            print('.\t'*(DIM-1-vetor[i]))
            print()
            

def populacao_inicial():
    populacao = []
    for i in range(POP):
        vetor = [j for j in range(DIM)]
        cromossomo = []
        for j in range(DIM):
            rand = choice(vetor)
            cromossomo.append(rand)
            vetor.remove(rand)
        populacao.append(Individuo(cromossomo))
    return Populacao(populacao)
        

def selecao_roleta(populacao):

    individuos_selecionados = []
    soma_fitness = populacao.somaFitness

    while True:
        for individuo in populacao.individuos:
            prob = random()
            if prob < individuo.fitness/soma_fitness:
                individuos_selecionados.append(individuo)
                if len(individuos_selecionados) == POP:
                    return Populacao(individuos_selecionados)

def selecao_torneio(populacao):
    global K,KP
    individuos_selecionados = []

    while True:
        copia_pop = None
        copia_pop = Populacao(populacao.individuos.copy())
        lista = []
        for i in range(K):
            individuo = choice(copia_pop.individuos)
            lista.append(individuo)
            copia_pop.individuos.remove(individuo)
        lista_pop = Populacao(lista)
        prob = random()
        if(prob <= KP):
            individuos_selecionados.append(lista_pop.melhor)
        else:
            individuos_selecionados.append(lista_pop.pior)
        if len(individuos_selecionados) == POP:
            return Populacao(individuos_selecionados)

# def gera_filho1_filho2_pmx(pai1_parte1, pai1_parte2, pai1_parte3, pai2_parte1, pai2_parte2, pai2_parte3):
#     for i in range(len(pai1_parte1)):
#         if pai2_parte2.contains(pai1_parte1[i]):

def recursion1 (relations, temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross):
    child = np.array([0 for i in range(DIM)])
    for i,j in enumerate(temp_child[:firstCrossPoint]):
        c=0
        for x in relations:
            if j == x[0]:
                child[i]=x[1]
                c=1
                break
        if c==0:
            child[i]=j
    j=0
    for i in range(firstCrossPoint,secondCrossPoint):
        child[i]=parent2MiddleCross[j]
        j+=1

    for i,j in enumerate(temp_child[secondCrossPoint:]):
        c=0
        for x in relations:
            if j == x[0]:
                child[i+secondCrossPoint]=x[1]
                c=1
                break
        if c==0:
            child[i+secondCrossPoint]=j
    child_unique=np.unique(child)
    if len(child)>len(child_unique):
        child=recursion1(relations,child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
    lista = []
    for i in child:
        lista.append(i)
    return(lista)

def recursion2(relations, temp_child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross):
        child = np.array([0 for i in range(DIM)])
        for i,j in enumerate(temp_child[:firstCrossPoint]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i]=x[0]
                    c=1
                    break
            if c==0:
                child[i]=j
        j=0
        for i in range(firstCrossPoint,secondCrossPoint):
            child[i]=parent1MiddleCross[j]
            j+=1

        for i,j in enumerate(temp_child[secondCrossPoint:]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i+secondCrossPoint]=x[0]
                    c=1
                    break
            if c==0:
                child[i+secondCrossPoint]=j
        child_unique=np.unique(child)
        if len(child)>len(child_unique):
            child=recursion2(relations,child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        lista = []
        for i in child:
            lista.append(i)
        return(lista)

def crossover(populacao):
    global PC, TIPO_CROSSOVER
    novaPop = []
    individuos = populacao.individuos.copy()
    while True:
        parent1 = choice(individuos).cromossomo
        parent2 = choice(individuos).cromossomo
        if random() < PC:
            if TIPO_CROSSOVER==3: ## PMX
                firstCrossPoint = np.random.randint(0,len(parent1)-2)
                secondCrossPoint = np.random.randint(firstCrossPoint+1,len(parent1)-1)
                parent1MiddleCross = parent1[firstCrossPoint:secondCrossPoint]
                parent2MiddleCross = parent2[firstCrossPoint:secondCrossPoint]
                temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]
                temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]
                relations = []
                for i in range(len(parent1MiddleCross)):
                    relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])
                child1=recursion1(relations, temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
                child2=recursion2(relations,temp_child2,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
            novaPop.append(Individuo(child1))
            novaPop.append(Individuo(child2))
            if len(novaPop) == POP:
                return Populacao(novaPop)


def mutacao(populacao):
    global PM
    novaPop = []
    individuos=[]
    for i in populacao.individuos:
        individuos.append(i.cromossomo)
    for i in individuos:
        for bit in range(len(i)):
            if random() < PM:
                temp = i[bit]
                aleatorio = randint(0,DIM-1)
                i[bit] = i[aleatorio]
                i[aleatorio] = temp
        novaPop.append(Individuo(i))
    return Populacao(novaPop)
                

def elitismo(populacao, melhorInd):
    melhorAtual = populacao.melhor
    novaPop=[]
    individuos = []
    for i in populacao.individuos:
        individuos.append(i.cromossomo)
    if(melhorAtual.fitness < melhorInd.fitness):
        for i in individuos:
            if(populacao.retorna_ind_pelo_cromossomo(i) == populacao.pior):
                individuos.remove(i)
                individuos.append(melhorInd.cromossomo)
                for i in individuos:
                    novaPop.append(Individuo(i))
                return Populacao(novaPop)
    else:
        return populacao

 # def selecao_anel(populacao):




def main():

    global MAXIMIZAR, RUN, GEN

    populacao = populacao_inicial()

    crossover(populacao)
    
    melhor_ex = []
    pior_ex = []
    media_ex = []
    for execucao in range(RUN):
        populacao = populacao_inicial()
        melhor_it = []
        pior_it = []
        media_it = []
        for iteracao in range(GEN):
            melhorInd = populacao.melhor
            melhor_it.append(melhorInd.fitness)
            pior_it.append(populacao.pior.fitness)
            media_it.append(populacao.somaFitness/POP)

            print("RUN:",execucao,"  GEN:", iteracao)

            pop_selecao = selecao_torneio(populacao)
            pop_crossover = crossover(pop_selecao)
            pop_mutacao = mutacao(pop_crossover)
            pop_selecao = selecao_torneio(pop_mutacao)
            populacao = elitismo(pop_selecao, melhorInd)

        for x in range(len(melhor_it)):
            if(execucao==0):
                melhor_ex.append(melhor_it[x])
                pior_ex.append(pior_it[x])
                media_ex.append(media_it[x])
            else:
                melhor_ex[x]+=melhor_it[x]
                pior_ex[x]+=pior_it[x]
                media_ex[x]+=media_it[x]


    x_melhor = []
    x_pior = []
    x_media = []
    for i in range(GEN):
        x_melhor.append(melhor_ex[i]/RUN)
        x_pior.append(pior_ex[i]/RUN)
        x_media.append(media_ex[i]/RUN)

    plt.plot(range(GEN),x_melhor, label = 'Melhor indivíduo', color = 'blue')
    plt.plot(range(GEN),x_pior, label = 'Pior indivíduo', color = 'red')
    plt.plot(range(GEN),x_media, label = 'Média da população', color = 'purple')
    plt.legend()
    plt.ylabel('Fitness')
    plt.xlabel('Gerações')
    plt.title('Gráfico de convergência N rainhas')
    #plt.title('Fitness do melhor indivíduo: ' + str(round(max(x_melhor),2)))
    plt.savefig('grafico_convergencia.png')
    plt.show()
 
    

if __name__ == "__main__":
    main()
