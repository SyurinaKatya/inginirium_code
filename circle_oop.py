import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
class Circle:
    def __init__(self,color,x,y,rad):
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad
        self.is_jump = False
        self.h = -30

    def move_by_keys(self):
        if self.is_jump:
            if self.h >= -30:
                self.y -= self.h
                self.h -= 3
            else:
                self.h = 30
                self.is_jump = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 3
        elif keys[pygame.K_s]:
            self.y += 3
        if keys[pygame.K_a]:
            self.y -= 3
        elif keys[pygame.K_d]:
            self.y += 3

        if keys[pygame.K_SPACE]:
            self.is_jump = True

    def draw(self, root):
        pygame.draw.circle(root, self.col, (self.x, self.y), self.rad)

circle = Circle((180, 255, 100), 250, 250,50 )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    circle.move_by_keys()

    win.fill((255, 255, 255))
    circle.draw(win)
    pygame.display.update()
    pygame.time.delay(10)