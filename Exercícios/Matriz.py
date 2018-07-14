"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Matriz                           |
|   Data : 10/04/2018                            |
|________________________________________________|
"""
import math
matriz1 = ([0, 0],
          [0, 0])
matriz2 = ([0, 0],
          [0, 0])
resultado = ([0, 0],
            [0, 0])

def multiplicar(a =[], b = []):
    resultado[0][0] = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0])
    resultado[0][1] = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1])
    resultado[1][0] = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0])
    resultado[1][1] = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1])

    return resultado

def subtrair(a = [], b = []):
    for i in range(2):
        for j in range(2):
            resultado[i][j] = a[i][j] - b[i][j]
    return resultado

for i in range(2):
    for j in range(2):
        matriz1[i][j] = int(input('| Matriz 1|\t\tDigite o elemento {}-{} da matriz: '.format(i + 1, j + 1)))
print('')
for i in range(2):
    for j in range(2):
        matriz2[i][j] = int(input('| Matriz 2|\t\tDigite o elemento {}-{} da matriz: '.format(i + 1, j + 1)))

print('\n\t\t\t\t\tMenu')
opcao = int(input('1 - Multiplicação da Matriz 1 pela Matriz 2:\n2 - Multiplicação da Matriz 2 pela Matriz 1\n'
                  '3 - Subtração da Matriz 1 pela Matriz 2\n4 - Subtração da Matriz 2 pela Matriz 1\n'
                  '5 - Matriz Identidade\n6 - Matriz Inversa\n\nOque deseja fazer: '))

if opcao == 1:
    resultado = multiplicar(matriz1, matriz2)

elif opcao == 2:
    resultado = multiplicar(matriz2, matriz1)

elif opcao == 3:
    resultado = subtrair(matriz1, matriz2)

elif opcao == 4:
    resultado = subtrair(matriz2, matriz1)

elif opcao == 5:
   resultado[0][0], resultado[1][1] = 1, 1

else:

    determinante = (matriz1[0][0] * matriz1[1][1]) - (matriz1[0][1] * matriz1[1][0])
    if determinante == 0:
        print('A determinante é 0, não é possivel prosseguir.')
    adjunta = 1/determinante
    temp = matriz1[0][0]
    matriz1[0][0] = matriz1[1][1]
    matriz1[1][1] = temp
    for i in range(2):
        for j in range(2):
            resultado[i][j] = adjunta * (matriz1[i][j] * -1)

for i in range(2):
    for j in range(2):
        print('{}\t\t'.format(resultado[i][j]), end='')
    print('')