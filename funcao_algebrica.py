from pprint import pprint
from random import randint, uniform, choice, random
import itertools
from math import ceil, cos

## GLOBAIS
tam_populacao = 10
tam_cromossomo = 17


def float_to_binary(x, m, n):
    x_scaled = round(x * 2 ** n)
    return '{:0{}b}'.format(x_scaled, m + n)

def binary_to_float(bstr, m, n):
    return int(bstr, 2) / 2 ** n

def string_lista(string):
    lista = []
    for i in string:
        if i == '-':
            lista.append(i)
        else:
            lista.append(int(i))
    return lista

def lista_string(lista):
    string = ''
    for i in lista:
        if i == '-':
            string+=i
        else:
            string+=str(i)
    return string

def populacao_inicial():
    populacao = []
    for i in range(tam_populacao):
        valor = round(uniform(-2,2),4)
        valor_binario = string_lista(float_to_binary(valor, 2, 13))
        populacao.append(valor_binario)
    return populacao
        

def fitness(individuo):
    individuo_string = lista_string(individuo)
    x = round(binary_to_float(individuo_string, 2, 13),4)
    return cos(20*x) - (abs(x)/2) + (x*x*x/4)

def main():

    populacao = populacao_inicial()

    populacao.sort(key=fitness)
    (minimo, maximo) = (populacao[0], populacao[-1])

    print('População:')
    pprint(populacao)
    print('\nMinimização: \nIndivíduo: ' + lista_string(minimo) + ' ou ' + str(round(binary_to_float(lista_string(minimo),2, 13),4)) + '\nFitness: ' + str(fitness(minimo)))
    print('\nMaximização: \nIndivíduo: ' + lista_string(maximo) + ' ou ' + str(round(binary_to_float(lista_string(maximo),2, 13),4)) + '\nFitness: ' + str(fitness(maximo)))


if __name__ == "__main__":
    main()


    
# b = binary_to_float(a, 2, 13)
# print(round(b,4))