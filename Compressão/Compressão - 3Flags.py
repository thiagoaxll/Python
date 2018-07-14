"""______________________________________________________________________________________________
|   Diagnóstico e Solução de Problemas de Tecnologia da Informação -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva                                                               |
|   Programa :  Compressão arquivos de texto                                                     |
|   Data : 06/04/2018                                                                            |
|________________________________________________________________________________________________|
"""
import os
pastaEntrada = 'Entrada/'
pastaSaida = 'Saida/'
flag, flag2, flag3 = '¥', 'Æ', '€'
textoOriginal = []
caracteresSeparados = []
textoComprimido = []
textoParaDescomprimir = []


def verificarIncidencia(incidencia, textoTemp, i):
    if incidencia == 0:
        textoTemp.append(caracteresSeparados[i])
    elif incidencia == 1:
        textoTemp.append(caracteresSeparados[i - 1])
        textoTemp.append(caracteresSeparados[i])
    elif incidencia == 2:
        textoTemp.append(caracteresSeparados[i - 1])
        textoTemp.append(caracteresSeparados[i - 2])
        textoTemp.append(caracteresSeparados[i])
    elif 2 < incidencia < 9:
        textoTemp.append(flag)
        textoTemp.append(incidencia + 1)
        textoTemp.append(caracteresSeparados[i])
    elif 9 <= incidencia <= 98:
        textoTemp.append(flag2)
        textoTemp.append(incidencia + 1)
        textoTemp.append(caracteresSeparados[i])
    elif 99 <= incidencia <= 999:
        textoTemp.append(flag3)
        textoTemp.append(incidencia + 1)
        textoTemp.append(caracteresSeparados[i])
    incidencia = 0
    return incidencia, textoTemp


def transformarEmCaracter():
    incidencia = 0
    textoTemp = []
    for i in range(len(caracteresSeparados)):
        if i < len(caracteresSeparados) - 1:
            if caracteresSeparados[i] == caracteresSeparados[i + 1] and incidencia < 998:
                incidencia += 1
            else:
                incidencia, textoTemp = verificarIncidencia(incidencia, textoTemp, i)
        else:
            incidencia, textoTemp = verificarIncidencia(incidencia, textoTemp, i)

    aux = ''.join(str(x) for x in textoTemp)
    return aux


def criarArquivoComprimido():
    arquivo.seek(0)
    textoComprimido.clear()
    print('Aguarde . . .\nProcessando . . .')
    for linhas in arquivo:
        textoOriginal.append(linhas)

    for i in range(len(textoOriginal)):
        for letra in textoOriginal[i]:
            caracteresSeparados.append(letra)
        textoComprimido.append(transformarEmCaracter())
        caracteresSeparados.clear()

    arquivoComprimido = open(pastaSaida + arquivoNome, 'w')

    for i in range(len(textoOriginal)):
        arquivoComprimido.write(textoComprimido[i])
    arquivoComprimido.close()
    print(pastaSaida + arquivoNome)
    print('\nO arquivo: [Comprimido] ' + arquivoNome + '  possui ' + str(os.stat(pastaSaida + arquivoNome).st_size) + ' Bytes')
    print('O arquivo é {:.2f} % menor.'.format(100 - (100 * os.stat(pastaSaida + arquivoNome).st_size / os.stat(pastaEntrada + arquivoNome).st_size)))
    arquivo.close()
    print('\n-----------------------\nConcluído com sucesso!\n-----------------------\n')


def descomprimirArquivo():
    textoTemp = []
    contador = 0
    arquivoParaDescomprimir = open(pastaSaida + arquivoNome, 'w')
    arquivoParaDescomprimir.seek(0)

    print('Aguarde . . .\nProcessando . . .')
    for linhas in arquivo:
        textoParaDescomprimir.append(linhas)

    for i in range(len(textoParaDescomprimir)):
        for letra in textoParaDescomprimir[i]:
            caracteresSeparados.append(letra)

    while contador < len(caracteresSeparados):
        if caracteresSeparados[contador] == flag:
            for j in range(1, int(caracteresSeparados[contador + 1])):
                textoTemp.append(caracteresSeparados[contador + 2])
            contador += 2
        if caracteresSeparados[contador] == flag2:
            aux = str(caracteresSeparados[contador + 1] + caracteresSeparados[contador + 2])
            for j in range(1, int(aux)):
                textoTemp.append(caracteresSeparados[contador + 3])
            contador += 3
        if caracteresSeparados[contador] == flag3:
            aux = str(caracteresSeparados[contador + 1] + caracteresSeparados[contador + 2] + caracteresSeparados[contador + 3])
            for j in range(1, int(aux)):
                textoTemp.append(caracteresSeparados[contador + 4])
            contador += 4
        else:
            textoTemp.append(caracteresSeparados[contador])
            contador += 1

    for i in range(len(textoTemp)):
        arquivoParaDescomprimir.write(textoTemp[i])
    print('\nO arquivo: [Descomprimido] ' + arquivoNome + '  possui ' + str(os.stat(pastaSaida + arquivoNome).st_size) + ' Bytes')
    print('O arquivo é {:.2f} % maior.'.format((100 * os.stat(pastaSaida + arquivoNome).st_size / os.stat(pastaEntrada + arquivoNome).st_size)))
    arquivoParaDescomprimir.close()
    arquivo.close()
    print('\n-----------------------\nConcluído com sucesso!\n-----------------------\n')


try:  # Cria a pasta Entrada e Saida caso nao existam.
    os.mkdir('Saida')
    os.mkdir('Entrada')
except FileExistsError:
    pass

while True:
    print('Escolha uma opção:\n|1 - Comprimir arquivo| |2 - Descomprimir arquivo| |3 - Intruções| |4 - Sair|')
    opcao = input('Entre com uma opção: ')
    if opcao is not "1" and opcao is not "2" and opcao is not "3" and opcao is not "4":
        print('Opção Inválida.')
    elif opcao == '1':
        arquivoNome = input('Exemplo:\tArquivo.txt\nQual o nome do arquivo que deseja comprimir: ')
        try:
            arquivo = open(pastaEntrada + arquivoNome, 'r')
            print('\nO arquivo: ' + arquivoNome + ' possui ' + str(os.stat(pastaEntrada + arquivoNome).st_size) + ' Bytes')
            if os.stat(pastaEntrada + arquivoNome).st_size == 0:
                print('Arquivo vazio.\n')
            else:
                caracteresSeparados.clear()
                textoOriginal.clear()
                criarArquivoComprimido()

        except FileNotFoundError or FileExistsError:
            print('\n--------------------------------------------------\nErro\nEsse arquivo não existe.\n'
                  'O arquivo deve estar dentro da Pasta .../Entrada\n--------------------------------------------------\n')

    elif opcao == "2":
        arquivoNome = input('Exemplo:\tArquivo.txt\nQual o nome do arquivo que deseja descomprimir: ')
        try:
            arquivo = open(pastaEntrada + arquivoNome, 'r')
            print('\nO arquivo: [Comprimido] ' + arquivoNome + ' possui ' + str(os.stat(pastaEntrada + arquivoNome).st_size) + ' Bytes')
            if os.stat(pastaEntrada + arquivoNome).st_size == 0:
                print('Arquivo vazio\n')
            else:
                caracteresSeparados.clear()
                textoParaDescomprimir.clear()
                descomprimirArquivo()
        except FileNotFoundError or FileExistsError:
            print('\n--------------------------------------------------\nErro\nEsse arquivo não existe.\n'
                  'O arquivo deve estar dentro da Pasta .../Entrada\n--------------------------------------------------\n')
    elif opcao == "3":
        print(
            '\n\n-----------------------------------------------------------------------------------------------------------------')
        print(
            'Para comprimir o arquivo:\nColoque o arquivo descomprimido na pasta \"Entrada\" que se encontra na Raiz do programa.')
        print(
            'Entre com a opção 1 no menu.\nDigite o nome do seu arquivo: \t\"exemplo.txt\"\nRetire o arquivo na pasta \"Saida.\"')
        print(
            '\nPara descomprimir o arquivo:\nColoque o arquivo Comprimido na pasta \"Entrada\" que se encontra na Raiz do programa.')
        print(
            'Entre com a opção 2 no menu.\nDigite o nome do seu arquivo: \t\"exemplo.txt\"\nRetire o arquivo na pasta \"Saida.\"')
        print(
            '-----------------------------------------------------------------------------------------------------------------\n')
    else:
        break
