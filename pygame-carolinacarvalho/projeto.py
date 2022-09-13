# Carolina Carvalho dos Santos 32129645

import pygame
pygame.init()

clock = pygame.time.Clock()

# cores
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# tela
screen_w = 660
screen_h = 388
SIZE = [screen_w, screen_h]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Chill Vibes")

# importa música
pygame.mixer.music.load('carolinabela.mp3')
pygame.mixer.music.play(1)

# background principal - estático
main_background = pygame.image.load('bg1.png')

# adicionando os outros backgrounds em uma lista
bg_images = []
for i in range(2, 6):
    bg_image = pygame.image.load(f'bg{i}.png')
    bg_images.append(bg_image)

# pegando largura da bg2
bg_width = bg_images[0].get_width()

scroll = 0
def bg():
    screen.blit(main_background, (0, 0))

    for x in range(5): # repetição de 5 vezes dos backgrounds
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0)) # (backgrounds, (largura= tendo a repeticao, o scroll vai ser ajustado com base no speed, altura=0))
            speed += 1 # velocidade aumenta a cada imagem


# enquanto o usuário não clicar em fechar
done = False
while not done:
    
    bg()

    # pega a posição do mouse
    pos = pygame.mouse.get_pos()

    # se o mouse está dentro da tela ou não
    dentro = pygame.mouse.get_focused()

    if dentro:
        # se o mouse estiver na direita vai para direita e vice-versa
        if pos[0] > 330 and scroll < 700:
            scroll += 0.7
        if pos[0] < 330 and scroll > 0:
            scroll -= 0.7
    else:
        speed = 0 # parar o movimento se o mouse sair da tela


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
