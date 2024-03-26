import random

import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, color, x, y, rad):
        self.dir = 'r'
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad

    def horizontal_move(self):
        if self.x > 500 - self.rad:
            self.dir = "l"
        elif self.x < 0 + self.rad:
            self.dir = "r"
        if self.dir == "r":
            self.x += 3 
        elif self.dir == "l":
            self.x -= 3

    def draw(self, root):
        pygame.draw.circle(root, self.col, (self.x, self.y), self.rad)

FPS = 60
clock = pygame.time.Clock()
circles = []
for i in range(180):
    circles.append(Circle(random.choices(range(256), k=3), i * 10, i * 5, 30))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for i in range(180):
        circles[i].horizontal_move()
    win.fill((255, 255, 255))
    for i in range(100):
        circles[i].draw(win)
    pygame.display.update()
    pygame.time.delay(10)
    clock.tick(FPS)