"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Matriz Soma e média              |
|   Data : 10/04/2018                            |
|________________________________________________|
"""
matriz = ([0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],)

for i in range(20):
    matriz[i][0] = int(input('{} | Digite um numero: '.format(i+1)))

print('')

for i in range(20):
    matriz[i][1] = matriz[i-1][1] + matriz[i][0]
for i in range(20):
    matriz[i][2] = matriz[i][1] / (i+1)

print('Numero\tSoma\tMedia')
for i in range(20):
    print('{}\t\t{}\t\t{:}'.format(matriz[i][0], matriz[i][1], matriz[i][2]))