"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Busca binaria                    |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

matriz = [0, 10, 20, 30, 31, 32, 33, 34, 35, 40, 45, 46, 50, 51, 100]

def pesquisar(lista, valor):
    indice =  -1
    for i in range(len(lista)):
        if lista[i] == valor:
            indice = i

    return indice

n = int(input('Digite o numero que deseja buscar no vetor: '))

n = pesquisar(matriz, n)

print('Indice vetor: {}'.format(n))