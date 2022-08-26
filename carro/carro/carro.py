# Carolina Carvalho dos Santos 32129645

from time import sleep
import pygame
from pygame.locals import *

red = (255,0,0)
white = (255,255,255)

pygame.init()

pygame.display.set_caption("Carro")
screen = pygame.display.set_mode((640, 370))
my_font = pygame.font.SysFont("lucidasanstypewriteroblique",80,bold=True,italic = False)
superficie = my_font.render("GAME OVER",True,red,white)

fundo = "fundo.png"
imagem1 = "ferrari1.png"
imagem2 = "ferrari2.png"

background = pygame.image.load(fundo)
carro = pygame.image.load(imagem1)

JogoAtivo = True

X = 0
Y = 50

while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    screen.blit(background, (0, 0))
    screen.blit(carro, (X, Y))
    pygame.display.update()
    X += 20
    pygame.time.delay(50)
    if (X == 640):
        Y = 150
        carro = pygame.image.load(imagem2)
        while X >= -100:
            screen.blit(background, (0, 0))
            screen.blit(carro, (X, Y))
            pygame.display.update()
            X -= 20
            pygame.time.delay(50)

        while X <= 640:
            carro = pygame.image.load(imagem1)
            Y = 270
            screen.blit(background, (0, 0))
            screen.blit(carro, (X, Y))
            pygame.display.update()
            X += 20
            pygame.time.delay(50)

            if X == 640:
                screen.blit(superficie, (100, 90))
                pygame.display.update()
                sleep(2)
                JogoAtivo = False

pygame.quit()
