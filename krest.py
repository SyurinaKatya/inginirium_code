import pygame
w,h = [int(t) for t in input().split()]
pygame.init()
win = pygame.display.set_mode((w, h))
win.fill((0,0,0))
pygame.draw.line(win,(255,255,255),(0, 0),(w, h), 5)
pygame.draw.line(win,(255,255,255),(w, 0),(0, h), 5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
