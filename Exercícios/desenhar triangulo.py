"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Desenhar triângulo               |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

n = int(input('Digite o tamanho do triangulo: '))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print('')