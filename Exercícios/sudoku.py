"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Sudoku                           |
|   Data : 20/04/2018                            |
|________________________________________________|
"""
import random

tabuleiro = [[random.randint(1, 20) for i in range(5)] for j in range(5)]


def imprimir():
    print('\nSudoku')
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            print('{}\t'.format(tabuleiro[i][j]), end='')
        print('')
    print('')


def alterarTabuleiro(l, c, e):
    tabuleiro[l - 1][c - 1] = e


while True:
    imprimir()
    linha = int(input('(1 ~ 5) Em qual linha deseja inserir o elemento : '))
    coluna = int(input('(1 ~ 5) Em qual coluna deseja inserir o elemento : '))
    n = int(input('Digite o numero para incluir no tabuleiro: '))
    if linha < 1 or linha > 5 or coluna < 1 or coluna > 5:
        print('\nOpção invalida!\n')
    else:
        alterarTabuleiro(linha, coluna, n)