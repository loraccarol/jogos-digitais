# Carolina Carvalho dos Santos 32129645

import math
import pygame
import random

pygame.init()
LARGURA_TELA = 800
ALTURA_TELA = 452
screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


background = pygame.image.load("background.png")
bg_width = background.get_width()
fonte = pygame.font.SysFont('Arial Black', 10)
textoSom = fonte.render ("Música ON/OFF = F10", True, (255, 255, 255), (0, 0, 0))

tiles = math.ceil(LARGURA_TELA / bg_width) +1

scroll = 0

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
music = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("airplane.png")
        self.rect = self.image.get_rect()
    # Movimenta o Player em função das teclas pressionadas
    def update(self, tecla):
        if tecla[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if tecla[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if tecla[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if tecla[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
    # Mantém o jogador no limite da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("missile.png")
        self.image = pygame.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect(
            center=(
                random.randint(LARGURA_TELA + 20, LARGURA_TELA + 100),
                random.randint(0, ALTURA_TELA),
            )
        )

        self.speed = random.randint(8, 15)
        # Remove o sprite quando atinge o limite esquerdo da tela
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
# Cria um evento próprio
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instancia um jogador (agora é um retângulo)
player = Player()

# Cria grupo para armazenar os sprites dos inimigos e todos os sprites
# inimigos são usados para detectar colisão e atualizar as posições
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

jogoAtivo = True
clock = pygame.time.Clock()

while jogoAtivo:
    
    clock.tick(20)
    tecla = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False
        if event.type == ADDENEMY:
            # Cria novo inimigo e adiciona no grupo de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    if tecla[pygame.K_F10]:
        if music:
            pygame.mixer.music.pause()
            music = False
        else:
            pygame.mixer.music.unpause()
            music = True
    
    # atualiza posição do player
    player.update(tecla)
    
    # atualiza posição dos inimigos
    enemies.update()

    scroll -= 5
    if abs(scroll) > bg_width:
        scroll = 0

    for i in range(0, tiles):
        screen.blit(background, (i* bg_width + scroll, 0))
    
    screen.blit(textoSom, (0,0))
    # Desenha todos os sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    # Verifica se algum inimigo colidiu com algum inimigo
    if pygame.sprite.spritecollideany(player, enemies):
        # Remove jogador e encerra programa
        player.kill()
        jogoAtivo = False
    # Desenha jogador na tela
    pygame.display.flip()
    
pygame.quit()

