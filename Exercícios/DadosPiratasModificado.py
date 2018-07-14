"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Dados pirata modificado          |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
import random

dados = 0

frequencia = [0] * 6

for i in range(6):
    dados += random.randint(1, 6)
    if dados == 1:
        frequencia[0] += 1
    elif dados == 2:
        frequencia[1] += 1
    elif dados == 3:
        frequencia[2] += 1
    elif dados == 4:
        frequencia[3] += 1
    elif dados == 5:
        frequencia[4] += 1
    elif dados == 6:
        frequencia[5] += 1


guess = int(input('Qual dado teve a maior frequencia: '))
guessComputer = random.randint(1, 6)
print('Palpite computador: {}\n'.format(guessComputer))
if frequencia[guess - 1] == frequencia[guessComputer - 1]:
    print('Empate')
elif frequencia[guess -1] > frequencia[guessComputer - 1]:
    print('Você venceu\t\t\tSaiu {} x este valor\t\tNumero do computador saiu : {} x'.format(frequencia[guess - 1], frequencia[guessComputer - 1]))
else:
    print('Você Perdeu\t\t\tSaiu {} x este valor\t\tNumero do computador saiu: {} x'.format(frequencia[guess - 1], frequencia[guessComputer - 1]))



