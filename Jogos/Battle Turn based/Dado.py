"""______________________________________________
|   Fiap                                         |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Turn Based                       |
|   Data : 18/04/2016                            |
|________________________________________________|
"""

from random import randint

class Dado(object):

    def aleatorio_balanceado(self):
        d1 = randint(1,12)
        if d1 >= 3 and d1 <= 10:
            d2 = randint(d1-2,d1+2)
        elif d1 < 3:
            d2 = randint(1,3)
        else:
            d2 = randint(10,12)


        return d1,d2

    def aleatorio(self):
        d1 = randint(1,12)
        return d1

