import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

xc = 100
yc = 50
xr = 100
yr =50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    yc = yc + 1
    if yc >500:
        yc = 0

    xr = xr + 1
    if xr >500:
        xr = 0

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 255, 0), (xc, yc), 50)
    pygame.draw.rect(win, (255, 100, 50), (xr, yr, 100, 50))
    pygame.display.update()

    pygame.time.delay(10)