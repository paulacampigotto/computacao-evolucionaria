from pprint import pprint
from random import uniform, random, randint
from math import cos, ceil
from scipy.interpolate import interp1d

## GLOBAIS
tam_populacao = 10
tam_cromossomo = 10
Li = -20000
Ui = 20000
L = tam_cromossomo


def lista_string(lista):
    string = ''
    for i in lista:
        string+=str(i)
    return string

def mapeia_d_x_standard(d):
    return ceil(0 + ((24 - 0)/(pow(2,L/2)-1))*d)

def mapeia_d_x_luxo(d):
    return ceil(0 + ((16 - 0)/(pow(2,L/2)-1))*d)

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
    for i in range(tam_populacao):
        cromossomo = []
        for j in range(tam_cromossomo):
            cromossomo.append(randint(0,1))
        populacao.append(cromossomo)
    return populacao
        

def fitness(individuo):
    decimal = converte_bin_dec(individuo)
    x_standard = mapeia_d_x_standard(decimal[0])
    x_luxo = mapeia_d_x_luxo(decimal[1])
    
    return cos(20*x) - (abs(x)/2) + (x*x*x/4)

def main():

    populacao = populacao_inicial()


    # populacao.sort(key=fitness)
    # (minimo, maximo) = (populacao[0], populacao[-1])

    # print('População:')
    # pprint(populacao)
    # print('\nMinimização:')
    # print('Indivíduo:')
    # print('- Binário: ' + str(lista_string(minimo)))
    # print('- Decimal: ' + str(converte_bin_dec(lista_string(minimo))/10000))
    # print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(minimo)))/10000))
    # print('Fitness: ' + str(fitness(minimo))) 

    # print('\nMaximização:')
    # print('Indivíduo:')
    # print('- Binário: ' + str(lista_string(maximo)))
    # print('- Decimal: ' + str(converte_bin_dec(lista_string(maximo))/10000))
    # print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(maximo)))/10000))
    # print('Fitness: ' + str(fitness(maximo))) 

if __name__ == "__main__":
    main()
