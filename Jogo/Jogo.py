import time
from Nomes import Nomes
from Dado import Dado
from Jogadas import Jogadas

dado = Dado()
play = Jogadas()
jdado = None
nome = Nomes()
jogador1 = [0,0,100,0]
jogador2 = [0,0,100,0]

nome1 = nome.nomes[0]
nome2 = nome.nomes[1]
play.nome1 = nome1
play.nome2 = nome2

c = ['|','|','|','|','|','|','|','|','|','|']



print("Gerando atributos basico ")

for i in range(10):
    print(c[i])
    time.sleep(0.4)

print("Atributos Gerados.")


def mensagem():
    print("um dos jogadores não possui pontos de especial.\nEscolha novamente sua ação")


# Gera o atributo basico dos Jogadores.
for i in range (2):
    jdado = dado.aleatorio_balanceado()
    if i == 0:
        jogador1[0] = jdado[0]
        jogador2[0] = jdado[1]
    if i == 1:
        jogador1[1] = jdado[0]
        jogador2[1] = jdado[1]

print(" ----------------------------------")
print("| Jogador 1: ",nome1)
print("| Ataque:",jogador1[0],"Defesa:",jogador1[1],"Vida:",jogador1[2])
print(" ----------------------------------")
print("| Jogador 2: ",nome2)
print("| Ataque:",jogador2[0],"Defesa:",jogador2[1],"Vida:",jogador2[2])
print(" ----------------------------------")


controle = True
turno = 1
while controle == True:
    if jogador1[3] > 5:
        jogador1[3] = 5
    if jogador2[3] > 5:
        jogador2[3] = 5
    print("--------------------------------------------------")
    print("",nome1,"HP:",jogador1[2],"     Pontos:",jogador1[3],"\n",nome2,"HP:",jogador2[2],"     Pontos:",jogador2[3])
    print("--------------------------------------------------")


    print("\n\n\n\n")

    print("**************************************************")
    print("Rodada:", turno,"\n")
    print(str(nome1)+":")
    acao1 = input("Digite sua ação: A, D ou S: ")
    print("\n"+str(nome2) + ":")
    acao2 = input("Digite sua ação: A, D ou S: ")
    print("**************************************************\n")



    if acao1 == 'a' and acao2 == 'a':
        jogador1[2],jogador2[2] = play.atkatk(jogador1[2],jogador2[2],jogador1[0],jogador2[0])
        jogador1[3] += 1
        jogador2[3] += 1



    if acao1 == 'a' and acao2 == 'd':
        jogador2[2] = play.atkdef(jogador2[2],jogador1[0],jogador2[1])
        jogador1[3] += 1
        jogador2[3] += 2

        print("\n------------------------------------------------------")

    if acao1 == 'd' and acao2 == 'a':
        jogador1[2] = play.defatk(jogador1[2], jogador2[0], jogador1[1])
        jogador1[3] += 2
        jogador2[3] += 1


    if acao1 == 'd' and acao2 == 'd':
        play.defdef()
        print("\n------------------------------------------------------")


    if acao1 == 's' and acao2 == 'a':
        if jogador1[3] >= 5:
            jogador2[3] += 1
            jogador1[2],jogador1[3],jogador2[2] = play.s1 (jogador1[0],jogador1[2],jogador2[0],jogador2[2])
        else:
            mensagem()
    if acao1 == 'a' and acao2 == 's':
        if jogador2[3] >=  5:
            jogador2[2], jogador2[3], jogador1[2] = play.s2(jogador2[0], jogador2[2], jogador1[0], jogador1[2])
            jogador1[3] += 1
        else:
            mensagem()

    if acao1 == 's' and acao2 == 's':
        if jogador1[3] >= 5 and jogador2[3] >= 5:
            jogador1[2], jogador1[3], jogador2[2], jogador2[3] = play.s1s2(jogador1[0], jogador1[2], jogador2[0], jogador2[2])
        else:
            mensagem()

    if acao1 == "s" and acao2 == "d":
        print("Não é possivel defender o ataque especial, digite sua ação novamente.")

    if acao1 == "d" and acao2 == "s":
        print("Não é possivel defender o ataque especial, digite sua ação novamente.")


    if jogador1[2] <= 0 and jogador2[2] <= 0:
        print("Empate")
        controle = False
    elif jogador1[2] <= 0:
        print("Jogador2 Venceu: ",nome2)
        controle = False
    elif jogador2[2] <= 0:
        print("Jogador1 Venceu: ",nome1)
        controle = False

    turno += 1


print("\n\n\n\n\n\n\n\n")
print("Game Over")




















