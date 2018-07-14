"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Retangulo                        |
|   Data : 11/04/2018                            |
|________________________________________________|
"""
altura = int(input('Digite a altura do retângulo: '))
largura = int(input('Digite a largura do retângulo: '))

for i in range(0, altura):
    print('{}'.format(largura*'*'))
