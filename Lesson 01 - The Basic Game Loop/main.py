import pygame
from settings import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
def update():
    pass

def draw():
    screen.fill(BGCOLOR)
    pygame.display.update()

def onMouseDown(x, y):
    pass

def onMouseMove(x, y):
    pass

def onKeyDown(key):
    pass

def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        update()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                onMouseMove(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMouseDown(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN:
                onKeyDown(event.key)
        clock.tick(FPS)


pygame.init()
mainloop()
