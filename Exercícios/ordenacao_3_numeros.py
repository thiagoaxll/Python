"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Ordenar 3 numeros                |
|   Data : 10/04/2018                            |
|________________________________________________|
"""
print('Os numeros não devem se repetir.\n')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b and a < c:
    if b < c:
        print('{} {} {}'.format(a, b, c))
    else:
        print('{} {} {}'.format(a, c, b))
if b < a and b < c:
    if a < c:
        print('{} {} {}'.format(b, a, c))
    else:
        print('{} {} {}'.format(b, c, a))
if c < a and c < b:
    if a < b:
        print('{} {} {}'.format(c, a, b))
    else:
        print('{} {} {}'.format(c, b, a))

