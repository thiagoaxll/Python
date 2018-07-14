"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Pedra papel tesoura              |
|   Data : 11/04/2018                            |
|________________________________________________|
"""
import random

print('1: Pedra\t2: Papel\t3: Tesoura')
jogador = int(input('Oque deseja jogar: '))
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(1, 3)


print('\nComputador escolheu:', jogadas[computador - 1], '\t Você escolheu: ', jogadas[jogador -1], '\n')

if jogador == 1:
    if computador == 1:
        print('Empate')
    elif computador == 2:
        print('Você perdeu.')
    else:
        print('Voce Ganhou')

elif jogador == 2:
    if computador == 2:
        print('Empate')
    elif computador == 1:
        print('Você Ganhou.')
    else:
        print('Voce Perdeu')
else:
    if computador == 3:
        print('Empate')
    elif computador == 1:
        print('Você Perdeu.')
    else:
        print('Voce Ganhou.')
