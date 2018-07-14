"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  lista 1 - 100 aleatório          |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

import random

n = [None] * 100

for i in range(100):
    n[i] = random.randint(1, 999)
    print(n[i])

