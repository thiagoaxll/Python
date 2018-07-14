"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Matriz inversa                   |
|   Data : 10/04/2018                            |
|________________________________________________|
"""
n = [None] * 20

for i in range(20):
    n[i] = int(input('{} | Digite um numero: '.format(i + 1)))
quantidade = i
print('')
for i in range(20):
    print(n[quantidade - i])

