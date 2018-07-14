"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Ordenar Matrizes                 |
|   Data : 10/04/2018                            |
|________________________________________________|
"""

matriz = [8, 2, 5, 4, 6, 11, 10, 20, 14, 3]



def ordenar():
    for i in range(0, len(matriz) - 1):
        min = i
        for j in range(i + 1, len(matriz)):
            if(matriz[j] < matriz[min]):
                min = j
            temp = matriz[min]
            matriz[min] = matriz[i]
            matriz[i] = temp

ordenar()


print('[\t', end='')
for i in range(len(matriz)):
    print('{}\t'.format(matriz[i]), end='')
print(']')