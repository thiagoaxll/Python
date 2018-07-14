"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Forca                            |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
import random
vida = 5
palavras = ['M O N I T O R', 'C E L U L A R', 'E S C O V A', 'C A S A', 'P L A Y S T A T I O N',
            'X B O X', 'N I N T E N D O', 'C O M P U T A D O R']
letrasErradas = [None] * vida
palavraSorteada = palavras[random.randint(0, len(palavras) - 1)].split()
palavraIncognita = ['_'] * len(palavraSorteada)

print('*** Jogo da forca ***\n')
while vida > 0:
    controle = 0
    print('Vidas: {}\tLetras erradas: '.format(vida, letrasErradas), end='')
    print('', end='')

    for i in range(len(letrasErradas)):
        if letrasErradas[i] != None:
            print(letrasErradas[i], end=' ')
    print('\n')
    for i in range(len(palavraIncognita)):
        print('{}'.format(palavraIncognita[i]), end=' ')
    print('')


    for i in range(len(palavraIncognita)):
        if palavraIncognita[i] == '_':
            controle = 1
            break
        else:
            controle = 0

    if controle == 0:
        print('\nParabens, Você venceu!')
        break
    else:
        controle = 0
        guess = str(input('\nAdvinhe uma letra: '))
        guess = guess.upper()

        for j in range(len(palavraSorteada)):
            if guess == palavraSorteada[j]:
                palavraIncognita[j] = guess
                controle = 1

        if controle == 0:
            for i in range(len(letrasErradas)):
                if letrasErradas[i] == guess:
                    break
                elif letrasErradas[i] == None:
                    letrasErradas[i] = guess
                    vida -= 1
                    break
        print("\n" * 100)
        print('------------------------------------------------')
if vida <= 0:
    print('Você perdeu!')
    print('A palavra era: ',end='')
    for i in range(len(palavraSorteada)):
        print('{}'.format(palavraSorteada[i]), end='')
input()

