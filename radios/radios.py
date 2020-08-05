from pprint import pprint
from random import uniform, random, randint
from math import cos, ceil
from scipy.interpolate import interp1d
from entrada import *

def lista_string(lista):
    string = ''
    for i in lista:
        string+=str(i)
    return string

def mapeia_d_x_standard(d):
    return ceil(Li_standard + ((Ui_standard - Li_standard)/(pow(2,L/2)-1))*d)

def mapeia_d_x_luxo(d):
    return ceil(Li_luxo + ((Ui_luxo - Li_luxo)/(pow(2,L/2)-1))*d)

def converte_bin_dec(lista_bin):
    bin_standard = ''
    bin_luxo = ''
    for i in lista_bin[:5]:
        bin_standard+=str(i)
    for i in lista_bin[5:]:
        bin_luxo+=str(i)
    dec_standard = int(bin_standard,2)
    dec_luxo = int(bin_luxo,2)
    return (dec_standard,dec_luxo)
    

def populacao_inicial():
    populacao = []
    for i in range(POP):
        cromossomo = []
        for j in range(DIM):
            cromossomo.append(randint(0,1))
        populacao.append(cromossomo)
    return populacao
        
def penalidade(total_funcionarios):
    return abs(40-total_funcionarios)/100

def fitness(individuo):
    decimal = converte_bin_dec(individuo)
    x_standard = mapeia_d_x_standard(decimal[0])
    x_luxo = mapeia_d_x_luxo(decimal[1])
    return ((x_standard*30 + x_luxo*40)/1360) - penalidade(x_standard+(x_luxo*2))

def main():

    populacao = populacao_inicial()

    populacao.sort(key=fitness)
    (minimo, maximo) = (populacao[0], populacao[-1])

    print('População:')
    pprint(populacao)
    print('\nMinimização:')
    print('Indivíduo:')
    print('-> Binário: ' + str(lista_string(minimo)))

    print('-> Decimal:')
    print('--Standard: ' + str(converte_bin_dec(lista_string(minimo))[0]))
    print('--Luxo: ' + str(converte_bin_dec(lista_string(minimo))[1]))

    print('-> X:')
    print('--Standard: ' + str(mapeia_d_x_standard(converte_bin_dec(lista_string(minimo))[0])))
    print('--Luxo: ' + str(mapeia_d_x_luxo(converte_bin_dec(lista_string(minimo))[1])))

    print('Fitness: ' + str(fitness(minimo))) 


    print('\nMaximização:')
    print('Indivíduo:')
    print('-> Binário: ' + str(lista_string(maximo)))

    print('-> Decimal:')
    print('-- Standard: ' + str(converte_bin_dec(lista_string(maximo))[0]))
    print('-- Luxo: ' + str(converte_bin_dec(lista_string(maximo))[1]))

    print('-> X:')
    print('-- Standard: ' + str(mapeia_d_x_standard(converte_bin_dec(lista_string(maximo))[0])))
    print('-- Luxo: ' + str(mapeia_d_x_luxo(converte_bin_dec(lista_string(maximo))[1])))

    print('Fitness: ' + str(fitness(maximo))) 

if __name__ == "__main__":
    main()
