import RPi.GPIO as GPIO
import pygame, sys
from pygame.locals import *

# setup GPIO Stuff
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.IN)
prevState = GPIO.input(3)

# setup pygame stuff
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
    btnState = GPIO.input(3)

    while not (btnState == prevState):
        if (not btnState):
            for i in xrange(3, 0, -1):
                DISPLAYSURF.fill(WHITE)
                textSurfaceObj = fontObj.render(str(i), True, RED)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                pygame.display.update()
                pygame.time.wait(1000)

            DISPLAYSURF.fill(BLACK)
            pygame.display.update()
            pygame.time.wait(100);
            DISPLAYSURF.fill(WHITE)
            pygame.display.update()

            prevState = btnState
        else :
            print "buttom released"
            prevState = btnState

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
