from pprint import pprint
from random import uniform, random, randint
from math import cos
from scipy.interpolate import interp1d
import itertools
from entrada import *


class Populacao:
    id = itertools.count()

    def __init__(self, individuos):
        self.id = next(Populacao.id)
        self.individuos = individuos
        self.melhor = self.melhor_pior_individuo()[0]
        self.pior = self.melhor_pior_individuo()[1]

    def melhor_pior_individuo(self):
        melhorFitness = 0
        piorFitness = 1
        for i in self.individuos:
            if(i.fitnessMax > melhorFitness):
                melhorFitness = i.fitnessMax
                melhorIndividuo = i
            if(i.fitnessMax < piorFitness):
                piorFitness = i.fitnessMax
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
            print('Fitness max: ', i.fitnessMax)
            print('Fitness min: ', i.fitnessMin)
            print()
        
                    

class Individuo:
    id = itertools.count()

    def __init__(self, cromossomo):
        self.id = next(Individuo.id)
        self.cromossomo = cromossomo
        self.binario = self.lista_string(cromossomo)
        self.decimal = self.converte_bin_dec(cromossomo)
        self.x = self.mapeia_d_x(self.decimal)
        self.fitnessMax = self.fitnessMaxFunc()
        self.fitnessMin = 1 - self.fitnessMax

    def getId(self):
        return self.id

    def fitnessMaxFunc(self):
        x = self.xFuncao()
        return (x+4)/6

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
        

# def selecao_roleta(populacao):

#     individuos_selecionados = []
#     soma_fitness = 0
#     for individuo in populacao:
#         soma_fitness+=fitness_maximizacao(individuo)

#     while True:
#         for individuo in populacao:
#             prob = random()
#             if prob > fitness_maximizacao(individuo)/soma_fitness:
#                 individuos_selecionados.append(individuo)
#                 if len(individuos_selecionados) == POP:
#                     return individuos_selecionados
    


# def selecao_torneio(populacao):


# def selecao_anel(populacao):

def main():

    populacao = populacao_inicial()
    populacao.printa()
 
    

if __name__ == "__main__":
    main()
