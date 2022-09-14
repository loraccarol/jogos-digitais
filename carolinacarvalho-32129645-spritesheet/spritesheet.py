#Carolina Carvalho dos Santos 32129645

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((537, 360))

sprite_sheet = pygame.image.load("imagem.png")
fundo = pygame.image.load("ponte2.png")
pedra = pygame.image.load("pedra.png")

def get_frame (gId, colunas, altura, largura, espaco_h, espaco_v, margem, topo):
    global sprite_sheet
    linha = gId // colunas #linha onde se encontra o frame desejado
    coluna = gId % colunas #coluna onde se encontra o frame desejado
    x = (coluna * (largura + espaco_h)) + margem
    y = (linha * (altura + espaco_v)) + topo
    
    return sprite_sheet.subsurface(pygame.Rect((x,y),(largura,altura)))

listaEsq = [5, 6, 7, 8 , 9]
listaDir = [10, 11, 12, 13, 14]
listaUp = [15, 16, 17, 18, 19]
listaDown = [0, 1, 2, 3, 4]

listaQuadros = listaDir
quadro = 0
velocidade = 12
mover = False

fps = pygame.time.Clock()

x = 0
y = 160

ativo = True
while ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ativo = False

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                mover = False
                quadro = 0

    if evento.type == pygame.KEYDOWN:
        mover = True
        if evento.key == pygame.K_LEFT:
            x -= 8
            listaQuadros = listaEsq
        if evento.key == pygame.K_RIGHT:
            x += 8
            listaQuadros = listaDir
        if evento.key == pygame.K_UP:
            y -= 8
            listaQuadros = listaUp
        if evento.key == pygame.K_DOWN:
            y += 8
            listaQuadros = listaDown

    screen.blit(fundo, (0,0))
    screen.blit(pedra, (80,150))
    screen.blit(pedra, (450,80))
    screen.blit(pedra, (80,290))

    gid = listaQuadros[quadro]
    frame = get_frame(gid,5,40,40,0,0,0,0)

    if mover:
        quadro = quadro + 1
    if quadro >= len(listaQuadros):
        quadro = 0
    if y < 0:
        y = 0
    if y > 300:
        y = 300

    if x < 0:
        x = 0
    if x > 500:
        x = 500


    if x >= 70 and x < 80 and y > 50:
        x = 70
    if y > 50 and x >= 80:
        y = 50
    screen.blit(frame, (x,y))

    pygame.display.update()
    fps.tick(15)

pygame.quit()
exit()