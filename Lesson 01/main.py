import pygame
from settings import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Basic Game Loop')
def update():
    pass
def draw():
    pass
def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
            update()
            draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            clock.tick(FPS)

pygame.init()
mainloop()
