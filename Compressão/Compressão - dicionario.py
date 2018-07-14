"""______________________________________________________________________________________________
|   Diagnóstico e Solução de Problemas de Tecnologia da Informação -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva                                                               |
|   Programa :  Compressão arquivos de texto por dicionário                                      |
|   Data : 06/04/2018                                                                            |
|________________________________________________________________________________________________|
"""
import os

pastaEntrada = 'Entrada/'
pastaSaida = 'Saida/'
textoOriginal = []
caracteresSeparados = []
textoComprimido = []
textoParaDescomprimir = []

dicionario = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12',
              'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
              'x': '24', 'y': '25', 'z': '26', 'A': '27', 'B': '28', 'C': '29', 'D': '30', 'E': '31', 'F': '32', 'G': '33', 'H': '34',
              'I': '35', 'J': '36', 'K': '37', 'L': '38', 'M': '39', 'N': '40', 'O': '41', 'P': '42', 'Q': '43', 'R': '44', 'S': '45',
              'T': '46', 'U': '47', 'V': '48', 'W': '49', 'X': '50', 'Y': '51', 'Z': '52', ' ': '53'}


def transformarEmCaracter():
    textoTemp = []
    for i in range(len(caracteresSeparados)):
        try:
            textoTemp.append(dicionario[caracteresSeparados[i]])
        except KeyError:
            textoTemp.append(caracteresSeparados[i])

    aux = ''.join(str(x) for x in textoTemp)
    return aux


def criarArquivoComprimido():
    arquivo.seek(0)
    textoComprimido.clear()
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
    arquivo.close()

    print('\n-----------------------\nConcluído com sucesso!\n-----------------------\n')


def descomprimirArquivo():
    textoTemp = []
    arquivoParaDescomprimir = open(pastaSaida + arquivoNome, 'w')
    arquivoParaDescomprimir.seek(0)

    for linhas in arquivo:
        textoParaDescomprimir.append(linhas)

    for i in range(len(textoParaDescomprimir)):
        for letra in textoParaDescomprimir[i]:
            caracteresSeparados.append(letra)
    contador = 0
    while contador < len(caracteresSeparados) - 1:
        aux = caracteresSeparados[contador] + caracteresSeparados[contador + 1]
        for key, value in dicionario.items():
            if value == aux:
                textoTemp.append(key)
                contador += 1
        contador += 1

    for i in range(len(textoTemp)):
        arquivoParaDescomprimir.write(textoTemp[i])
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
            print('\nO arquivo: ' + arquivoNome + ' possui ' + str(
                os.stat(pastaEntrada + arquivoNome).st_size) + ' Bytes')
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
            print('\nO arquivo: [Comprimido] ' + arquivoNome + ' possui ' + str(
                os.stat(pastaEntrada + arquivoNome).st_size) + ' Bytes')
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
