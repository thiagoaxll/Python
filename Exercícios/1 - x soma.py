"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  1 - x soma                       |
|   Data : 06/04/2018                            |
|________________________________________________|
"""

resultado = 0
limite = int(input('Digite um numero para a soma: '))
for i in range(1, limite + 1):
    resultado += i
    print('{}'.format(i))
print('\nTotal = {}'.format(resultado))