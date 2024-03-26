import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 100
speed = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if abs(250 - x) > 150 or abs(250 - y) > 150:
        color = (255, 0, 0)
        speed = 1
    else:
        color = (250, 250, 0)
        speed = 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 25:
        x -= speed
    elif keys[pygame.K_RIGHT] and x <= 500 - 25:
        x += speed
    elif keys[pygame.K_UP] and y >= 25:
        y -= speed
    elif keys[pygame.K_DOWN] and y <= 500 - 25:
        y += speed
    else:
        if x > 250:
            x -= speed
        elif x < 250:
            x += speed
        if y > 250:
            y -= speed
        elif y < 250:
            y += speed

    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (x, y), 25)
    pygame.display.update()
    pygame.time.delay(10)