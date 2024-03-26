import random


import pygame as pg


pg.init()
size = W, H = 700, 700
FPS = 30
win = pg.display.set_mode(size)


class Inginirium(pg.sprite.Sprite):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) * random.choice((1, -1)),
                                   random.randrange(3) * random.choice((1, -1)))


all_spryte = pg.sprite.Group()
for _ in range(50):
    Inginirium(all_spryte)

clock = pg.time.Clock()

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    all_spryte.update()
    win.fill((255,)*3)
    all_spryte.draw(win)
    pg.display.update()
    pg.display.update()
