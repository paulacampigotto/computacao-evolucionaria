from pprint import pprint
from random import uniform, random, randint
from math import cos
from scipy.interpolate import interp1d

## GLOBAIS
tam_populacao = 0
tam_cromossomo = 0
Li = 0
Ui = 0
L = 0


def leitura():
    global tam_populacao, tam_cromossomo, Li, Ui, L
    f = open('entrada.txt', 'r')
    linhas = f.readlines()

    for i in range(len(linhas)):
        linhas[i] = linhas[i].split("\n")[0]

    tam_populacao = (int)(linhas[0].split("=")[1])
    tam_cromossomo = (int)(linhas[1].split("=")[1])
    Li = (int)((linhas[2].split("=")[1]).split(",")[0].split("[")[1])
    Ui = (int)((linhas[2].split("=")[1]).split(",")[1].split("]")[0])
    L = tam_cromossomo

def lista_string(lista):
    string = ''
    for i in lista:
        string+=str(i)
    return string

def mapeia_d_x(d):
    return (Li + ((Ui - Li)/(pow(2,16)-1))*d)

def converte_bin_dec(lista_bin):
    binario = ''
    for i in lista_bin:
        binario+=str(i)
    decimal = int(binario,2)
    return decimal
    

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
    x = mapeia_d_x(decimal)
    return cos(20*x) - (abs(x)/2) + (x*x*x/4)

def main():

    leitura()

    populacao = populacao_inicial()

    populacao.sort(key=fitness)
    (minimo, maximo) = (populacao[0], populacao[-1])

    print('População:')
    pprint(populacao)
    print('\nMinimização:')
    print('Indivíduo:')
    print('- Binário: ' + str(lista_string(minimo)))
    print('- Decimal: ' + str(converte_bin_dec(lista_string(minimo))/10000))
    print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(minimo)))))
    print('Fitness: ' + str(fitness(minimo))) 

    print('\nMaximização:')
    print('Indivíduo:')
    print('- Binário: ' + str(lista_string(maximo)))
    print('- Decimal: ' + str(converte_bin_dec(lista_string(maximo))/10000))
    print('- X: ' + str(mapeia_d_x(converte_bin_dec(lista_string(maximo)))))
    print('Fitness: ' + str(fitness(maximo))) 

if __name__ == "__main__":
    main()
