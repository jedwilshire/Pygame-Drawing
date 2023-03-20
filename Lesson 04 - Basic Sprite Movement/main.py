import pygame
from settings import *
# Global Variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myGroup = pygame.sprite.Group()
mySprite = pygame.sprite.Sprite(myGroup)

pygame.display.set_caption(TITLE)

def createSprite():
    mySprite.image = pygame.Surface((50, 50))
    mySprite.image.fill(MAROON)
    pygame.draw.circle(mySprite.image, WHITE, (25, 25), 10)
    mySprite.rect = mySprite.image.get_rect()
    mySprite.rect.center = (WIDTH // 2, HEIGHT // 2)
    mySprite.dx = 0
    mySprite.dy = 0
    
def update():
    mySprite.rect.x += mySprite.dx
    mySprite.rect.y += mySprite.dy
    if mySprite.rect.right >= WIDTH:
        mySprite.rect.right = WIDTH
        mySprite.dx = -mySprite.dx
    if mySprite.rect.top <= 0:
        mySprite.rect.top = 0
        mySprite.dy = -mySprite.dy
    if mySprite.rect.bottom >= HEIGHT:
        mySprite.rect.bottom = HEIGHT
        mySprite.dy = 0
    if mySprite.rect.left <= 0:
        mySprite.rect.left = 0
        mySprite.dx = 0
def draw():
    screen.fill(CYAN)
    # if not in a sprite group use .blit
    # screen.blit(mySprite.image, mySprite.rect)
    myGroup.draw(screen)
    pygame.display.update()

def onMouseDown(x, y):
    pass

def onMouseMove(x, y):
    pass   

def onKeyDown(key):
    if key == pygame.K_LEFT:
        mySprite.dx = -1
    elif key == pygame.K_RIGHT:
        mySprite.dx = 1
    elif key == pygame.K_DOWN:
        mySprite.dy = 1
    elif key == pygame.K_UP:
        mySprite.dy = -1
    else:
        mySprite.dx = 0
        mySprite.dy = 0

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
createSprite()
pygame.init()
mainloop()
