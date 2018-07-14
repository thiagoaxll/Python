"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Times x Pontos                   |
|   Data : 20/04/2018                            |
|________________________________________________|
"""

times = ['Corinthians', 'São Paulo', 'Palmeiras', 'Santos', 'Flamengo']
tabela = [[0 for i in range(30)] for j in range(5)]
pontos = 0
media = 0
campeao = None

for i in range(5):
    totalPontos = 0
    for j in range(30):
        tabela[i][j] = int(input('Digite quantos pontos o {} fez na {}º rodada: '.format(times[i], j + 1)))
        media += tabela[i][j]
        totalPontos += tabela[i][j]
    print('--------------------------------------------------------------------------------')
    if i == 0:
        pontos = totalPontos
        campeao = times[i]
    elif totalPontos > pontos:
        pontos = totalPontos
        campeao = times[i]

media = media/((j + 1) * 5)

print('\nTime Campeão: {}\t|\t{} Pontos\n\nMedia de pontos do campeonato: {}'.format(campeao, pontos, media))



