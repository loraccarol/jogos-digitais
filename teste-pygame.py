import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Olá, mundo!")
screen.fill((0,0,255))

pygame.draw.rect(screen,(255, 255, 255),(150, 20, 300, 300), 4) # surface,cor,posição/tamanho, borda

pygame.draw.line(screen,(255, 255, 255),(250, 20), (250, 320), 4) # surface,cor,posição inicio, posição fim, espessura
pygame.draw.line(screen,(255, 255, 255),(350, 20), (350, 320), 4) # surface,cor,posição inicio, posição fim, espessura

pygame.draw.line(screen,(255, 255, 255),(150, 120), (450, 120), 4) # surface,cor,posição inicio, posição fim, espessura
pygame.draw.line(screen,(255, 255, 255),(150, 220), (450, 220), 4) # surface,cor,posição inicio, posição fim, espessura

pygame.draw.circle(screen,(255, 255, 0),(300, 170),20, 0) # Surface, cor, posição centro, raio, borda

pygame.display.flip() # atualiza o status da tela
pygame.time.delay(5000)


pygame.quit()
