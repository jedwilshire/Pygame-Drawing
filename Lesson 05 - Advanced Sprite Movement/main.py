import pygame
from settings import *
from writer import *
# Global Variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(CYAN)
pygame.display.flip()
myGroup = pygame.sprite.Group()
mySprite = pygame.sprite.Sprite(myGroup)
dt = 0
writer = Writer(screen, size = 20)
pygame.display.set_caption(TITLE)

def createSprite():
    mySprite.image = pygame.Surface((50, 50))
    mySprite.image.fill(MAROON)
    pygame.draw.circle(mySprite.image, WHITE, (25, 25), 10)
    mySprite.rect = mySprite.image.get_rect()
    mySprite.rect.center = (WIDTH // 2, HEIGHT // 2)
    mySprite.pos = [mySprite.rect.x, mySprite.rect.y]
    mySprite.dx = 60
    mySprite.dy = 60
    
def update():
    mySprite.pos[0] += mySprite.dx * dt/1000
    mySprite.pos[1] += mySprite.dy * dt/1000
    mySprite.rect.topleft = mySprite.pos
    if mySprite.rect.right >= WIDTH:
        mySprite.rect.right = WIDTH
        mySprite.dx = -mySprite.dx
    if mySprite.rect.top <= 0:
        mySprite.rect.top = 0
        mySprite.dy = -mySprite.dy
    if mySprite.rect.bottom >= HEIGHT:
        mySprite.rect.bottom = HEIGHT
        mySprite.dy = -mySprite.dy
    if mySprite.rect.left <= 0:
        mySprite.rect.left = 0
        mySprite.dx = -mySprite.dx
def draw():
    screen.fill(CYAN)
    # if not in a sprite group use .blit
    # screen.blit(mySprite.image, mySprite.rect)
    writer.setText(str(dt))
    writer.writeText(200, 200)
    myGroup.draw(screen)
    pygame.display.flip()

def onMouseDown(x, y):
    pass

def onMouseMove(x, y):
    pass   

def onKeyDown(key):
    pass

def mainloop():
    global dt
    running = True
    clock = pygame.time.Clock()
    while running:
        dt = clock.tick_busy_loop(60)
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
        
createSprite()
pygame.init()
mainloop()
