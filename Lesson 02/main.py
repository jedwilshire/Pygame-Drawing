import pygame
import math
from settings import *
from writer import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Drawing Canvas')
writer = Writer(screen)
def update():
    pass

def draw():
    screen.fill(CYAN)
    pygame.draw.rect(screen, RED, pygame.Rect(200, 200, 100, 100))
    pygame.draw.polygon(screen, BLUE, [(0, 50), (100, 50), (100, 200), (50, 200)])
    pygame.draw.circle(screen, BLACK, (400, 400), 40)
    pygame.draw.circle(screen, WHITE, (100, 400), 40, width = 10)
    pygame.draw.ellipse(screen, GREEN, pygame.Rect(650, 150, 50, 100))
    pygame.draw.arc(screen, NAVY,
                    pygame.Rect(650, 500, 100, 100),
                    math.radians(0), math.radians(90),
                    width = 1)
    pygame.draw.line(screen, BLACK, (140, 100), (500, 200),
                     width = 4)
    pygame.draw.lines(screen, BROWN, False,
                      [(50, 580), (100, 580), (115, 500),
                       (76, 490), (50, 490)], width = 5)
    pygame.draw.lines(screen, RED, True,
                      [(200, 580), (300, 580), (315, 500),
                       (276, 490), (250, 490)], width = 2)
    
    write_mouse_pos()
def write_mouse_pos():
    x, y = pygame.mouse.get_pos()
    writer.write(str(x) + ', ' + str(y), 750, 575)
    
    
    
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
