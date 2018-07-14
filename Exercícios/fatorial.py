"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Fatorial                         |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
n1 = int(input('Digite um número natural: '))
fatorial = n1
for i in range(1, n1):
    n1 = n1 * (fatorial-i)
print('O fatorial é: {}'.format(n1))
input()
