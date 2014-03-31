import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((480,360))

WHITE = (255,255,255)
RED = (200,24,24)
BLACK = (0,0,0)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render("3", True, RED)

textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (240,180)

pygame.mouse.set_visible(False)

while True:

    DISPLAYSURF.fill(WHITE)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                for i in xrange(3, 0, -1):
                    DISPLAYSURF.fill(WHITE)
                    textSurfaceObj = fontObj.render(str(i), True, RED)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    print(i)

                DISPLAYSURF.fill(BLACK)
                pygame.display.update()
                pygame.time.wait(100);
                DISPLAYSURF.fill(WHITE)
                pygame.display.update()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.quit()

#    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
