"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Campo minado                     |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
import random

campo = [[0 for i in range(11)] for i in range(11)]


def imprimir():
    print('\nSudoku')
    for i in range(len(campo) - 1):
        for j in range(len(campo) - 1):
            print('{}\t'.format(campo[i][j]), end='')
        print('')
    print('')


def preencherBombas():
    for i in range(len(campo)):
        while True:
            linha = random.randint(0, len(campo) - 2)
            coluna = random.randint(0, len(campo) - 2)
            if campo[linha][coluna] == 0:
                campo[linha][coluna] = 200
                break


def fronteiras():
    for i in range(len(campo) - 1):
        for j in range(len(campo) - 1):
            if campo[i][j] == 200:
                if j < len(campo) - 1:
                    if campo[i][j + 1] == 0:
                        campo[i][j + 1] = 1
                    if j > 0:
                        if campo[i][j - 1] == 0:
                            campo[i][j - 1] = 1
                if j < len(campo):
                    if campo[i + 1][j] == 0:
                        campo[i + 1][j] = 1
                    if j >= 0:
                        if campo[i - 1][j] == 0:
                            campo[i - 1][j] = 1


preencherBombas()
fronteiras()
imprimir()

