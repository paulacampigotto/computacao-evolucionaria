from pprint import pprint
from random import uniform, random, randint, choice
from math import cos
from scipy.interpolate import interp1d
import itertools
import copy
import matplotlib.pyplot as plt
from entrada import *
import math


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
        melhorFitness = 0
        piorFitness = 1
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
            print('Binário: ', i.binario)
            print('Decimal: ', i.decimal)
            print('X: ', i.x)
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
        self.binario = self.lista_string(cromossomo)
        self.decimal = self.converte_bin_dec(cromossomo)
        self.x = self.mapeia_d_x(self.decimal)
        self.xFunc = self.xFuncao()
        self.fitness = self.fitnessFunc()

    def getId(self):
        return self.id

    def fitnessFunc(self):
        fit = (self.xFunc+4)/6
        if MAXIMIZAR:
            return fit
        else:
            return 1-fit
            

    def xFuncao(self):
        return cos(20*self.x) - (abs(self.x)/2) + (self.x*self.x*self.x/4)

    def lista_string(self, lista):
        string = ''
        for i in lista:
            string+=str(i)
        return string

    def converte_bin_dec(self, lista_bin):
        binario = ''
        for i in lista_bin:
            binario+=str(i)
        decimal = int(binario,2)
        return decimal

    def mapeia_d_x(self,d):
        return (Li + ((Ui - Li)/(pow(2,16)-1))*d)
    

def populacao_inicial():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for j in range(L):
            cromossomo.append(randint(0,1))
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


def crossover(populacao):
    global PC, TIPO_CROSSOVER
    novaPop = []
    individuos = populacao.individuos.copy()
    while True:
        pai1 = choice(individuos).cromossomo
        pai2 = choice(individuos).cromossomo
        # if(pai1 == pai2):
        #     for i in individuos:
        #         print(i.x)
        #     print()
        #     continue
        if random() < PC:
            filho1 = pai1.copy()
            filho2 = pai2.copy()
            if TIPO_CROSSOVER==0: # Uniforme
                for i in range(len(filho1)):
                    p = random()
                    if p < 0.5:
                        filho1[i] = pai2[i]
                        filho2[i] = pai1[i]
            elif TIPO_CROSSOVER==1: ## 1 Pt
                corte = randint(0,len(filho1)-1)
                filho1 = pai1[0:corte] + pai2[corte:len(filho1)]
                filho2 = pai2[0:corte] + pai1[corte:len(filho1)]
            elif TIPO_CROSSOVER==2: ## 2 Pt
                corte1 = randint(0,len(filho1)-1)
                corte2 = randint(corte1+1,len(filho1))
                filho1 = pai1[0:corte1] + pai2[corte1:corte2] + pai1[corte2:len(filho1)]
                filho2 = pai2[0:corte1] + pai1[corte1:corte2] + pai2[corte2:len(filho1)]
            novaPop.append(Individuo(filho1))
            novaPop.append(Individuo(filho2))
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
                if(i[bit] == 1):
                    i[bit] = 0
                else: i[bit] = 1
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


def desvio_padrao(lista):
    n = len(lista)
    media = sum(lista) / n
    cont = 0
    for i in lista:
        cont += (abs(i - media)) ** 2
    cont /= n
    cont = math.sqrt(cont)
    return cont


def main():

    global MAXIMIZAR, RUN, GEN

    populacao = populacao_inicial()
    melhorInd = populacao.melhor
    melhor_execucao = []
    melhor_execucao_fo = []

    melhor_ex = []
    media_ex = []
    pior_ex = []
    for execucao in range(RUN):
        melhor_it = []
        media_it = []
        pior_it = []
        for iteracao in range(GEN):
            if(melhorInd.fitness < populacao.melhor.fitness):
                melhorInd = populacao.melhor
            print(execucao, iteracao)
            melhor_it.append(populacao.melhor.fitness)
            pior_it.append(populacao.pior.fitness)
            media_it.append(populacao.somaFitness/POP)
            pop_selecao = selecao_torneio(populacao)
            pop_crossover = crossover(pop_selecao)
            pop_mutacao = mutacao(pop_crossover)
            pop_selecao = selecao_torneio(pop_mutacao)
            populacao = elitismo(pop_selecao, populacao.melhor)
            if(iteracao == GEN-1):
                melhor_execucao_fo.append(populacao.melhor.xFunc)

        melhor_execucao.append(melhor_it[GEN-1])
        for x in range(len(melhor_it)):
            if(execucao==0):
                melhor_ex.append(melhor_it[x])
                pior_ex.append(pior_it[x])
                media_ex.append(media_it[x])
            else:
                melhor_ex[x]+=melhor_it[x]
                pior_ex[x]+=pior_it[x]
                media_ex[x]+=media_it[x]

    melhor=[]
    pior=[]
    media=[]
    for i in range(len(melhor_ex)):
        melhor.append(melhor_ex[i]/RUN)
        pior.append(pior_ex[i]/RUN)
        media.append(media_ex[i]/RUN)


    print('Melhor Indivíduo:')
    print('Cromossomo: ',melhorInd.cromossomo)
    print('Fitness: ', melhorInd.fitness)
    print()
    print('Média do melhor indivíduo das execuções: ',sum(melhor_execucao)/len(melhor_execucao))
    print('Desvio padrão do melhor indivíduo das execuções: ',desvio_padrao(melhor_execucao))
    print()
    print('Média da FO melhor indivíduo das execuções: ',sum(melhor_execucao_fo)/len(melhor_execucao_fo))
    print('Desvio padrão da FO do melhor indivíduo das execuções: ',desvio_padrao(melhor_execucao_fo))

    plt.plot(range(GEN),melhor, label = 'Melhor indivíduo', color = 'blue')
    plt.plot(range(GEN),pior, label = 'Pior indivíduo', color = 'red')
    plt.plot(range(GEN),media, label = 'Média da população', color = 'purple')
    plt.legend()
    plt.ylabel('Fitness')
    plt.xlabel('Gerações')
    #plt.title('Gráfico de convergência função algébrica')
    plt.title('Fitness do melhor indivíduo: ' + str(round(max(melhor),2)))
    plt.savefig('grafico_convergencia.png')
    plt.show()
 
    

if __name__ == "__main__":
    main()
