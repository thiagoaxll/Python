"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  2 - 30 fatorial                  |
|   Data : 06/04/2018                            |
|________________________________________________|
"""


def calcular(valor):
    fatorial = valor
    for i in range(1, valor):
        valor = valor * (fatorial - i)
    return(valor)

for i in range(2, 31):
    print('{} '.format(i), end='')
    fatorial = calcular(i)
    print('\t-\t{}! = {}'.format(i, fatorial))

