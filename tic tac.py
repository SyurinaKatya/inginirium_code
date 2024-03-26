import pygame as pg

pg.init()
W, H = 600, 600
FPS = 60
win = pg.display.set_mode((W, H))
pg.display.set_caption("TIC TAC TOE!)")


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

