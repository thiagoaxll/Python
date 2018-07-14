"""______________________________________________
|   Programação II -  2º Ciclo Jogos Digitais    |
|   Nome: Thiago Zacarias da Silva               |
|   Programa :  Arkanoid                         |
|   Data : 08/05/2018                            |
|________________________________________________|
"""

import pygame
import random

pygame.init()
barra = pygame.image.load('barra.png')
bola = pygame.image.load('bola.png')
clk = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Arkanoide')

retObjetos = [0] * 36
objeto = [0] * 36
regra = [1] * 36
barraX, barraY = 200, 535
blocosDestruidos = 0

for i in range(len(objeto)):
    objeto[i] = pygame.image.load('objeto.png')

bolaX, bolaY = 372, 400
velBolaX = 1
velBolaY = 1

while True:
    screen.fill((255, 255, 255))
    retBarra = barra.get_rect()

    x, y = 0, 0
    for i in range(len(objeto)):
        if i % 12 == 0:
            y += 30
            x = 12
        if regra[i] == 1:
            screen.blit(objeto[i], (x, y))
            retObjetos[i] = objeto[i].get_rect()
            retObjetos[i].left, retObjetos[i].top = x, y
        else:
            retObjetos[i] = None

        x += objeto[i].get_width() + 7

    screen.blit(barra, (barraX, barraY))
    retBarra.left, retBarra.top = barraX, barraY

    screen.blit(bola, (bolaX, bolaY))
    retBola = bola.get_rect()
    retBola.left, retBola.top = bolaX, bolaY

    bolaY += velBolaY
    bolaX += velBolaX

    if retBola.left + bola.get_width() > 800:
        velBolaX = -1

    if retBola.left < 0:
        velBolaX = 1

    if retBola.top <= 0:
        if velBolaX > 0:
            velBolaX = 1
        else:
            velBolaX = -1
        velBolaY = 1

    for i in range(len(objeto)):
        if retObjetos[i] is not None:
            if retObjetos[i].colliderect(retBola):
                regra[i] = 0
                blocosDestruidos += 1
                direction = random.randint(0, 1)
                if direction == 0:
                    velBolaX = 1
                else:
                    velBolaX = -1
                velBolaY = 1

    if retBola.colliderect(retBarra):
        velBolaY = random.uniform(-1, - 0.9)
        direction = random.randint(0, 1)
        if direction == 0:
            velBolaX = random.uniform(0.5, 1.2)
        else:
            velBolaX = random.uniform(-1, - 0.9)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if retBarra.left > 0:
                    barraX -= 90
            if event.key == pygame.K_RIGHT:
                if retBarra.left + barra.get_width() < 800:
                    barraX += 90

        clk.tick(30)

    if bolaY > 600 or blocosDestruidos > (len(objeto) - 1):
        regra = [1] * 36
        barraX, barraY = 200, 535
        bolaX, bolaY = 372, 400
        velBolaX = 1
        velBolaY = 1
        blocosDestruidos = 0

    pygame.display.update()

