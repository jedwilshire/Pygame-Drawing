import pygame
from settings import *
from writer import *
# Global Variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myGroup = pygame.sprite.Group()

# make sprite not in a group
# mySprite = pygame.sprite.Sprite()

# make sprite in a group
mySprite = pygame.sprite.Sprite(myGroup)

pygame.display.set_caption(TITLE)

def createSprite():
    mySprite.image = pygame.Surface((50, 50))
    mySprite.image.fill(MAROON)
    # mySprite.rect = mySprite.image.get_rect()
    
    # you can make your own rect as well
    mySprite.rect = pygame.Rect(100, 100, 50, 50)
    
def update():
    mySprite.rect.x += 1

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
createSprite()
pygame.init()
mainloop()
