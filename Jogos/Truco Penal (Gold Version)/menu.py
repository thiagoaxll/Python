# *********************************************************************************************
# ******   FATEC - Faculdade de Tecnologia de Carapicuiba                                ******
# ******   Funcao: responsavel por efetuar o processamento principal do jogo com todas   ******
# ******           as regras, definicoes e comportamento da aplicacao cliente            ******
# ******   Nome..: Diego Vinicius de Mello Munhoz                                        ******
# ******           Thiago Zacarias da Silva                                              ******
# ******           Victor Otavio Ponciano                                                ******
# ******   Data..: 07/07/2018                                                            ******
# *********************************************************************************************

import os
import pygame
import resources
import config
import textos
import random
import socket
import compress

os.environ['SDL_VIDEO_CENTERED'] = '1' #Centraliza a tela da pygame ao inicializar / deve ser declarada antes de iniciar engine

# Dicionário de posicionamento do menu
#                       XY Botao,  XY Texto
menuDic = {'btStart': [(14, 252), (80, 270)], 'btConfig': [(14, 416), (40, 429)], 'posBandeira': (710, 10),
           'btAvatar': [(14, 334), (80, 348)], 'nomeJogo': (0, 0), 'btVoltar': [(488, 529), (560, 540)],
           'btLeft': (7, 434), 'btRight': (263, 434), 'opcaoIdioma': (52, 434), 'nomeMenu': (325, 205), 'posAvatarMenu': (342, 240), 'posAvatarLoja': (185, 266), 'btLeftAvatar': (20, 249), 'btRightAvatar': (130, 249),
           'nomeTexto': (300, 514), 'contrato1': (325, 30), 'contrato2': (50, 120), 'contrato3': (30, 200), 'contrato4': (350, 250), 'contrato5': (50, 320),
           'btnServer': (121, 246), 'btnClient': (492, 246), 'btnConfirmServer': (595, 431),  'ipTxt': (248, 260), 'posEspelho': (300, 213), 'nomeSalaEspera': (14, 357), 'posAvatarSalaEspera': (24, 247), 'txtLobby': (20, 20),
           'txtAguardando': (20, 50), 'txtErrorLobby': (50, 70), 'btnMudarNome': (12, 220), 'btnCredito': (12, 300), 'txtMudarNome': (26, 235), 'txtCreditos': (50, 315), 'btnSingle': (626, 317), 'btnMult': (626, 252),
           'txtSinglePlayer': (642, 337), 'txtMultiPlayer': (642, 271), 'btnRegras': (12, 529), 'txtRegras': (42, 549), 'imgRegras': (0, 0)}
# /Dicionário de posicionamento do menu


# Dicionário de posicionamento In-Game
jogoDic = {'posCartaPlayer1': [(309, 525), (375, 525), (441, 525)], 'posCartaPlayer2': [(716, 388), (716, 340), (716, 290)], 'posCartaPlayer3': [(16, 278), (16, 328), (16, 378)],
           'posJogada': [(343, 290), (416, 388), (546, 278)], 'posBralho': (192, 290), 'posCartaVirada': (242, 290), 'posPontoJogador1': (680, 540), 'posPontoJogador2': (680, 100), 'posPontoJogador3': (68, 100),
           'posTextoRodada': (292, 8), 'posTextoNomeJogador': [(540, 545), (540, 112), (126, 112)], 'posBgFundoAvatar': [(675, 475), (675, 23), (7, 24)], 'posAvatar': [(740, 490), (730, 34), (7, 34)],
           'posAvatarVencedor': (340, 208), 'posNomeVencedor': (333, 425), 'posTextoVencedor': (292, 8), 'posTxtPerdedor': [(228, 540), (449, 540)], 'posPerdedores': [(228, 483), (449, 483)]}
# /Dicionário de posicionamento In-Game

# instanciamento de variáveis de imagem previamente importadas na classe resources
botao = pygame.image.load(resources.BOTAO)
botao2 = pygame.image.load(resources.BOTAO2)
backgroundMenu = pygame.image.load(resources.BACKGROUND_MENU)
backgroundJogo = pygame.image.load(resources.BACKGROUND_JOGO)
baralhoImg = pygame.image.load(resources.BARALHO)
logo = (resources.spriteLogo())
imgProjetoK = pygame.image.load(resources.PROJETOK)
imgPKFatec = pygame.image.load(resources.PROJETOK_FATEC)
imgEspelho = pygame.image.load(resources.ESPELHO)
fundoCarta = pygame.image.load(resources.FUNDO_CARTA)
fundoAvatarBg = pygame.image.load(resources.FUNDO_AVATAR)
spriteSheetAvatar = (resources.spriteAvatar())
bandeira = resources.bandeiraSprite()
paginaPortugues = resources.pagina_portugues()
paginaIngles = resources.pagina_ingles()
cgInicial = (resources.animInicial())
left = pygame.image.load(resources.LEFT)
right = pygame.image.load(resources.RIGHT)
leftRegras = pygame.image.load(resources.LEFT)
rightRegres = pygame.image.load(resources.RIGHT)

turnoImg = pygame.image.load(resources.TURNO)
vencedorBg = pygame.image.load(resources.VENCEDOR_BG)
lobbyBg = pygame.image.load(resources.LOBBY_BG)
imgRegras = (resources.spriteRegrasPt())
imgRegrasIngles = (resources.spriteRegrasIng())

#Intsanciamento da tela principal, e Título da janela, além de setar o clock ou relógio interno da aplucação
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(config.TITULO)
clock = pygame.time.Clock()

# inicialização de audio
pygame.mixer.init()
pygame.mixer.music.load(resources.MENU_MUSIC)#Carrega música de background
fxCardAnim = pygame.mixer.Sound(resources.FX_CARD)#Carrega SFX de cartas
fxBtn = pygame.mixer.Sound(resources.FX_CLICK) #Carrega SFX de click


#Váriaveis globais para controle de tempo
global cronometro1, cronometro2, contadorG, pagina
cronometro1, cronometro2, contadorG = 0, 0, 0

global paginaRegras

paginaRegras = 0

#variáveis para controle de socket em partidas multiplayer
global s, host, porta, instruction, player, multiplayer, estadoJogo, animator, animation

# /inicialização das Variaveis instanciadas
pagina = 0
animator = 0 #Controle de animação
animation = 0
estadoJogo = 0
multiplayer = True
instruction = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
player = None
porta = 8291
host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pygame.font.init()

"""Metodo responsavel por efetuar a intancia da classe COMPRESS, listar todos os arquivos
existentes no diretorio /imagens, apos isso chamar a rotina responsavel por comprimir os arquivos"""
def comprimir_imagens():
    diretorio = 'imagens'

    comprimir = compress.ComprimirImagem()

    for name in os.listdir(diretorio):
        if ('jpeg' in name) or ('jpg' in name) or ('png' in name):
            comprimir.processarArquivo(os.path.join(diretorio,name))

"""Metodo responsavel por efetuar a intancia da classe COMPRESS, listar todos os arquivos
de bakckup existentes no diretorio /imagens, apos isso chamar a rotina responsavel por descomprimir os arquivos"""
def descomprimir_imagens():
    diretorio = 'imagens'

    descomprimir = compress.DescomprimirImagem()

    for name in os.listdir(diretorio):
        if ('backup' in name) and ('.py' not in name):
            descomprimir.processarArquivo(os.path.join(diretorio,name))

"""Metodo responsavel por controlar o comportamento da tela de captura do nome do jogador, 
   controlando idioma, colisao e input de informacao"""


#Método responsável pela captura e configuração do nome do jogador, recebe como parâmetros a biblioteca com os textos do idioma selecionado pelo jogador, o nome do jogador e o identificador do idioma
def enterNomePlayer(idioma, nome, idiomaTexto):
    font = pygame.font.Font('font/Pixellari.ttf', 45)#declaração da fonte com tamanho 45
    font2 = pygame.font.Font('font/Pixellari.ttf', 35)#declaração da fonte com tamanho 35

    mouse = pygame.mouse.get_pos() #Captura e salva a posição do mouse em uma variável
    screen.fill(resources.PRETO) #Preenche  background dessa tela em preto

    retBandeira = pygame.Rect(menuDic['posBandeira'][0], menuDic['posBandeira'][1], bandeira[0].get_width(), bandeira[0].get_height())#Cria o retângulo de colisão para o ícone da bandeira que fará a seleção de linguagem da tela

    #Se o idioma selecionado pleo player for português
    if idioma['idioma'] == 'portugues':
        #Se o retângulo do icone de bandeira colidir com o mnouse
        if retBandeira.collidepoint(mouse[0], mouse[1]):
            #Selecionamos e anexamos a tela o ícone da bandeira do Brasil com a borda branca
            screen.blit(bandeira[3], menuDic['posBandeira'])
        else:
            #Caso contrário anexamos a bandeira do Brasil sem borda
            screen.blit(bandeira[2], menuDic['posBandeira'])
    #Se o idioma selecionado for inglês
    else:
        #Se hover colião do ícone com o mouse
        if retBandeira.collidepoint(mouse[0], mouse[1]):
            #Anexamos a imagem da bandeira americana com borda branca
            screen.blit(bandeira[1], menuDic['posBandeira'])
        else:
            #Caso contrário mostramos bandeira sem bordas
            screen.blit(bandeira[0], menuDic['posBandeira'])

    texto = font.render(nome, 1, resources.BRANCO) #Definimos o render que irá mostrar o texto de nome na tela, na cor branca em contraste com o background


    #Bloco que anexa o texto da tela de contrato de acordo com o idioma selecionado
    screen.blit(font2.render((idioma['contrato1']), 1, resources.BRANCO), menuDic['contrato1'])
    screen.blit(font2.render((idioma['contrato2']), 1, resources.BRANCO), menuDic['contrato2'])
    screen.blit(font2.render((idioma['contrato3']), 1, resources.BRANCO), menuDic['contrato3'])
    screen.blit(font2.render((idioma['contrato4']), 1, resources.BRANCO), menuDic['contrato4'])
    screen.blit(font2.render((idioma['contrato5']), 1, resources.BRANCO), menuDic['contrato5'])

    nome = nome.split() #Essa linha divide a string nome em uma lista coim cada letra contida em nome

    #laço para captura de eventos
    for event in pygame.event.get():
        #Se o evento chamado for do tipo QUIT
        if event.type == pygame.QUIT:
            #Realiza a rotina de descompressão da imagem
            descomprimir_imagens()
            #Fecha a aplicação
            pygame.quit()
        #Eventos de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Se hover click de mopuse enquanto há uma colisão com o ícone das bandeiras
            if retBandeira.collidepoint(mouse):
                #Se o idioma setado for português
                if idioma['idioma'] == 'portugues':
                    idioma = textos.dicIngles #Selecionamos o dicionário de palavras em inglês
                    idiomaTexto = 'Inglês' #Setamos o identificador de idioma como Inglês
                #Se o idioma for inglês
                else:
                    idioma = textos.dicPortugues #Selecionamos o dicionário de palavras em portugês
                    idiomaTexto = 'Português' # Setamos o identificador para português

        #Captura do evento de teclas
        if event.type == pygame.KEYDOWN:
            #Se a tecla pressionada for alfabética ou númérica
            if event.unicode.isalpha() or event.unicode.isnumeric():
                fxBtn.play() #Aciona o sfx de botão
                #para cada letra na lista nome
                for i in range(len(nome)):
                    #Se as letras forem o padrão _
                    if nome[i] == '_':
                        #substitui o _ pela letra ou número digitado
                        nome[i] = event.unicode
                        break #Sai do laço
            #Se a tecla pressionada for o backspace
            if event.key == pygame.K_BACKSPACE:
                fxBtn.play() #Aciona o sfx de botão
                #para cada letra na lista nome
                for i in range(len(nome)):
                    #Se a letra selecionada for o padrão _
                    if nome[i] == '_':
                        #substituímos a letra da esquerda por _
                        nome[i - 1] = '_'
                        break
                    #Se a penúltima letra da lista for igual a letra selecionada
                    elif i == (len(nome) - 1):
                        nome[i] = '_'
            #Se a tecla pressionada for a espaço
            if event.key == pygame.K_SPACE:
                fxBtn.play()
                #Para cada letra na lista nome
                for i in range(len(nome)):
                    #se o elemento for o padrão _
                    if nome[i] == '_':
                        nome[i] = '-'#substituí o undeline por traço
                        break
            #Se for pressionada a tecla de confirmação
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                fxBtn.play()
                #reagrupa todas as letras em em uma variável  e substituí os traços por espaços
                nomeTemp = ' '.join(str(nome) for nome in nome)
                nomeTemp = nomeTemp.replace('_', '')
                nomeTemp = nomeTemp.replace(' ', '')
                #Se a variável não estiver vazia
                if nomeTemp is not '':
                    return 'menu', nomeTemp, idioma, idiomaTexto #Retorna o próximo estado, o nome digitado, a bibliotaca de idioma que será utilizada e o identificador de idioma

    nomeTemp = ' '.join(str(nome) for nome in nome)#captura a entrada de nome padrão com _ e salva na veriável nomeTemp
    screen.blit(texto, menuDic['nomeTexto'])#mostra para o usuário o texto de nome

    return 'escreverNome', nomeTemp, idioma, idiomaTexto#Retorna o próximo estado, o nome digitado, a bibliotaca de idioma que será utilizada e o identificador de idioma

"""Metodo responsavel por controlar todo o processamento do menu principial, suas animacoes, 
   definicoes de fontes, colisoes, chamada das telas de configuracao, avatar e inicio do jogo"""
def menu(idioma, nome, avatarJogador, estadoMenu):
    #Acessa as variáveis de escopo global
    global animator, multiplayer

    #Se a música de fundo estiver tocando
    if pygame.mixer.music.get_busy():
        #Não fazer nada
        pass
    #Caso contrário
    else:
        #Executa a música de background
        pygame.mixer.music.play()
    #Definição das fontes
    font = pygame.font.Font('font/Pixellari.ttf', 45)
    font2 = pygame.font.Font('font/Pixellari.ttf', 35)
    font3 = pygame.font.Font('font/Pixellari.ttf', 25)
    #captura da posição do Mouse
    mouse = pygame.mouse.get_pos()
    #Adiciona a imagem de plano de fundo
    screen.blit(backgroundMenu, (0, 0))
    #Adiciona imagem do espelho
    screen.blit(imgEspelho, menuDic['posEspelho'])
    #Adiciona retângulo de colisão para botões de menu
    botaoRetIniciar = pygame.Rect(menuDic['btStart'][0][0], menuDic['btStart'][0][1], botao.get_width(), botao.get_height())
    botaoRetConfigurar = pygame.Rect(menuDic['btConfig'][0][0], menuDic['btConfig'][0][1], botao.get_width(), botao.get_height())
    botaoRetAvatar = pygame.Rect(menuDic['btAvatar'][0][0], menuDic['btAvatar'][0][1], botao.get_width(), botao.get_height())

    #Retângulo de colisão submenu
    botaoRetSingle = pygame.Rect(menuDic['btnSingle'][0], menuDic['btnSingle'][1], botao.get_width(), botao.get_height())
    botaoRetMult = pygame.Rect(menuDic['btnMult'][0], menuDic['btnMult'][1], botao.get_width(), botao.get_height())

    #Se o estado do menu for jogar
    if estadoMenu == 'jogar':
        #Se o mouse estiver sob o botão Single Player
        if botaoRetSingle.collidepoint(mouse):
            #Adiciona a variação de cor no botão
            screen.blit(botao2, menuDic['btnSingle'])
        #Se não hover colisão com o mouse
        else:
            #Adiciona a versão do botão padrão
            screen.blit(botao, menuDic['btnSingle'])
        if botaoRetMult.collidepoint(mouse):
            screen.blit(botao2, menuDic['btnMult'])
        else:
            screen.blit(botao, menuDic['btnMult'])
        #Adiciona os textos do submenu Jogar
        screen.blit(font3.render((idioma['umJogador']), 1, resources.BRANCO), menuDic['txtSinglePlayer'])
        screen.blit(font3.render((idioma['multiJogador']), 1, resources.BRANCO), menuDic['txtMultiPlayer'])

    #Se o mouse estiver sobre o botão iniciar
    if botaoRetIniciar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btStart'][0])
    else:
        screen.blit(botao, menuDic['btStart'][0])
    screen.blit(font2.render((idioma['iniciar']), 1, resources.BRANCO), (menuDic['btStart'][1]))

    #Se o mouse estiver sob o botão Configurar
    if botaoRetConfigurar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btConfig'][0])
    else:
        screen.blit(botao, menuDic['btConfig'][0])
    #Adiciona texto Configurar na tela
    screen.blit(font2.render((idioma['configurar']), 1, resources.BRANCO), menuDic['btConfig'][1])

    #Se o mouse estiver sobre o botão Avatar
    if botaoRetAvatar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btAvatar'][0])
    else:
        screen.blit(botao, menuDic['btAvatar'][0])
    #Adicion o texto avatar ao menu
    screen.blit(font2.render((idioma['avatar']), 1, resources.BRANCO), menuDic['btAvatar'][1])

    #Adiciona o nome do jogador a tela de menu
    screen.blit(font.render(nome, 1, resources.BRANCO), menuDic['nomeMenu'])

    #Controle de animação do personagem
    if animator < 30:
        #Anexa a imagem do avatar do jogador no menu principal(Ecalona a imagem em 2X seu tamanho e inverte sua orientação padrão da spritesheet)
        screen.blit(pygame.transform.flip(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador]), -1, 0), menuDic['posAvatarMenu'])
    else:
        # Anexa a imagem alternativa do avatar do jogador no menu principal(Ecalona a imagem em 2X seu tamanho e inverte sua orientação padrão da spritesheet)
        screen.blit(pygame.transform.flip(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador + 1]), -1, 0), menuDic['posAvatarMenu'])

    #Captura os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            descomprimir_imagens()
            pygame.quit()
        #Se o mouse clicar
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Se há colisão com o botão iniciar
            if botaoRetIniciar.collidepoint(mouse):
                fxBtn.play()
                #Seta o estado do menu para o submenu jogar
                estadoMenu = 'jogar'
            #Se há colisão do mouse com o botão configurar
            elif botaoRetConfigurar.collidepoint(mouse):
                fxBtn.play()
                #Não é aberto o estado de submenu jogar
                estadoMenu = ''
                return 'configuracao', avatarJogador, estadoMenu #Retorna o estado de jogo configurar, o avatar atual do jogador e se o estado de submenu está ativado ou não

            #Se há colisão do mouse com o botão avatar
            elif botaoRetAvatar.collidepoint(mouse):
                fxBtn.play()
                estadoMenu = ''
                return 'avatar', avatarJogador, estadoMenu#Retorna o estado de jogo Avatar, o avatar atual do jogador e se o estado de submenu está ativado ou não

            #Se o estado de submenu Jogar estiver aivado
            if estadoMenu == 'jogar':
                #Se o mouse estiver sobre o botão singleplayer
                if botaoRetSingle.collidepoint(mouse):
                    #seta a varável global multiplayer para falso
                    multiplayer = False
                    fxBtn.play()
                    estadoMenu = ''
                    return 'jogandoSingle', avatarJogador, estadoMenu#Retorna o estado de jogo para jogando Single pllayer, o avatar selecionado do jogador e o estado do submenu
                #Se o mouse estiver sobre o botão multiplayer
                elif botaoRetMult.collidepoint(mouse):
                    #seta a variável multiplayer como true
                    multiplayer = True
                    fxBtn.play()
                    estadoMenu = ''
                    return 'aguardandoJogadores', avatarJogador, estadoMenu#Retorna o estado de jogo para a tela de sala de espera

    return 'menu', avatarJogador, estadoMenu #Retorna o estado padrão de menu, avatar selecionado pelo jogador

"""Metodo responsavel por controlar todo o processamento da tela de configuracao, suas animacoes, 
   definicoes de fontes, colisoes, chamada das telas de regras, mudanca de nome e creditos do jogo 
   e troca de idioma"""
def configuracao(idioma, idiomaTexto, nome):
    #Acessa a variável global estadoJogo
    global estadoJogo, paginaRegras

    paginaRegras = paginaRegras

    #Controle de fluxo da música
    if pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.play()

    #Definição de fontes dos botões
    font = pygame.font.Font('font/Pixellari.ttf', 45)
    font2 = pygame.font.Font('font/Pixellari.ttf', 35)
    font3 = pygame.font.Font('font/Pixellari.ttf', 25)
    font4 = pygame.font.Font('font/Pixellari.ttf', 20)

    #Posicionamento do mouse
    mouse = pygame.mouse.get_pos()

    #Background da tela configurações
    screen.blit(backgroundMenu, (0, 0))



    #Configurações de retângulos dos botões
    botaoRetVoltar = pygame.Rect(menuDic['btVoltar'][0][0], menuDic['btVoltar'][0][1], botao.get_width(), botao.get_height())
    botaoRetLeft = pygame.Rect(menuDic['btLeft'][0], menuDic['btLeft'][1], left.get_width(), left.get_height())
    botaoRetRight = pygame.Rect(menuDic['btRight'][0], menuDic['btRight'][1], right.get_width(), right.get_height())
    botaoRetLeftRegras = pygame.Rect(690,380, leftRegras.get_width(), leftRegras.get_height())
    botaoRetRightRegras = pygame.Rect(730,380, rightRegres.get_width(), rightRegres.get_height())
    botaoRetMudarNome = pygame.Rect(menuDic['btnMudarNome'][0], menuDic['btnMudarNome'][1], botao.get_width(), botao.get_height())
    botaoRetCredito = pygame.Rect(menuDic['btnCredito'][0], menuDic['btnCredito'][1], botao.get_width(), botao.get_height())
    botaoRetRegras = pygame.Rect(menuDic['btnRegras'][0], menuDic['btnRegras'][1], botao.get_width(), botao.get_height())

    #Adiciona botões a tela
    screen.blit(left, menuDic['btLeft'])
    screen.blit(right, menuDic['btRight'])
    #Adiciona texto de seleção de idioma
    screen.blit(font.render(idiomaTexto, 1, resources.BRANCO), menuDic['opcaoIdioma'])

    #Efeitos de colisão do mouse com os botões
    if botaoRetVoltar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btVoltar'][0])
    else:
        screen.blit(botao, menuDic['btVoltar'][0])
    screen.blit(font2.render(idioma['voltar'], 1, resources.BRANCO), menuDic['btVoltar'][1])

    if botaoRetMudarNome.collidepoint(mouse):
        screen.blit(botao2, menuDic['btnMudarNome'])
    else:
        screen.blit(botao, menuDic['btnMudarNome'])

    if botaoRetCredito.collidepoint(mouse):
        screen.blit(botao2, menuDic['btnCredito'])
    else:
        screen.blit(botao, menuDic['btnCredito'])

    if botaoRetRegras.collidepoint(mouse):
        screen.blit(botao2, menuDic['btnRegras'])
    else:
        screen.blit(botao, menuDic['btnRegras'])

    #Adiciona textos dos botões em suas devidas áreas
    screen.blit(font2.render(idioma['regras'], 1, resources.BRANCO), menuDic['txtRegras'])
    screen.blit(font2.render(idioma['mudarNome'], 1, resources.BRANCO), menuDic['txtMudarNome'])
    screen.blit(font2.render(idioma['credito'], 1, resources.BRANCO), menuDic['txtCreditos'])

    #Se o esstado do jogo for o submenu créditos
    if estadoJogo == 'creditos':
        #Mostra na tela as informações de créditos do jogo
        screen.blit(font3.render('Diego Munhoz', 1, resources.BRANCO), (300, 220))
        screen.blit(font4.render('Programing, Compress Programing', 1, resources.BRANCO), (325, 245))
        screen.blit(font3.render('Thiago Zacarias da Silva', 1, resources.BRANCO), (300, 268))
        screen.blit(font4.render('Programing, Network Programing', 1, resources.BRANCO), (325, 289))
        screen.blit(font3.render('Victor Ponciano', 1, resources.BRANCO), (300, 316))
        screen.blit(font4.render('Programing, Game design, Art', 1, resources.BRANCO), (325, 335))
        screen.blit(font3.render('BGM', 1, resources.BRANCO), (260, 356))
        screen.blit(font4.render('Jazz in Paris-Media Right Productions-YouTube Audio Library', 1, resources.BRANCO), (265, 375))
        screen.blit(font4.render('Bitters At The Saloon-Bird Creek-YouTube Audio Library', 1, resources.BRANCO),(265, 405))
        screen.blit(font3.render('SFX', 1, resources.BRANCO), (300, 445))
        screen.blit(font4.render('site FreeSFX - www.freesfx.co.uk', 1, resources.BRANCO),
                    (325, 475))

    # Se o esstado do jogo for o submenu regras
    if estadoJogo == 'regras':

        #Se o idioma de jogo for inglês
        if idioma['idioma'] == 'ingles':
            #Anexa na tela as imagens referentes as regras do jogo em inglês
            screen.blit(imgRegrasIngles[paginaRegras], menuDic['imgRegras'])
        #Caso contrário
        else:
            #Anexa as imagens de regras do jogo em português
            screen.blit(imgRegras[paginaRegras], menuDic['imgRegras'])
        screen.blit(leftRegras, (690,380))
        screen.blit(rightRegres, (730,380))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            descomprimir_imagens()
            pygame.quit()
        #Eventos de click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Se o botão mudar o nome for clicado
            if botaoRetMudarNome.collidepoint(mouse):
                fxBtn.play()
                #Zera o nome do jogador
                nome = '_ _ _ _ _ _'
                #Seta o etado de submenu para 0
                estadoJogo = 0
                return 'escreverNome', idiomaTexto, idioma, nome #Retorna o estado de jogo Escrever o nome, o identificador de idioma, o dicionário de textos e o nome do jogador
            #Se o botão créditos for clicado
            elif botaoRetCredito.collidepoint(mouse):
                fxBtn.play()
                #Se o estado de jogo estiver setado em 0
                if estadoJogo == 0:
                    #setamo o estado de jogo para o subMenu créditos
                    estadoJogo = 'creditos'
                else:
                #Se o estado de jogo for oute, setamos em 0
                    estadoJogo = 0
            #Se o botão regras for clicado
            elif botaoRetRegras.collidepoint(mouse):
                fxBtn.play()
                #Se o estado de SubMenu for 0
                if estadoJogo == 0:
                    #Inica o submenu regras
                    estadoJogo = 'regras'
                    paginaRegras = 0
                #Se o estado for outro
                else:
                    #Setamos os estado de jogo para 0
                    estadoJogo = 0
            #Se o botão voltar for selecionado
            elif botaoRetVoltar.collidepoint(mouse):
                fxBtn.play()
                #Setamos os estados de submenu para 0
                estadoJogo = 0
                return 'menu', idiomaTexto, idioma, nome #Retorna o estado de jogo Menu, o identificador de idioma, a biblioteca de textos e o nome do jogador
            # Se os botões de seleção de idioma forem clicados
            elif botaoRetLeft.collidepoint(mouse) or botaoRetRight.collidepoint(mouse):
                fxBtn.play()
                if idiomaTexto == 'Português':
                    idiomaTexto = 'Inglês'
                    idioma = textos.dicIngles
                else:
                    idiomaTexto = 'Português'
                    idioma = textos.dicPortugues
            #Botões de regras
            elif botaoRetLeftRegras.collidepoint(mouse) :
                fxBtn.play()
                if paginaRegras == 0:
                    paginaRegras = 3
                    #screen.blit(imgRegras[paginaRegras], menuDic['imgRegras'])
                else:
                    paginaRegras -=1
                    #screen.blit(imgRegras[paginaRegras], menuDic['imgRegras'])
            elif botaoRetRightRegras.collidepoint(mouse):
                fxBtn.play()
                if paginaRegras == 3:
                    paginaRegras = 0
                    #screen.blit(imgRegras[paginaRegras], menuDic['imgRegras'])
                else:
                    paginaRegras +=1
                    #screen.blit(imgRegras[paginaRegras], menuDic['imgRegras'])

        #Mostra o texto de seleção de idioma
        screen.blit(font.render(idiomaTexto, 1, resources.BRANCO), menuDic['opcaoIdioma'])

    #Captura de eventos

    return 'configuracao', idiomaTexto, idioma, nome#Retorna o estado do jogo

"""Metodo responsavel por controlar todo o processamento da escolha de avatar, suas animacoes, 
   e transicao de telas de avatar disponiveis no jogo"""
def avatar(idioma, avatarJogador):
    #Acessa a varável global página que funciona como um indicie da página de seleção do avatar
    global pagina

    pagina = int(avatarJogador/2)#Converte o indicie do avatar já selecionado para um número de indicie da spritesheet página na seleção de avatar

    #Controle de música
    if pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.play()

    #Declaração de fonte
    font = pygame.font.Font('font/Pixellari.ttf', 35)
    #Captura da posução do mouse
    mouse = pygame.mouse.get_pos()

    #Anexa o backgroun da página
    screen.blit(backgroundMenu, (0, 0))

    #Difinição dos retângulos dos botões
    botaoRetVoltar = pygame.Rect(menuDic['btVoltar'][0][0], menuDic['btVoltar'][0][1], botao.get_width(), botao.get_height())
    botaoRetLeft = pygame.Rect(menuDic['btLeftAvatar'][0], menuDic['btLeftAvatar'][1], left.get_width(), left.get_height())
    botaoRetRight = pygame.Rect(menuDic['btRightAvatar'][0], menuDic['btRightAvatar'][1], right.get_width(), right.get_height())

    #Seleção das páginas de avatr de acordo com o idioma
    if idioma['idioma'] == 'portugues':
        screen.blit(paginaPortugues[pagina], (0, 0))
    else:
        screen.blit(paginaIngles[pagina], (0, 0))

    if botaoRetVoltar.collidepoint(mouse):
        screen.blit(botao2, menuDic['btVoltar'][0])
    else:
        screen.blit(botao, menuDic['btVoltar'][0])

    #Adiciona botões a tela
    screen.blit(font.render(idioma['voltar'], 1, resources.BRANCO), menuDic['btVoltar'][1])
    screen.blit(left, menuDic['btLeftAvatar'])
    screen.blit(right, menuDic['btRightAvatar'])

    #Captura de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            descomprimir_imagens()
            pygame.quit()
        #Eventos de click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Se o botão voltar for pressionado
            if botaoRetVoltar.collidepoint(mouse):
                fxBtn.play()
                return 'menu', avatarJogador #Retorna para o estado de jogo Menu e retorna o avatar que está selecionado
            #Se o botão para a esquerda for pressionado
            if botaoRetLeft.collidepoint(mouse):
                fxBtn.play()
                #Se o avatar do jogador estriver entre o indicie 2 e 10 da spritesheet
                if 10 > avatarJogador >= 2:
                    #Seta o avatar do jogador para o indicie da spritesheet siretamente a esquerda da lista na sua imagem padrão
                    avatarJogador -= 2
                    #Seta a página de seleção de avatar no indicie de página diretamente a esquerda do atualmente selecionado
                    pagina -= 1
                #Se o indicíe do avatar de jogador estiver fora do range permitido da spritesheet nessa tela
                else:
                    #stamos o avatar do jogador para o indicie 8
                    avatarJogador = 8
                    pagina = 4 #Setamos a tela de seleção do avatar na página 4

            #Faz o looping de seleção da página para o lado direito
            if botaoRetRight.collidepoint(mouse):
                fxBtn.play()
                if avatarJogador < 8:
                    avatarJogador += 2
                    pagina += 1
                else:
                    avatarJogador = 0
                    pagina = 0

    return 'avatar', avatarJogador #retorna o estado atual e o avatar selecionado até então

"""Metodo responsavel por controlar todo o processamento de entregas de cartas aos
   jogadores, tanto no modo singleplayer como tambem no metodo multiplayer"""
#recebe como parametro a lista baralho e a lista de cartas na mão do pleyer
def entregarCartas(baralho, cartasPlayer=[]):
    #Acessa as varáveis globais referente a conexão em socket com o servidor
    global s, host, porta, instruction, player, multiplayer

    #Se for uma partida multiplayer
    if multiplayer:
        # print(instruction)
        #Se for o primeiro jogador chamando a função
        if player == 0:
            #Preenche as posições da lista de cartas nas mãos do jogador de acordo com as instruções do server
            cartasPlayer[0] = int(instruction[1])
            cartasPlayer[1] = int(instruction[2])
            cartasPlayer[2] = int(instruction[3])
        #Se for o 2º jogador chamando a função
        elif player == 1:
            # Preenche as posições da lista de cartas nas mãos do jogador de acordo com as instruções do server
            cartasPlayer[0] = int(instruction[4])
            cartasPlayer[1] = int(instruction[5])
            cartasPlayer[2] = int(instruction[6])
        else:
            cartasPlayer[0] = int(instruction[7])
            cartasPlayer[1] = int(instruction[8])
            cartasPlayer[2] = int(instruction[9])

        return cartasPlayer, baralho #retorna a matriz de cartas dos players e o baralho sem as cartas do player
    #Se for uma partida single player
    else:
        #Dfine a matriz que vai servir como mãos dos players
        cartasPlayer = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            #Cada linha representa um jogador
            for j in range(3):
                #Cada elemento na coluna uma carta
                while True:
                    #Enquanto houver distribuição cada elemento da matriz recebe um indície aleatório que representa uma carta no baralho
                    cartasPlayer[i][j] = random.randint(0, len(baralho) - 1)
                    #Se já hover houver uma carta nessa posição
                    if baralho[cartasPlayer[i][j]] is not None:
                        break
                #Retira as cartas do player da lista de baralho
                baralho[cartasPlayer[i][j]] = None

        return cartasPlayer, baralho #Retorna as castas do pleyer e o baralho modificado

#Reorganiza a posição das crtas na spritesheet baralho para organizar de acordo com a ordem de maior para menor
def inverterPosCartas(spritesBaralho, cartasInverter=[]):
    temp = [0] * 4
    for i in range(4):
        temp[i] = spritesBaralho[cartasInverter[i]]
    while i >= 0:
        spritesBaralho.remove(spritesBaralho[cartasInverter[i]])
        i -= 1
    for i in range(4):
        spritesBaralho.append(temp[i])

    return spritesBaralho #Retorna o baralho reorganizado

#Vira a carta que servirá como manilha
def virarCarta(baralho, spritesBaralho):
    #Acessa as varáveis relativas ao multiplayer
    global s, host, porta, instruction, player, multiplayer

    #Se for multiplayer
    if multiplayer:
        #recebe a instrução de carta virada do servidor
        cartaVirada = int(instruction[10])
    #Se for single player
    else:
        #Enquanto a carta precisar ser virada
        while True:
            #seleciona um indicíe aleatório do baralho
            cartaVirada = random.randint(0, len(baralho) - 1)
            #Se a carta virada foi selecionada e não é um indicie vazio
            if baralho[cartaVirada] is not None:
                #Continua o código
                break
        #Retira a carta virada do baralho
        baralho[cartaVirada] = None
    # print('\nVirou', cartaVirada)
    #Se a carta virada estiver entre o indice 0 e 3 da spritesheet (cartas Q)
    if 0 <= cartaVirada <= 3:
        #Reorganizamos a spritesheet de baralho onde as cartas J são as mais fortes na ordem de sua manilha
        spritesBaralho = inverterPosCartas(spritesBaralho, [4, 5, 6, 7])
    #Se a Manilha for a carta J
    elif 4 <= cartaVirada <= 7:
        #Reorganizamos a spritesheet de baralho onde as cartas de K são as mais fortes
        spritesBaralho = inverterPosCartas(spritesBaralho, [8, 9, 10, 11])
    #Manilha K
    elif 8 <= cartaVirada <= 11:
        #spritesheet A mais forte
        spritesBaralho = inverterPosCartas(spritesBaralho, [12, 13, 14, 15])
    #Manilha A
    elif 12 <= cartaVirada <= 15:
        #Spritesheet 2 mais forre
        spritesBaralho = inverterPosCartas(spritesBaralho, [16, 17, 18, 19])
    #Manilha 2
    elif 16 <= cartaVirada <= 19:
        spritesBaralho = inverterPosCartas(spritesBaralho, [20, 21, 22, 23])
    #Manilha 3
    elif 20 <= cartaVirada <= 23:
        spritesBaralho = inverterPosCartas(spritesBaralho, [0, 1, 2, 3])
        cartaVirada -= 4 #Seta a carta virada para a de valor 2
    return cartaVirada, baralho, spritesBaralho #Retorna carta virada, baralho modificado

#Controla a animação de ditribuição de cartas e prepara o visual do jogo a cada rodada
def distribuirCartas(distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho):

    global s, host, porta, instruction, player, multiplayer
    if multiplayer:
        instruction[24] = 1
        if distribuir_cartas and animacaoCarta[1] < 9:
            screen.blit(fundoCarta, (animacaoCarta[0], 290))

            animacaoCarta[0] += 10
            if animacaoCarta[0] > 300:
                fxCardAnim.play()
                animacaoCarta[0] = 192
                animacaoCarta[1] += 1
            if animacaoCarta[0] < 100:
                fxCardAnim.play()
                animacaoCarta[0] = 192
                animacaoCarta[1] += 1
            if animacaoCarta[1] >= 1:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][0])
            if animacaoCarta[1] >= 2:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][1])
            if animacaoCarta[1] >= 3:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][2])
            if animacaoCarta[1] >= 4:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
            if animacaoCarta[1] >= 5:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
            if animacaoCarta[1] >= 6:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
                animacaoCarta[0] -= 20
            if animacaoCarta[1] >= 7:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
            if animacaoCarta[1] >= 8:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
            if animacaoCarta[1] >= 9:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
                distribuir_cartas = False
                cartasComJogador, baralho = entregarCartas(baralho, cartasComJogador)
                cartaVirada, baralho, spritesBaralho = virarCarta(baralho, spritesBaralho)
                # print('\n\n', cartasComJogador)

        return distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho

    else:
        # print('Single')
        #Se a sequencia de distribuição de cartas for verdadeira e o contador for menor que o número de cartas que precisa ser distribuído
        if distribuir_cartas and animacaoCarta[1] < 9:
            #Posiciona a imagem de baralho no início da animação de distribuição
            screen.blit(fundoCarta, (animacaoCarta[0], 290))
            #Incremento da animação
            animacaoCarta[0] += 10
            #Controla a animação de distribuição de cartas, se o valor x da carta do baralho for maior que 300
            if animacaoCarta[0] > 300:
                animacaoCarta[0] = 192 #Retornamos a carta para a posição do baralho
                fxCardAnim.play()#Toca o som de distribuição de carta
                animacaoCarta[1] += 1 #Incrementa o contador
            #Controla a animação de distribuição quando o x é < 100 ou seja é distribuída cartas para a esquerda do baralho
            if animacaoCarta[0] < 100:
                fxCardAnim.play()
                animacaoCarta[0] = 192 #Seta a carta na posição x do baralho
                animacaoCarta[1] += 1 #Incrementa o contador de controle dos quadros de animação de embaralhamento

            #Se o contador de animação for de 1 a 3 significa que a sequencia de distribuição acrescenta cartas a mão do jogador 1
            if animacaoCarta[1] >= 1:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][0])
            if animacaoCarta[1] >= 2:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][1])
            if animacaoCarta[1] >= 3:
                screen.blit(fundoCarta, jogoDic['posCartaPlayer1'][2])

            #Controla o posicionamento das cartas do segundo jogador durante a aniimação de distribuição
            if animacaoCarta[1] >= 4:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
            if animacaoCarta[1] >= 5:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
            if animacaoCarta[1] >= 6:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
                #após terminada a distribuição para o jogador 1 e 2 a terceira rodada de distribuição tem a orientação a esquerda do baralho, por isso sua posição x agora decrementa e a animação tem o sentido invertido
                animacaoCarta[0] -= 20
            #Controla o posicionamento das cartas do terceiro jogador
            if animacaoCarta[1] >= 7:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
            if animacaoCarta[1] >= 8:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
            if animacaoCarta[1] >= 9:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
                #após distribuir a última carta a função saí do looping de distribuição
                distribuir_cartas = False
                #Define define os novos valores de cartas para a mão do jogador e para o baralho
                cartasComJogador, baralho = entregarCartas(baralho, cartasComJogador)
                #Define a manilha
                cartaVirada, baralho, spritesBaralho = virarCarta(baralho, spritesBaralho)
                # print('\n\n', cartasComJogador)

        return distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho #Retorna toda a sequencia de distribuição de cartas e suas informaçãoes

#Função para atribuir pontos de acrodo com a rodada de jogo
def atribuirPontos(rodada, pontosJogador, vencedor):
    #Acessa a variável global de estado do jogo
    global estadoJogo
    #Se for a primeira rodada
    if rodada == 1:
        #O jogador vencedor da rodada recebe 3 pontos
        pontosJogador[vencedor] += 3
    #Se for a segunda rodada
    elif rodada == 2:
        #O jogador vencedor da rodada recebe 2 pontos
        pontosJogador[vencedor] += 2
    else:
        #O jogador vencedor da última rdada recebe 1 ponto
        pontosJogador[vencedor] += 1
    if pontosJogador[vencedor] == 12:
        # print('Jogador {} Venceu.'.format(vencedor))
        estadoJogo = 'vencedor'
        # main()
    elif pontosJogador[vencedor] > 12:
        # print('Jogador {} Zerou.'.format(vencedor))
        pontosJogador[vencedor] = 0
    return pontosJogador #Retorna a quantidade de pontos do jogador que venceu a rodada


# Verifica quem jogou a carta com o maior valor.
def verificarVencedorRodada(cartasJogadas, rodada, pontosJogador):
    #Essa lista contém o poder de cada carta de acordo com seu posicionamento na spritesheet
    forcaCarta = [1, 1, 1, 1,
                  2, 2, 2, 2,
                  3, 3, 3, 3,
                  4, 4, 4, 4,
                  5, 5, 5, 5,
                  6, 6, 6, 6]
    #Comparação da força das crtas que não forem manilhas
    if forcaCarta[cartasJogadas[0]] != 6 and forcaCarta[cartasJogadas[1]] != 6 and forcaCarta[cartasJogadas[2] != 6]:
        #verifica se o jogador 1 venceu a rodada
        if cartasJogadas[0] > cartasJogadas[1] and cartasJogadas[0] > cartasJogadas[2]:
            #verifica se não há empate
            if forcaCarta[cartasJogadas[0]] != forcaCarta[cartasJogadas[1]] and forcaCarta[cartasJogadas[0]] != forcaCarta[cartasJogadas[2]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 0)
            else:
                pass
                #print("Empatou")
        #Verifica se o jogador 2 venceu a rodada
        elif cartasJogadas[1] > cartasJogadas[0] and cartasJogadas[1] > cartasJogadas[2]:
            if forcaCarta[cartasJogadas[1]] != forcaCarta[cartasJogadas[0]] and forcaCarta[cartasJogadas[1]] != forcaCarta[cartasJogadas[2]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 1)
            else:
                pass
                # print("Empatou")
        #Verifica se o jogador 3 venceu a rodada
        elif cartasJogadas[2] > cartasJogadas[0] and cartasJogadas[2] > cartasJogadas[1]:
            if forcaCarta[cartasJogadas[2]] != forcaCarta[cartasJogadas[0]] and forcaCarta[cartasJogadas[2]] != forcaCarta[cartasJogadas[1]]:
                pontosJogador = atribuirPontos(rodada, pontosJogador, 2)
            else:
                pass
                # print("Empatou")
    #Verifica a força das manilhas
    else:
        if cartasJogadas[0] > cartasJogadas[1] and cartasJogadas[0] > cartasJogadas[2]:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 0)
        elif cartasJogadas[1] > cartasJogadas[0] and cartasJogadas[1] > cartasJogadas[2]:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 1)
        else:
            pontosJogador = atribuirPontos(rodada, pontosJogador, 2)

    return pontosJogador
# /Verifica quem jogou a carta com o maior valor.

#Lógica de jogo multiplayer
def jogarMult(idioma, nome, baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada, conectionC):

    #Acessa as variáveis globais de controle multiplayer
    global s, host, porta, instruction, player, cronometro1, estadoJogo, cronometro2, animator

    #Controle da música
    if pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.play()

    #Aguarda a recepção da instrução do servidor
    try:
        instruction = s.recv(1024)
        instruction = instruction.decode('utf-8')
        instruction = instruction.split(',')
    #Se houver erro de conexeão reinicia a aplicação
    except socket.error:
        main()

    #Definição de fontes
    font = pygame.font.Font('font/Pixellari.ttf', 45)
    font2 = pygame.font.Font('font/Pixellari.ttf', 35)
    font3 = pygame.font.Font('font/Pixellari.ttf', 25)

    #Captura a posição do mouse
    mouse = pygame.mouse.get_pos()
    #Inicia backgroun da gameplay
    screen.blit(backgroundJogo, (0, 0))

    # Exibe o placar e a rodada.
    #Se a sequentcia de distribuição de cartas for verdadeiro
    if distribuir_cartas:

        for i in range(3):
            #Anexams os fundos de avatar da gameplay
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])

        #Configuração do primeiro jogador
        if player == 0:
            #Controle de animação do avatar
            if animator < 30:
                #Anexa as imagens dos avateres de acordo com a instrução recebida do servidor
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[19])], jogoDic['posAvatar'][2])
            #Variação da animação do avatar durante a distribuição
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[19]) + 1], jogoDic['posAvatar'][2])

            #anexa a tela as informações de pontos de cada jogador
            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador3'])
            #Anexa as informações de nome de cada jogador na tela
            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])
        #Configurações de visualização e animação do jogador 2
        elif player == 1:
            if animator < 30:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[17])], jogoDic['posAvatar'][2])
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[17]) + 1], jogoDic['posAvatar'][2])

            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador3'])

            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])
        #Configurações de animação e visualização do jogador 3
        elif player == 2:
            if animator < 30:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[18])], jogoDic['posAvatar'][2])
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[18]) + 1], jogoDic['posAvatar'][2])

            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador3'])

            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])

        #Anexa o indicador de fase de embaralhamento
        screen.blit(font.render(idioma['embaralhar'], 1, resources.BRANCO), (jogoDic['posTextoRodada'][0] - 40, jogoDic['posTextoRodada'][1]))

        #Captura eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                descomprimir_imagens()
                pygame.quit()
        #Inicia o método de distribuição de cartas e configuração do baralho
        distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho = distribuirCartas(distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho)

    #Se as cartas já foram distribuídas
    else:
        # Desenha o retangulo das cartas do player
        retCartas = [None] * 3
        for i in range(3):
            retCartas[i] = pygame.Rect(jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1],
                                       spritesBaralho[0].get_width(), spritesBaralho[0].get_height())

        # Animação das Cartas quando o mouse está sobre elas
        for i in range(3):
            #Se a lista de cartas com o jogador não está vazia
            if cartasComJogador[i] is not None:
                #Se houver colisão entre a  carta do jogador e o mouse
                if retCartas[i].collidepoint(mouse[0], mouse[1]):
                    #Criamos um efeito de movimentação da carta incrementando seu y
                    screen.blit(spritesBaralho[cartasComJogador[i]], (jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1] - 15))
                    #Controle do ponto de vista de qual carta irá mecher dependendo do jogador da vez
                    if player == 0:
                        if i == 0:
                            instruction[26] = 1
                        elif i == 1:
                            instruction[27] = 1
                        else:
                            instruction[28] = 1
                    elif player == 1:
                        if i == 0:
                            instruction[29] = 1
                        elif i == 1:
                            instruction[30] = 1
                        else:
                            instruction[31] = 1
                    else:
                        if i == 0:
                            instruction[32] = 1
                        elif i == 1:
                            instruction[33] = 1
                        else:
                            instruction[34] = 1
                #Se não hover colisão as cartas se mantém em sua posição padrão
                else:
                    screen.blit(spritesBaralho[cartasComJogador[i]], jogoDic['posCartaPlayer1'][i])
                    if player == 0:
                        if i == 0:
                            instruction[26] = -1
                        elif i == 1:
                            instruction[27] = -1
                        else:
                            instruction[28] = -1
                    elif player == 1:
                        if i == 0:
                            instruction[29] = -1
                        elif i == 1:
                            instruction[30] = -1
                        else:
                            instruction[31] = -1
                    else:
                        if i == 0:
                            instruction[32] = -1
                        elif i == 1:
                            instruction[33] = -1
                        else:
                            instruction[34] = -1

        #Controle de eventos após a distribuição
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                descomprimir_imagens()
                estadoJogo = 'sair'
                instruction[24] = -10
            #Eventos de click do mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Definições para o player se definido pelo sevidor como o primeiro
                if player == int(instruction[0]):
                    #Confere a colisão entre o mouse e a 1ª carta na mão do player e se há carta na mão do player
                    if retCartas[0].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0] is not None:
                        fxCardAnim.play()
                        #Seleciona a posição na mesa em que a carta será jogada
                        if int(instruction[11]) == -1:
                            instruction[11] = cartasComJogador[0]
                        elif int(instruction[12]) == -1:
                            instruction[12] = cartasComJogador[0]
                        elif int(instruction[13]) == -1:
                            instruction[13] = cartasComJogador[0]
                        #Apaga a carta selecionada da mão do jogador
                        cartasComJogador[0] = None
                        #Executa a jogada nas outras visualizações e retira uma carta da mão do player
                        if int(instruction[11]) is -1 or int(instruction[12]) is -1 or int(instruction[13]) is -1:
                            if player == 0:
                                instruction[0] = 1
                                instruction[1] = -1
                            elif player == 1:
                                instruction[0] = 2
                                instruction[4] = -1
                            elif player == 2:
                                instruction[0] = 0
                                instruction[7] = -1
                    #Confere a colisão entre o muse e a segunda carta do player
                    elif retCartas[1].collidepoint(mouse[0], mouse[1]) and cartasComJogador[1] is not None:
                        fxCardAnim.play()
                        #Joga a carta selecionada me seu espaço na mesa
                        if int(instruction[11]) == -1:
                            instruction[11] = cartasComJogador[1]
                        elif int(instruction[12]) == -1:
                            instruction[12] = cartasComJogador[1]
                        elif int(instruction[13]) == -1:
                            instruction[13] = cartasComJogador[1]
                        #Apaga a carta da mão do jogador
                        cartasComJogador[1] = None
                        #Retira a carta da mão do jogador na visualização dos outros jogadore
                        if int(instruction[11]) is -1 or int(instruction[12]) is -1 or int(instruction[13]) is -1:
                            if player == 0:
                                instruction[0] = 1
                                instruction[2] = -1
                            elif player == 1:
                                instruction[0] = 2
                                instruction[5] = -1
                            elif player == 2:
                                instruction[0] = 0
                                instruction[8] = -1
                    #Confere a colisão e seleção da últiuma carta na mão do player
                    elif retCartas[2].collidepoint(mouse[0], mouse[1]) and cartasComJogador[2] is not None:
                        fxCardAnim.play()
                        if int(instruction[11]) == -1:
                            instruction[11] = cartasComJogador[2]
                        elif int(instruction[12]) == -1:
                            instruction[12] = cartasComJogador[2]
                        elif int(instruction[13]) == -1:
                            instruction[13] = cartasComJogador[2]
                        cartasComJogador[2] = None

                        if int(instruction[11]) is -1 or int(instruction[12]) is -1 or int(instruction[13]) is -1:
                            if player == 0:
                                instruction[0] = 1
                                instruction[3] = -1
                            elif player == 1:
                                instruction[0] = 2
                                instruction[6] = -1
                            elif player == 2:
                                instruction[0] = 0
                                instruction[9] = -1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load(resources.MENU_MUSIC)
                    instruction[24] = -10
        #Anexa a carta virada a tela
        screen.blit(spritesBaralho[cartaVirada], jogoDic['posCartaVirada'])


        # Exibe a animação das cartas quando os outros jogadores interagem se for do ponto de vista do player 1
        if player == 0:
            if int(instruction[4]) is not -1:
                if int(instruction[29]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), (jogoDic['posCartaPlayer2'][0][0] - 15, jogoDic['posCartaPlayer2'][0][1]))

            if int(instruction[5]) is not -1:
                if int(instruction[30]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), (jogoDic['posCartaPlayer2'][1][0] - 15, jogoDic['posCartaPlayer2'][1][1]))

            if int(instruction[6]) is not -1:
                if int(instruction[31]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][2][0] - 15, jogoDic['posCartaPlayer2'][2][1]))

            if int(instruction[7]) is not -1:
                if int(instruction[32]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), (jogoDic['posCartaPlayer3'][0][0] + 15, jogoDic['posCartaPlayer3'][0][1]))

            if int(instruction[8]) is not -1:
                if int(instruction[33]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), (jogoDic['posCartaPlayer3'][1][0] + 15, jogoDic['posCartaPlayer3'][1][1]))
            if int(instruction[9]) is not -1:
                if int(instruction[34]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), (jogoDic['posCartaPlayer3'][2][0] + 15, jogoDic['posCartaPlayer3'][2][1]))
        # Exibe a animação das cartas quando os outros jogadores interagem se for do ponto de vista do player 2
        elif player == 1:
            if int(instruction[7]) is not -1:
                if int(instruction[32]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][0][0] - 15, jogoDic['posCartaPlayer2'][0][1]))

            if int(instruction[8]) is not -1:
                if int(instruction[33]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][1][0] - 15, jogoDic['posCartaPlayer2'][1][1]))
            if int(instruction[9]) is not -1:
                if int(instruction[34]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][2][0] - 15, jogoDic['posCartaPlayer2'][2][1]))

            if int(instruction[1]) is not -1:
                if int(instruction[26]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][0][0] + 15, jogoDic['posCartaPlayer3'][0][1]))
            if int(instruction[2]) is not -1:
                if int(instruction[27]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][1][0] + 15, jogoDic['posCartaPlayer3'][1][1]))
            if int(instruction[3]) is not -1:
                if int(instruction[28]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][2][0] + 15, jogoDic['posCartaPlayer3'][2][1]))
        # Exibe a animação das cartas quando os outros jogadores interagem se for do ponto de vista do player 3
        elif player == 2:
            if int(instruction[1]) is not -1:
                if int(instruction[26]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][0][0] - 15, jogoDic['posCartaPlayer2'][0][1]))
            if int(instruction[2]) is not -1:
                if int(instruction[27]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][1][0] - 15, jogoDic['posCartaPlayer2'][1][1]))
            if int(instruction[3]) is not -1:
                if int(instruction[28]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, 90),
                                (jogoDic['posCartaPlayer2'][2][0] - 15, jogoDic['posCartaPlayer2'][2][1]))

            if int(instruction[4]) is not -1:
                if int(instruction[29]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][0])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][0][0] + 15, jogoDic['posCartaPlayer3'][0][1]))
            if int(instruction[5]) is not -1:
                if int(instruction[30]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][1])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][0][0] + 15, jogoDic['posCartaPlayer3'][1][1]))
            if int(instruction[6]) is not -1:
                if int(instruction[31]) == -1:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][2])
                else:
                    screen.blit(pygame.transform.rotate(fundoCarta, -90),
                                (jogoDic['posCartaPlayer3'][2][0] + 15, jogoDic['posCartaPlayer3'][2][1]))
        # /Exibe a animação das cartas


        temp = 0
        # Desenha as cartas jogadas na mesa
        for i in range(11, 14):
            #Se houverem cartas na mesa
            if int(instruction[i]) is not -1:
                #Anexa a imagem da carta
                screen.blit(spritesBaralho[int(instruction[i])], jogoDic['posJogada'][temp])
                temp += 1

        # Desenha o Placar

        for i in range(3):
            #Anexa a imagem de fundo do avatar
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])

        #Posiciona e controla a animação do personagem durante a gameplay
        if player == 0:
            if animator < 30:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[19])], jogoDic['posAvatar'][2])
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[19]) + 1], jogoDic['posAvatar'][2])

            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador3'])

            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])

            if int(instruction[0]) == 0:
                screen.blit(turnoImg, jogoDic['posAvatar'][0])
            elif int(instruction[0]) == 1:
                screen.blit(turnoImg, jogoDic['posAvatar'][1])
            else:
                screen.blit(turnoImg, jogoDic['posAvatar'][2])
        elif player == 1:
            if animator < 30:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[17])], jogoDic['posAvatar'][2])
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[18]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[17]) + 1], jogoDic['posAvatar'][2])

            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador3'])

            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])

            if int(instruction[0]) == 0:
                screen.blit(turnoImg, jogoDic['posAvatar'][2])
            elif int(instruction[0]) == 1:
                screen.blit(turnoImg, jogoDic['posAvatar'][0])
            else:
                screen.blit(turnoImg, jogoDic['posAvatar'][1])
        elif player == 2:
            if animator < 30:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19])], -1, 0), jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17])], -1, 0), jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[18])], jogoDic['posAvatar'][2])
            else:
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[19]) + 1], -1, 0),
                            jogoDic['posAvatar'][0])
                screen.blit(pygame.transform.flip(spriteSheetAvatar[int(instruction[17]) + 1], -1, 0),
                            jogoDic['posAvatar'][1])
                screen.blit(spriteSheetAvatar[int(instruction[18]) + 1], jogoDic['posAvatar'][2])

            screen.blit(font.render(instruction[22], 1, resources.BRANCO), jogoDic['posPontoJogador1'])
            screen.blit(font.render(instruction[20], 1, resources.BRANCO), jogoDic['posPontoJogador2'])
            screen.blit(font.render(instruction[21], 1, resources.BRANCO), jogoDic['posPontoJogador3'])

            screen.blit(font2.render(instruction[16], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
            screen.blit(font2.render(instruction[14], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
            screen.blit(font2.render(instruction[15], 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])

            if int(instruction[0]) == 0:
                screen.blit(turnoImg, jogoDic['posAvatar'][1])
            elif int(instruction[0]) == 1:
                screen.blit(turnoImg, jogoDic['posAvatar'][2])
            else:
                screen.blit(turnoImg, jogoDic['posAvatar'][0])

        #Display da rodada atual
        screen.blit(font.render(idioma['rodada'] + ' ' + instruction[23], 1, resources.BRANCO), jogoDic['posTextoRodada'])

    #Posicionamento da imagem do baralho
    screen.blit(baralhoImg, jogoDic['posBralho'])

    # reseta o jogo após a 3 rodada
    if int(instruction[24]) == -1:
        spritesBaralho.clear()
        spritesBaralho = resources.spritesBaralho()
        distribuir_cartas = True
        animacaoCarta[1] = 0
    # /reseta o jogo após a 3 rodada

    if int(instruction[24]) == -10 and estadoJogo is not 'sair':
        estadoJogo = -10

    # Exibe o vencedor e os perdedores para os jogadores.
    if instruction[35] == instruction[14] or instruction[35] == instruction[15] or instruction[35] == instruction[16]:
        cronometro2 += 1
        instruction[37] = cronometro2
        screen.blit(vencedorBg, (0, 0))
        screen.blit(font2.render(idioma['vencedor'], 1, resources.BRANCO), jogoDic['posTextoVencedor'])
        screen.blit(font2.render(instruction[35], 1, resources.BRANCO), jogoDic['posNomeVencedor'])
        if animation < 30:
            screen.blit(pygame.transform.scale2x(spriteSheetAvatar[int(instruction[36])]), jogoDic['posAvatarVencedor'])
        else:
            screen.blit(pygame.transform.scale2x(spriteSheetAvatar[int(instruction[36])] + 1), jogoDic['posAvatarVencedor'])

        if instruction[35] == instruction[14]:
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[18]) / 2 + 10)], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[19]) / 2 + 10)], 90), jogoDic['posPerdedores'][1])

            screen.blit(font3.render(instruction[15], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render(instruction[16], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])

        elif instruction[35] == instruction[15]:
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[17]) / 2 + 10)], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[19]) / 2 + 10)], 90), jogoDic['posPerdedores'][1])
            screen.blit(font3.render(instruction[14], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render(instruction[16], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])
        else:
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[17]) / 2 + 10)], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(int(instruction[18]) / 2 + 10)], 90), jogoDic['posPerdedores'][1])
            screen.blit(font3.render(instruction[14], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render(instruction[15], 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])
    else:
        cronometro2 = 0
    # /Exibe o vencedor e os perdedores para os jogadores.

    # Tempo de exibição da rodada
    if int(instruction[13]) is not -1:
        cronometro1 += 1
        instruction[25] = cronometro1
    else:
        cronometro1 = 0
    # /Tempo de exibição da rodada

    # print('Estado do jogo: ', instruction[24])
    try:
        instruction = ','.join(str(e) for e in instruction)
        if estadoJogo is not -10:
            s.send((instruction.encode('utf-8')))
        else:
            main()
    except socket.error:
        # print('Fim')
        main()

    if estadoJogo == 'sair':
        descomprimir_imagens()
        pygame.quit()

    if estadoJogo == -10:
        conectionC = False
        estadoJogo = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada = resetar(baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada)
        return 'menu', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador, conectionC

    return 'jogandoMult', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador, conectionC

#Lógica de jogo single player
def jogarSingle(idioma, nome, baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada):
    #Controle global de estado de jogo e tempo de exibição e animação
    global estadoJogo, cronometro2, animator

    if pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.play()

    font = pygame.font.Font('font/Pixellari.ttf', 45)
    font2 = pygame.font.Font('font/Pixellari.ttf', 35)
    font3 = pygame.font.Font('font/Pixellari.ttf', 25)
    mouse = pygame.mouse.get_pos()
    screen.blit(backgroundJogo, (0, 0))

    #Se for o momento de distribuição de cartas
    if distribuir_cartas:

        for i in range(3):
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])

        # Desenha os Avatares e define sua animação
        if animator < 30:
            screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador], -1, 0), jogoDic['posAvatar'][0])
            screen.blit(pygame.transform.flip(spriteSheetAvatar[0], -1, 0), jogoDic['posAvatar'][1])
            screen.blit(spriteSheetAvatar[2], jogoDic['posAvatar'][2])
        else:
            screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador + 1], -1, 0),
                        jogoDic['posAvatar'][0])
            screen.blit(pygame.transform.flip(spriteSheetAvatar[1], -1, 0),
                        jogoDic['posAvatar'][1])
            screen.blit(spriteSheetAvatar[3], jogoDic['posAvatar'][2])


        screen.blit(font.render(str(pontosJogador[0]), 1, resources.BRANCO), jogoDic['posPontoJogador1'])
        screen.blit(font.render(str(pontosJogador[1]), 1, resources.BRANCO), jogoDic['posPontoJogador2'])
        screen.blit(font.render(str(pontosJogador[2]), 1, resources.BRANCO), jogoDic['posPontoJogador3'])

        screen.blit(font2.render(str(nome), 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
        screen.blit(font2.render('Morte', 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
        screen.blit(font2.render('Burocrata', 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])

        screen.blit(font.render(idioma['embaralhar'], 1, resources.BRANCO), (jogoDic['posTextoRodada'][0] - 40, jogoDic['posTextoRodada'][1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                descomprimir_imagens()
                pygame.quit()
        #Executa a função de distribuição de cartas
        distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho = distribuirCartas(distribuir_cartas, animacaoCarta, cartaVirada, baralho, cartasComJogador, spritesBaralho)


    #Cartas já distribuidas
    else:
        # Desenha o retangulo das cartas do player
        retCartas = [None] * 3
        for i in range(3):
            retCartas[i] = pygame.Rect(jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1],
                                       spritesBaralho[0].get_width(), spritesBaralho[0].get_height())
        # /Desenha o retangulo das cartas do player
        # Animação das Cartas ------------------------------------------------------------------------------------------------------------------------------------------
        for i in range(3):
            if cartasComJogador[0][i] is not None:
                if retCartas[i].collidepoint(mouse[0], mouse[1]):
                    screen.blit(spritesBaralho[cartasComJogador[0][i]], (jogoDic['posCartaPlayer1'][i][0], jogoDic['posCartaPlayer1'][i][1] - 15))
                else:
                    screen.blit(spritesBaralho[cartasComJogador[0][i]], jogoDic['posCartaPlayer1'][i])
        # /Animação das Cartas ------------------------------------------------------------------------------------------------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                descomprimir_imagens()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turno == 0:
                    if retCartas[0].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][0] is not None:
                        cartasJogadas.append(cartasComJogador[0][0])
                        cartasComJogador[0][0] = None
                        turno += 1
                        fxCardAnim.play()
                    elif retCartas[1].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][1] is not None:
                        cartasJogadas.append(cartasComJogador[0][1])
                        cartasComJogador[0][1] = None
                        turno += 1
                        fxCardAnim.play()
                    elif retCartas[2].collidepoint(mouse[0], mouse[1]) and cartasComJogador[0][2] is not None:
                        cartasJogadas.append(cartasComJogador[0][2])
                        cartasComJogador[0][2] = None
                        turno += 1
                        fxCardAnim.play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.load(resources.MENU_MUSIC)
                    estadoJogo = 0
                    pontosJogador[0], pontosJogador[1], pontosJogador[2] = 0, 0, 0
                    baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada = resetar(baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada)
                    return 'menu', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador

        screen.blit(spritesBaralho[cartaVirada], jogoDic['posCartaVirada'])

        # # Blit na mao do player 2 - Mostra
        # for i in range(3):
        #     if cartasComJogador[1][i] is not None:
        #         screen.blit(pygame.transform.rotate(spritesBaralho[cartasComJogador[1][i]], 90), jogoDic['posCartaPlayer2'][i])
        #
        # # Blit na mao do player 3
        # for i in range(3):
        #     if cartasComJogador[2][i] is not None:
        #         screen.blit(pygame.transform.rotate(spritesBaralho[cartasComJogador[2][i]], -90), jogoDic['posCartaPlayer3'][i])

        # Blit na mao do player 2 - Esconde
        for i in range(3):
            if cartasComJogador[1][i] is not None:
                screen.blit(pygame.transform.rotate(fundoCarta, 90), jogoDic['posCartaPlayer2'][i])

        # Blit na mao do player 3
        for i in range(3):
            if cartasComJogador[2][i] is not None:
                screen.blit(pygame.transform.rotate(fundoCarta, -90), jogoDic['posCartaPlayer3'][i])

        # Desenha as cartas jogadas na mesa -----------------------------------------------------
        for i in range(len(cartasJogadas)):
            screen.blit(spritesBaralho[cartasJogadas[i]], jogoDic['posJogada'][i])
        # /Desenha as cartas jogadas na mesa -----------------------------------------------------

        # Desenha o Placar
        for i in range(3):
            screen.blit(fundoAvatarBg, jogoDic['posBgFundoAvatar'][i])

        if animator < 30:
            screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador], -1, 0), jogoDic['posAvatar'][0])
            screen.blit(pygame.transform.flip(spriteSheetAvatar[0], -1, 0), jogoDic['posAvatar'][1])
            screen.blit(spriteSheetAvatar[2], jogoDic['posAvatar'][2])
        else:
            screen.blit(pygame.transform.flip(spriteSheetAvatar[avatarJogador + 1], -1, 0),
                        jogoDic['posAvatar'][0])
            screen.blit(pygame.transform.flip(spriteSheetAvatar[1], -1, 0),
                        jogoDic['posAvatar'][1])
            screen.blit(spriteSheetAvatar[3], jogoDic['posAvatar'][2])

        screen.blit(font.render(str(pontosJogador[0]), 1, resources.BRANCO), jogoDic['posPontoJogador1'])
        screen.blit(font.render(str(pontosJogador[1]), 1, resources.BRANCO), jogoDic['posPontoJogador2'])
        screen.blit(font.render(str(pontosJogador[2]), 1, resources.BRANCO), jogoDic['posPontoJogador3'])
        screen.blit(font2.render(str(nome), 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][0])
        screen.blit(font2.render('Morte', 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][1])
        screen.blit(font2.render('Burocrata', 1, resources.BRANCO), jogoDic['posTextoNomeJogador'][2])
        screen.blit(font.render(idioma['rodada'] + ' ' + str(rodada), 1, resources.BRANCO), jogoDic['posTextoRodada'])
        # /Desenha o Placar

    screen.blit(baralhoImg, jogoDic['posBralho'])

    # Inteligencia Artificial TEMP
    if turno == 1:
        while True:
            aleatorio = random.randint(0, 2)
            if cartasComJogador[1][aleatorio] is not None:
                break
        cartasJogadas.append(cartasComJogador[1][aleatorio])
        cartasComJogador[1][aleatorio] = None
        turno += 1

    if turno == 2:
        while True:
            aleatorio = random.randint(0, 2)
            if cartasComJogador[2][aleatorio] is not None:
                break
        cartasJogadas.append(cartasComJogador[2][aleatorio])
        cartasComJogador[2][aleatorio] = None
        turno = -1
    # /Inteligencia Artificial

    # Exibe o vencedor e os perdedores para os jogadores.
    if estadoJogo == 'vencedor':
        screen.blit(vencedorBg, (0, 0))
        if pontosJogador[0] == 12:
            screen.blit(font2.render(nome, 1, resources.BRANCO), jogoDic['posNomeVencedor'])
            if animation < 30:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador]), jogoDic['posAvatarVencedor'])
            else:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[avatarJogador] + 1), jogoDic['posAvatarVencedor'])
            screen.blit(font2.render(idioma['vencedor'], 1, resources.BRANCO), jogoDic['posTextoVencedor'])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[10], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[11], 90), jogoDic['posPerdedores'][1])
            screen.blit(font3.render('Morte', 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render('Burocrata', 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])

        elif pontosJogador[1] == 12:
            if animation < 30:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[0]), jogoDic['posAvatarVencedor'])
            else:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[0] + 1), jogoDic['posAvatarVencedor'])

            screen.blit(font2.render('Morte', 1, resources.BRANCO), jogoDic['posNomeVencedor'])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(avatarJogador / 2 + 10)], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[11], 90), jogoDic['posPerdedores'][1])
            screen.blit(font3.render(str(nome), 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render('Burocrata', 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])
        else:
            if animation < 30:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[2]), jogoDic['posAvatarVencedor'])
            else:
                screen.blit(pygame.transform.scale2x(spriteSheetAvatar[2] + 1), jogoDic['posAvatarVencedor'])
            screen.blit(font2.render('Burocrata', 1, resources.BRANCO), jogoDic['posNomeVencedor'])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[int(avatarJogador / 2 + 10)], 90), jogoDic['posPerdedores'][0])
            screen.blit(pygame.transform.rotate(spriteSheetAvatar[10], 90), jogoDic['posPerdedores'][1])
            screen.blit(font3.render(str(nome), 1, resources.BRANCO), jogoDic['posTxtPerdedor'][0])
            screen.blit(font3.render('Morte', 1, resources.BRANCO), jogoDic['posTxtPerdedor'][1])
        cronometro2 += 1
        if cronometro2 >= 120:
            pontosJogador[0], pontosJogador[1], pontosJogador[2] = 0, 0, 0
            baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada = resetar(baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada)
            estadoJogo = 0
    else:
        cronometro2 = 0
    # /Exibe o vencedor e os perdedores para os jogadores.

    # Tempo de exibição da rodada
    if turno == -1:
        global cronometro1
        cronometro1 += 1
        if cronometro1 == tempoExibicaoRodada:
            # print('Cartas jogadas', cartasJogadas)
            # print('\n\n', cartasComJogador)
            pontosJogador = verificarVencedorRodada(cartasJogadas, rodada, pontosJogador)
            cartasJogadas.clear()
            turno = 0
            rodada += 1
            cronometro1 = 0
        # Reset
        if rodada > 3 and estadoJogo is not 'vencedor':
            baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada = resetar(baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada)
        # /Reset
    # /Tempo de exibição da rodada

    return 'jogandoSingle', baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador


def resetar(baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada):
    baralho = [0, 1, 2, 3,
               4, 5, 6, 7,
               8, 9, 10, 11,
               12, 13, 14, 15,
               16, 17, 18, 19,
               20, 21, 22, 23]
    distribuir_cartas = True
    animacaoCarta[1] = 0
    spritesBaralho.clear()
    spritesBaralho = resources.spritesBaralho()
    rodada = 1
    return baralho, distribuir_cartas, animacaoCarta, spritesBaralho, rodada

#Controle de Sequencia de abertura
def abertura(apresentacao):
    # Se a música de fundo estiver tocando
    if pygame.mixer.music.get_busy():
        # Não fazer nada
        pass
    # Caso contrário
    else:
        # Executa a música de background
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            descomprimir_imagens()
            pygame.quit()
    global cronometro1, contadorG

    screen.fill(resources.BRANCO)

    font = pygame.font.Font('font/Pixellari.ttf', 45)

    #Controle de apresentação do logo
    if apresentacao == 1:
        cronometro1 += 1
        if cronometro1 <= 10:
            screen.blit(logo[0], (160, 190))
        elif 5 < cronometro1 <= 10:
            screen.blit(logo[1], (160, 190))
        elif 10 < cronometro1 <= 15:
            screen.blit(logo[2], (160, 190))
        elif 15 < cronometro1 <= 20:
            screen.blit(logo[3], (160, 190))
        elif 20 < cronometro1 <= 25:
            screen.blit(logo[4], (160, 190))
        elif 25 < cronometro1 <= 30:
            screen.blit(logo[5], (160, 190))
        elif 30 < cronometro1 <= 35:
            screen.blit(logo[6], (160, 190))
        elif 35 < cronometro1 <= 40:
            screen.blit(logo[7], (160, 190))
        elif 40 < cronometro1 <= 45:
            screen.blit(logo[8], (160, 190))
        elif 45 < cronometro1 <= 50:
            screen.blit(logo[9], (160, 190))
        elif 50 < cronometro1 <= 55:
            screen.blit(logo[10], (160, 190))
        elif 55 < cronometro1 <= 60:
            screen.blit(logo[11], (160, 190))
        elif 60 < cronometro1 <= 65:
            screen.blit(logo[12], (160, 190))
        elif 65 < cronometro1 <= 70:
            screen.blit(logo[13], (160, 190))
        elif 70 < cronometro1 <= 75:
            screen.blit(logo[14], (160, 190))
        elif 75 < cronometro1 <= 80:
            screen.blit(logo[15], (160, 190))
        elif 80 < cronometro1 <= 85:
            screen.blit(logo[16], (160, 190))
        elif 85 < cronometro1 <= 90:
            screen.blit(logo[17], (160, 190))
        elif 90 < cronometro1 <= 95:
            screen.blit(logo[18], (160, 190))
        elif 95 < cronometro1 <= 100:
            screen.blit(logo[19], (160, 190))
        elif 100 < cronometro1 <= 105:
            screen.blit(logo[20], (160, 190))
        elif 105 < cronometro1 <= 110:
            screen.blit(logo[21], (160, 190))
        elif 110 < cronometro1 <= 115:
            screen.blit(logo[22], (160, 190))
        elif 115 < cronometro1 <= 120:
            screen.blit(logo[22], (160, 190))
        else:
            screen.blit(logo[21], (160, 190))
            cronometro1 = 0
            contadorG = -100
            apresentacao += 1
    #Controle de animação do Texto
    elif apresentacao == 2:
        cronometro1 += 1
        screen.blit(logo[10], (160, 190))
        if contadorG < 270:
            screen.blit(font.render('Apresenta', 1, resources.PRETO), (contadorG, 439))
            contadorG += 20
        else:
            screen.blit(font.render('Apresenta', 1, resources.PRETO), (270, 439))
            if cronometro1 > 50:
                apresentacao += 1
                cronometro1 = 0
                contadorG = 0
    #Controle de animação Sequencia projeto K
    elif apresentacao == 3:
        screen.blit(imgProjetoK, (0, 0))
        cronometro1 += 1
        if cronometro1 > 60:
            screen.blit(imgPKFatec, (0, 0))
            if cronometro1 > 120:
                apresentacao += 1
                cronometro1 = 0
    #Abertura do jogo
    elif apresentacao == 4:
        cronometro1 += 1
        if cronometro1 <= 10:
            screen.blit(cgInicial[0], (0, 0))
        elif 5 < cronometro1 <= 10:
            screen.blit(cgInicial[1], (0, 0))
        elif 10 < cronometro1 <= 15:
            screen.blit(cgInicial[2], (0, 0))
        elif 15 < cronometro1 <= 20:
            screen.blit(cgInicial[3], (0, 0))
        elif 20 < cronometro1 <= 25:
            screen.blit(cgInicial[4], (0, 0))
        elif 25 < cronometro1 <= 30:
            screen.blit(cgInicial[5], (0, 0))
        elif 30 < cronometro1 <= 35:
            screen.blit(cgInicial[6], (0, 0))
        elif 35 < cronometro1 <= 40:
            screen.blit(cgInicial[7], (0, 0))
        elif 40 < cronometro1 <= 45:
            screen.blit(cgInicial[8], (0, 0))
        elif 45 < cronometro1 <= 50:
            screen.blit(cgInicial[9], (0, 0))
        elif 45 < cronometro1 <= 55:
            screen.blit(cgInicial[10], (0, 0))
        elif 50 < cronometro1 <= 60:
            screen.blit(cgInicial[11], (0, 0))
        elif 55 < cronometro1 <= 65:
            screen.blit(cgInicial[12], (0, 0))
        elif 60 < cronometro1 <= 70:
            screen.blit(cgInicial[13], (0, 0))
        elif 65 < cronometro1 <= 75:
            screen.blit(cgInicial[14], (0, 0))
        elif 70 < cronometro1 <= 80:
            screen.blit(cgInicial[15], (0, 0))
        elif 75 < cronometro1 <= 85:
            screen.blit(cgInicial[16], (0, 0))
        elif 80 < cronometro1 <= 90:
            screen.blit(cgInicial[17], (0, 0))
        elif 85 < cronometro1 <= 95:
            screen.blit(cgInicial[18], (0, 0))
        elif 90 < cronometro1 <= 100:
            screen.blit(cgInicial[19], (0, 0))
        elif 95 < cronometro1 <= 105:
            screen.blit(cgInicial[20], (0, 0))
        elif 100 < cronometro1 <= 110:
            screen.blit(cgInicial[21], (0, 0))
        elif cronometro1 > 110:
            screen.blit(cgInicial[22], (0, 0))
        if cronometro1 > 120:
            apresentacao += 1
            cronometro1 = 0
            cgInicial.clear()
            return 'escreverNome', 0
    return 'abertura', apresentacao

#Tela de espera para o Multiplayer
def aguardarJogadores(idioma, conectionC, serverIp, nome, avatarJogador):
    global s, host, porta, instruction, player

    mouse = pygame.mouse.get_pos()
    font = pygame.font.Font('font/Pixellari.ttf', 45)
    font2 = pygame.font.Font('font/Pixellari.ttf', 25)
    font3 = pygame.font.Font('font/Pixellari.ttf', 35)
    screen.blit(lobbyBg, (0, 0))

    screen.blit(spriteSheetAvatar[avatarJogador], menuDic['posAvatarSalaEspera'])
    screen.blit(font2.render(nome, 1, resources.BRANCO), menuDic['nomeSalaEspera'])

    botaoRetConfirm = pygame.Rect(menuDic['btnConfirmServer'][0], menuDic['btnConfirmServer'][1], botao.get_width(), botao.get_height())

    if botaoRetConfirm.collidepoint(mouse):
        screen.blit(botao2, menuDic['btnConfirmServer'])
    else:
        screen.blit(botao, menuDic['btnConfirmServer'])
    screen.blit(font3.render(idioma['confirmar'], 1, resources.BRANCO),(menuDic['btnConfirmServer'][0] + 10, menuDic['btnConfirmServer'][1] + 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            descomprimir_imagens()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoRetConfirm.collidepoint(mouse):
                fxBtn.play()
                if not conectionC:
                    try:
                        s.connect((serverIp, porta))
                        msgFromServer = s.recv(1024)
                        screen.blit(font2.render(idioma['aguardandoJogadores'], 1, resources.BRANCO), menuDic['txtAguardando'])
                        player = int(msgFromServer.decode('utf-8'))
                        # print('Jogador: ', player)
                        conectionC = True

                        instruction = s.recv(1024)
                        instruction = instruction.decode('utf-8')
                        instruction = instruction.split(',')

                        if player == 0:
                            instruction[14] = nome
                            instruction[17] = avatarJogador
                        elif player == 1:
                            instruction[15] = nome
                            instruction[18] = avatarJogador
                        else:
                            instruction[16] = nome
                            instruction[19] = avatarJogador

                        instruction = ','.join(str(e) for e in instruction)
                        s.send((instruction.encode('utf-8')))
                        pygame.mixer.music.load(resources.GAMEPLAY_MUSIC)
                        return 'jogandoMult', conectionC, serverIp, nome, avatarJogador
                    except socket.error:
                        # print(socket.error)
                        screen.blit(font2.render('Erro', 1, resources.BRANCO), menuDic['txtErrorLobby'])
                    finally:
                        pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                try:
                    serverIp = serverIp.split()
                    serverIp.pop(len(serverIp) - 1)
                    serverIp = ''.join(serverIp)
                except IndexError:
                    serverIp = ''.join(serverIp)
            elif event.key == pygame.K_ESCAPE:
                return 'menu', conectionC, serverIp, nome, avatarJogador
            elif event.unicode:
                serverIp += str(event.unicode)

    screen.blit(font.render(idioma['digiteServidor'], 1, resources.BRANCO), menuDic['txtLobby'])
    screen.blit(font.render(str(serverIp), 1, resources.BRANCO), menuDic['ipTxt'])

    return 'aguardandoJogadores', conectionC, serverIp, nome, avatarJogador


#Classe principal do jogo
def main():

    #Inicia processo de compressão das imagens
    comprimir_imagens()
    #Acessa varáveis globais de controle multiplayer e de animação
    global s, host, porta, instruction, player, animator
    #Inicia música principal do jogo
    pygame.mixer.music.load(resources.MENU_MUSIC)
    #Atribui uma lista de referência ao baralho
    baralho = [0, 1, 2, 3,
               4, 5, 6, 7,
               8, 9, 10, 11,
               12, 13, 14, 15,
               16, 17, 18, 19,
               20, 21, 22, 23]
    #A aplicação inicia sem conexão até que a mesma seja solicitada
    conectionC = False
    #Endereço de ip do server
    serverIp = 'localhost'
    #Matriz que controla os pontos do jogador
    pontosJogador = [0] * 3
    #Lista para cartas com jogador no multiplayer
    cartasComJogador = [None, None, None]
    #Matriz com as cartas de single player
    cartasComJogadorSingle = [[None, None, None], [None, None, None], [None, None, None]]
    #Mesa
    cartasJogadas = []
    #Função de distribuição de cartas inicia em True
    distribuir_cartas = True
    #inicialização de turno
    turno = 0
    #Inicialização de rodada
    rodada = 1
    #Definição do tempo máximo de rodada
    tempoExibicaoRodada = 85
    #Define se há uma carta virada
    cartaVirada = None
    #instância de animação da distribuiçãop do baralho
    animacaoCarta = [192, 0]
    #Instaância da spritesheet de baralho
    spritesBaralho = resources.spritesBaralho()
    #Instância de index da apresentação antes do menu
    apresentacao = 1
    #Inicialização do avatar do jogador
    avatarJogador = 6
    #Inicialização dos estados de jogo
    estadoMenu = ''

    #Inicialização dos módulos da pygame
    pygame.init()
    pygame.font.init()

    #Inicialização do estado de jogo
    estado = 'abertura'
    #Inicialização do nome de jogador
    nome = '_ _ _ _ _ _'
    #Inicializa os textos da aplicação em português
    idioma = textos.dicPortugues
    #inicializa o identificador de idioma em português
    idiomaTexto = 'Português'



    #looping de jogo
    while True:
        #Executa o estado de abertura
        if estado == 'abertura':
            #Retorna para a variável estado e apresentação o resultado da função abertura
            estado, apresentacao = abertura(apresentacao)

        #Executa o estado escrever nome
        elif estado == 'escreverNome':
            #Recebe as variáveis alteradas na tela escrever nome
            estado, nome, idioma, idiomaTexto = enterNomePlayer(idioma, nome, idiomaTexto)

        #Executa o estado Menu
        elif estado == 'menu':
            #Recebe as variáveis alteradas  da função menu
            estado, avatarJogador, estadoMenu = menu(idioma, nome, avatarJogador, estadoMenu)

        #Executa o estado configuração
        elif estado == 'configuracao':
            #Recebe as variáveis alteradas no menu configuração
            estado, idiomaTexto, idioma, nome = configuracao(idioma, idiomaTexto, nome)

        #Executa o estado avatar
        elif estado == 'avatar':
            #Recebe as variáveis alteradas no menu de seleção de avatar
            estado, avatarJogador = avatar(idioma, avatarJogador)

        #Executa o estado de sala de espera do multiplayer
        elif estado == 'aguardandoJogadores':
            #Retorna as variáveis alteradas pelo estado aguardadoJogadores
            estado, conectionC, serverIp, nome, avatarJogador = aguardarJogadores(idioma, conectionC, serverIp, nome, avatarJogador)

        #Excuta o estado de jogo Multiplayer
        elif estado == 'jogandoMult':
            #Retorna as variáveis alteradas durante a gameplay
            estado, baralho, turno, rodada, pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador, conectionC = \
                jogarMult(idioma, nome, baralho, turno, rodada,  pontosJogador, cartasComJogador, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada, conectionC)

        #Executa o estado de jogo single player
        elif estado == 'jogandoSingle':
            #retiorna as variáveis alteradas pelo jogo em single player
            estado, baralho, turno, rodada, pontosJogador, cartasComJogadorSingle, cartasJogadas, cartaVirada, animacaoCarta, distribuir_cartas, spritesBaralho, avatarJogador = \
                jogarSingle(idioma, nome, baralho, turno, rodada, pontosJogador, cartasComJogadorSingle, cartasJogadas, cartaVirada, distribuir_cartas, animacaoCarta, spritesBaralho, avatarJogador, tempoExibicaoRodada)

        #incremento para o controle de animação
        animator += 1
        #Se o tempo de animação for igual a 60
        if animator == 60:
            #retorna o controle de animação para 0
            animator = 0

        clock.tick(config.FPS)
        pygame.display.update()

main()