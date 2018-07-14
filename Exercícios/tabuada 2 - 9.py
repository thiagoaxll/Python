"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Tabuada 2 - 9                    |
|   Data : 20/04/2018                            |
|________________________________________________|
"""

n1 = int(input('Digite um número para ver sua tabuada: '))
n2 = int(input('Digite o multiplicador máximo: '))
for i in range(1, n2+1):
    print('{} x {} = {}'.format(n1, i, n1*i))
input()
