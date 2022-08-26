import pygame

pygame.init()

opc = 0
print('Escolha uma opção: \n'
      '1- Guiné\n'
      '2- Alemanha\n'
      '3- Laos\n'
      '4- sair\n')
opc = int(input('Opção: '))

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Olá, mundo!")
screen.fill((255, 255, 255))

pygame.draw.rect(screen, (255, 0, 0), (50, 50, 300, 150), 0)  # surface,cor,posição/tamanho, borda

if opc == 1:
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 150), 0)  # surface,cor,posição/tamanho, borda
    pygame.draw.rect(screen, (255, 255, 0), (150, 50, 100, 150), 0)  # surface,cor,posição/tamanho, borda
    pygame.draw.rect(screen, (0, 255, 0), (250, 50, 100, 150), 0)  # surface,cor,posição/tamanho, borda
elif opc == 2:
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 50), 0)  # surface,cor,posição/tamanho, borda
    pygame.draw.rect(screen, (255, 0, 0), (50, 100, 300, 50), 0)  # surface,cor,posição/tamanho, borda
    pygame.draw.rect(screen, (255, 255, 0), (50, 150, 300, 50), 0)  # surface,cor,posição/tamanho, borda
else:
    pygame.draw.rect(screen, (0, 0, 255), (50, 90, 300, 70), 0)  # surface,cor,posição/tamanho, borda
    pygame.draw.circle(screen, (255, 255, 255), (200, 125), 25, 0)  # Surface, cor, posição centro, raio, borda

pygame.display.flip()  # atualiza o status da tela
pygame.time.delay(8000)

pygame.quit()
