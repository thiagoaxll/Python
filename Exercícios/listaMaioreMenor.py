"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Lista maior e menor              |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

numero = [None] * 5

for i in range(5):
    numero[i] = int(input('Digite um numero: '))

maior = numero[0]
menor = numero[0]

for i in range(5):
    if numero[i] >= maior:
        maior = numero[i]
    if numero[i] <= menor:
        menor = numero[i]
print('')
for i in range(5):
    print(numero[i])

print('\nMaior numero: {}\t Menor numero: {}'.format(maior, menor))
