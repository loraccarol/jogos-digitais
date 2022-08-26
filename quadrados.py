# Carolina Carvalho TIA: 32129645
# Michele Ramos TIA: 32166052

import random
import pygame

white = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quadrados")

screen.fill(white)

class Quadrado:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.cor = (0, 0, 0)
        self.posX = 0
        self.posY = 0

    def sorteiacor(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def sorteiax(self):
        self.posX = random.randint(1, 600)

    def sorteiay(self):
        self.posY = random.randint(1, 400)

    def mostra_quadrado(self):
        pygame.draw.rect(screen, self.cor, (self.posX, self.posY, self.largura, self.altura))

def main():
    quadrado = Quadrado(250, 250)
    while(quadrado.largura != 0):
        quadrado.sorteiacor()
        quadrado.sorteiax()
        quadrado.sorteiay()
        quadrado.mostra_quadrado()
        quadrado.altura = int(quadrado.altura / 2)
        quadrado.largura = int(quadrado.largura / 2)
    
main()
pygame.display.flip() # atualiza o status da tela
pygame.time.delay(3000)

pygame.quit()
