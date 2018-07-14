"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  100 numeros aleatorios usuário   |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

import random

n = [None] * 100

for i in range(100):
    n[i] = random.randint(1, 999)

numero = int(input('Entre  1 ~ 999 qual numero acha que esta na lista? '))

valor = 'O numero que você escolheu não esta na lista'
for i in range(100):
    if numero == n[i]:
        valor = 'O numero que você escolheu está na lista.'
        break

print(valor)