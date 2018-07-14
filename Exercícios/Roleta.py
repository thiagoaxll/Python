"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Roleta                           |
|   Data : 11/04/2018                            |
|________________________________________________|
"""

import random

valorCliente = 1000
valorBanca = 5000
parImparPremio = 2
especificNumPremio = 30
lista = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36]

def pagamento(g, valor, sort, valorB, valorC):
    if g == 1:
        valorC += valorApostado * valor
        valorB -= valorApostado * valor
        print('Numero sorteado: {}, você ganhou!!!'.format(sort))
        return (valorB, valorC)
    elif g == 0:
        valorC -= valorApostado
        valorB += valorApostado
        print('Numero sorteado: {}, você perdeu!!!'.format(sort))
        return (valorB, valorC)
    else:
        valorC = 0
        valorB += valorCliente
        print('Numero sorteado: {}, você perdeu TUDO ;D'.format(sort))
        return (valorB, valorC)

def dado(num, valorB, valorC):
    sort = random.randint(0, 37)
    sort = lista[sort]
    if sort == 0:
        valorB, valorC = pagamento(2, parImparPremio, sort, valorB, valorC)

    else:
        if num == 'par' or num == 'impar':
            tipoNumero = sort % 2
            if tipoNumero == 0 and num == 'par':
                valorB, valorC = pagamento(1, parImparPremio, sort, valorB, valorC)

            elif tipoNumero == 1 and num == 'impar':
                valorB, valorC = pagamento(1, parImparPremio, sort, valorB, valorC)
            else:
                valorB, valorC = pagamento(0, parImparPremio, sort, valorB, valorC)

        elif sort == num:
            valorB, valorC = pagamento(1, especificNumPremio, sort, valorB, valorC)
        else:
            valorB, valorC = pagamento(0, especificNumPremio, sort, valorB, valorC)

    return (valorB, valorC)

while valorCliente > 0 and valorBanca > 0:
    print('\n{:=^70}'.format(' Apostas '))
    print('Banca: R${:=.2f}   |    Cliente: R${:=.2f}\n'.format(valorBanca, valorCliente))
    valorApostado = int(input('Deseja apostar quantos R$: '))

    if valorApostado > valorCliente:
        print('Você não possui essa quantidade, você possuí R$: {:.2f}'.format(valorCliente))
    else:
        print(' 1: numero ímpar.\n 2: Numero par. \n 3: Valor específico. ')
        opcao = int(input('Escolha uma opção: '))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print('Opção inválida.')
        else:
            if opcao == 3:
                while True:
                    numeroApostado = int(input('\nEm qual numero deseja apostar | 1 ~ 36: '))
                    if numeroApostado < 1 or numeroApostado > 36:
                        print('Opção inválida.')
                    else:
                        break
            elif opcao == 1:
                numeroApostado = 'impar'
            else:
                numeroApostado = 'par'
            valorBanca, valorCliente = dado(numeroApostado, valorBanca, valorCliente)
print('{:=^70}\nBanca: {:.2f} | Cliente: {:.2f}'.format(' Resultado ', valorBanca, valorCliente))
