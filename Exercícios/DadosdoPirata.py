"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Dados pirata                     |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
import random

dados = 0


for i in range(6):
    dados += random.randint(1, 6)

guess = int(input('Quanto deu a soma dos dados: '))
guessComputer = random.randint(6, 36)

print('Seu valor: {}\tComputador: {}'.format(guess, guessComputer))
if guess == guessComputer:
    print('Empate\tA soma é: {}'.format(dados))
elif guess == dados:
    print('Voê ganhou\tA soma é: {}'.format(dados))
elif guessComputer == dados:
    print('O computador ganhou\tA soma é: {}'.format(dados))
else:
    diferencaPlayer = guess - dados
    diferecaComputer = guessComputer - dados

    if diferecaComputer < 0:
        diferecaComputer *= -1
    if diferencaPlayer < 0:
        diferencaPlayer *= -1

    if diferecaComputer > diferencaPlayer:
        print('Você Chegou mais proximo.\tA soma é: {}'.format(dados))
    else:
        print('O computador chegou mais proximo.\tA soma é: {}'.format(dados))






