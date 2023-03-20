import pygame
from settings import *
from writer import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
writer = Writer(screen, size = 30)
def update():
    pass

def draw():
    screen.fill(CYAN)
    pygame.draw.rect(screen, RED, pygame.Rect(200, 200, 100, 100))
    pygame.draw.polygon(screen, BLUE, [(0, 50), (100, 50), (100, 200), (50, 200)])
    pygame.draw.circle(screen, BLACK, (400, 400), 40)
    pygame.draw.circle(screen, WHITE, (100, 400), 40, width = 10)
    pygame.draw.line(screen, BLACK, (140, 100), (500, 200),
                     width = 4)
    writer.writeText(300, 300)
    pygame.display.update()
def onMouseDown(x, y):
    writer.setText('Mouse Pressed at:' + str(x) + ', ' + str(y))

def onMouseMove(x, y):
    writer.setText(str(x) + ', ' + str(y))    

def onKeyDown(key):
    writer.setText('Key: ' + pygame.key.name(key))

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
