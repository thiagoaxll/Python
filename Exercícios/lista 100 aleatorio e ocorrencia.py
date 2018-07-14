"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  1 - 100 + ocorrência             |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

import random

n = [None] * 100

for i in range(100):
    n[i] = random.randint(1, 10)

numero = int(input('Entre  1 ~ 999 qual numero acha que esta na lista? '))
ocorrencia = 0
valor = 'O numero que você escolheu não esta na lista'
for i in range(100):
    if numero == n[i]:
        valor = 'O numero que você escolheu está na lista.'
        ocorrencia += 1

print('{} | {} ocorrências.'.format(valor, ocorrencia))
