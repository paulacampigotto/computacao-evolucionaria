from pprint import pprint
from random import uniform, random
from math import cos

## GLOBAIS
tam_populacao = 10
tam_cromossomo = 17
Li = -2
Ui = 2
casas_decimais = 4

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
        valor = round(uniform(Li,Ui),casas_decimais)
        valor_binario = string_lista(float_to_binary(valor, 2, 13))
        populacao.append(valor_binario)
    return populacao
        

def fitness(individuo):
    individuo_string = lista_string(individuo)
    x = round(binary_to_float(individuo_string, 2, 13),casas_decimais)
    return cos(20*x) - (abs(x)/2) + (x*x*x/4)

def main():

    populacao = populacao_inicial()

    populacao.sort(key=fitness)
    (minimo, maximo) = (populacao[0], populacao[-1])

    print('População:')
    pprint(populacao)
    print('\nMinimização:')
    print('Indivíduo: ' + lista_string(minimo)+ ' ou ' + str(round(binary_to_float(lista_string(minimo),2, 13),casas_decimais)))
    print('Fitness: ' + str(fitness(minimo))) 
    print('\nMaximização:')
    print('Indivíduo: ' + lista_string(maximo)+ ' ou ' + str(round(binary_to_float(lista_string(maximo),2, 13),casas_decimais)))
    print('Fitness: ' + str(fitness(maximo))) 

if __name__ == "__main__":
    main()
