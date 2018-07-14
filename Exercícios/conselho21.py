"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Conselho 21                      |
|   Data : 06/04/2018                            |
|________________________________________________|
"""
import random

player = 0
for i in range(3):
    player += random.randint(1, 13)

print(player)
if player <= 10:
    print('Sem dúvida compre mais uma carta.')
elif player > 10 and player <= 15:
    print('Há um risco, mas aconselho a comprar mais uma carta')
elif player > 15 and player <= 20:
    print('Aconselho a parar de jogar')
elif player == 21:
    print('Você já venceu, não precisa comprar mais nada')
else:
    print('Você perdeu.')