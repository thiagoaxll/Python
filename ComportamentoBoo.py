import time

boo = '¶'
mapa = ['_'] * 20
booPos = len(mapa) - 2
player = '>'
playerSide = 'esquerda'

mapa[0] = player
mapa[len(mapa) - 1] = boo
digitar = True
controle = 0

while True:
    if digitar and controle == 0:
        playerSide = input('\nesquerda\t|\tdireita\nPra qual lado deseja virar o jogador? ')
        controle = 3

    if playerSide == 'esquerda':
        player = '<'
        mapa[0] = player
        for i in range(len(mapa)):
            mapa[booPos] = boo
            mapa[booPos + 1] = '_'
            print(mapa[i], end='')

    else:
        player = '>'
        mapa[0] = player
        for i in range(len(mapa)):
            print(mapa[i], end='')
            controle = 1

    if playerSide == 'esquerda':
        booPos -= 1
    controle -= 1
    if booPos < 0:
        print('\n\nO jogador Morreu')
        break


    print('')
    time.sleep(.2)