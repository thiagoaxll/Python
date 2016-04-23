from Dado import Dado
from random import randint


class Jogadas(object):

    dado = Dado()
    def atkatk(self,vida1,vida2,base1,base2):
        atk1 = self.dado.aleatorio()
        atk2 = self.dado.aleatorio()
        print("----------------------------------------")
        print("Valor dado 1: ",atk1)
        print("Valor dado 2: ",atk2)
        if atk1 > base1:
            atk1 = base1
        if atk2 > base2:
            atk2 = base2
        if atk1 == 1:
            print("Jogador 1 Crítico")
            atk1 = base1 * 2
        if atk2 == 1:
            print("Jogador 2 Crítico")
            atk2 = base2 * 2


        print("\nAtaque jogador1:",atk1,"|| Ataque jogador2:",atk2,"\n")
        vida2 -= atk1
        vida1 -= atk2

        return vida1,vida2


    def atkdef(self,vida2,base1,def2):
        atk1 = self.dado.aleatorio()
        print("Valor do dado de Ataque:",atk1)
        if atk1 == 1:
            print("Jogador 1 Crítico")
            atk1 = base1 * 2
            vida2 = vida2-atk1
            return vida2

        if atk1 > base1:
            atk1 = base1

        if atk1 > def2:
            print("--------------------------------------")
            print("Jogador 2 Recebeu dano.")
            print("---------------------------------------")
            atk1 = atk1 - def2
            vida2 -= atk1
            return vida2
        print("----------------------------------")
        print("Jogador 2 Não recebeu dano")
        print("---------------------------------")
        return vida2


    def defatk(self, vida1, base2, def1):
        atk2 = self.dado.aleatorio()
        print("Valor do dado de Ataque:", atk2,"Valor da Defesa:",def1)
        if atk2 == 1:
            atk2 = base1 * 2
            vida1 = vida1 - atk2
            print("----------------------------------")
            print("Jogador 2 Crítico")
            print("Valor do dado de Ataque:", atk2, "Valor da Defesa:", def1)
            print("----------------------------------")

            return vida1

        if atk2 > base2:
            atk2 = base2

        if atk2 > def1:
            print("----------------------------------")
            print("Jogador 1 Recebeu dano.")
            print("----------------------------------")
            atk2 = atk2 - def1
            vida1 -= atk2
            return vida1
        print("----------------------------------")
        print("Jogador 1 Não recebeu dano")
        print("----------------------------------")
        return vida1


    def defdef(self):
        print("Nada aconteceu!")

    def s1(self,base1,vida1,base2,vida2):

        atk1 = self.dado.aleatorio()
        atk2 = self.dado.aleatorio()
        print("dado 1 ||",atk1)
        print("dado 2 ||", atk2)
        if atk1 < base1:
            vida2 -= base1
        else:
            vida2 -= atk1

        if atk2 <= base2:
            vida1 -= atk2
        else:
            vida1 -= base2

        return vida1,0,vida2

    def s2(self, base2, vida2, base1, vida1):

        atk1 = self.dado.aleatorio()
        atk2 = self.dado.aleatorio()
        print("dado 1 ||", atk1)
        print("dado 2 ||", atk2)
        if atk2 < base2:
            vida1 -= base2
        else:
            vida1 -= atk2

        if atk1 <= base1:
            vida2 -= atk1
        else:
            vida2 -= base1

        return vida2, 0, vida1


    def s1s2(self,base1,vida1,base2,vida2):
        atk1 = self.dado.aleatorio()
        atk2 = self.dado.aleatorio()

        print("dado 1 ||", atk1)
        print("dado 2 ||", atk2)
        if atk1 < base1:
            vida2 -= base1
        else:
            vida2 -= atk1
        if atk2 < base2:
            vida1 -= base2
        else:
            vida1 -= atk2

        return vida1,0,vida2,0




