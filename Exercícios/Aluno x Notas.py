"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Alunos X Notas                   |
|   Data : 06/04/2018                            |
|________________________________________________|
"""


nomes = ['Lucas', 'Pedro', 'Joelson', 'Judite', 'Carla', 'Claudia', 'Maria', 'Mario', 'Roberta', 'Ricardo']
notas = ([0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0])

for i in range(10):
    for j in range(5):
        notas[i][j] = float(input('Digite a {}º nota do {}: '.format(j + 1, nomes[i])))

    print('')
maior, menor = notas[0][0], notas[0][0]

print('\t\t\t\t\t\t\tNotas\t\t\t\t\t\tMedia\n')

for i in range(10):
    print('{}\t\t'.format(nomes[i]), end='')
    media = 0
    for j in range(5):

        if maior < notas[i][j]:
            maior = notas[i][j]
        if menor > notas[i][j]:
            menor = notas[i][j]

        print(notas[i][j], '\t',  end='')
        media += notas[i][j]
    print('\t{}'.format(media / 5), end='')
    print('')

print('\nMaior nota digitada: {}\t\tMenor nota digitada: {}'.format(maior, menor))

