"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Tabuada                          |
|   Data : 20/04/2018                            |
|________________________________________________|
"""
n1, n2 = 2, 6
for i in range(0,2):
    for j in range(1, 11):
        for k in range(n1, n2):
            if j < 10:
                if(k * j) > 9:
                    print('{} x {} = {}'.format(k, j, k * j), end = '     ')
                else:
                    print('{} x {} = {}'.format(k, j, k * j), end = '      ')
            else:
                print('{} x {} = {}'.format(k, j, k * j), end = '    ')
        print('')
    n1, n2 = 6, 10
    print('')
