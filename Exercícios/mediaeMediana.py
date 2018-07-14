"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Média e mediana                  |
|   Data : 10/04/2018                            |
|________________________________________________|
"""

n = [None] * 20
media = 0
mediana = 0
for i in range(20):
    n[i] = int(input('Digite o {}º numero: '.format(i + 1)))

for i in range(20):
    media += n[1]
    if i > 9 and i < 12:
        mediana += n[i]

print('Media: {}\tMediana: {}'.format(media / 20, mediana / 2))
