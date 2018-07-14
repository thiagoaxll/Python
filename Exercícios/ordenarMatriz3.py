"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Ordenar matriz 3 numeros         |
|   Data : 10/04/2018                            |
|________________________________________________|
"""
matriz = [0] * 3

for i in range(len(matriz)):
    matriz[i] = int(input('Digite o {}º numero: '.format(i + 1)))

for i in range(0, len(matriz) - 1):
    min = i
    for j in range(i + 1, len(matriz)):
        if(matriz[j] < matriz[min]):
            min = j
        temp = matriz[min]
        matriz[min] = matriz[i]
        matriz[i] = temp

print('[\t', end='')
for i in range(len(matriz)):
    print('{}\t'.format(matriz[i]), end='')
print(']')