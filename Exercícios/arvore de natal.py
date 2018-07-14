"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Arvore de natal                  |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

def espaco (i):
    for k in range(5 - i):
       print(' ', end='')

for i in range(1, 6):
    espaco(i)
    print('/', end='')
    for j in range(1, (i * 2) + 1):
        print('*', end='')
    print('\ ')
    print('')

print('\t||\n\t||\n\t||')