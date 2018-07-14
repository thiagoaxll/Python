"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Ordenar 2 matrizes               |
|   Data : 10/04/2018                            |
|________________________________________________|
"""

n = [0] * 2
for i in range(2):
    n[i] = int(input('Digite o {}º numero: '.format(i + 1)))

if n[0] > n[1]:
    print(n[1], n[0])
else:
    print((n[0], n[1]))
