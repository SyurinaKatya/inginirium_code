import pygame

from sprits.block import Block
from sprits.plain import Plain
from sprits.Ball import Ball

pygame.init()
win = pygame.display.set_mode((740, 840))
pygame.display.set_caption("My Arcaniod!")
pygame.display.set_icon(pygame.image.load('ing.png'))

score = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

all_sprites = pygame.sprite.Group()

plain = Plain(690, all_sprites)
ball = Ball(all_sprites)

blacks = pygame.sprite.Group()
for i in range(28):
    for j in range(3):
        Block(20 + 25 * i, 200 + 25 * j, 1, "#C2F83E", blacks, all_sprites)

    for j in range(3):
        Block(20 + 25 * i, 100 + 25 * j, 3, (165, 0, 165), blacks, all_sprites)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if ball.rect.colliderect(plain.rect):
        ball.collisions(plain.rect.center)

    cb = pygame.sprite.spritecollide(ball, blacks, True)
    if cb is not None:
        if len(cb) > 0:
            ball.block_collision(cb[0].rect.center)
            score += 1

    surf_font = my_font.render(f"SCORE: {score}", False, (255,) * 3)


    all_sprites.update()
    win.fill((0,) * 3)
    all_sprites.draw(win)
    win.blit(surf_font, (0, 0))
    pygame.display.update()

    clock.tick(90)
