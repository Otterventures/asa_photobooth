import RPi.GPIO as GPIO
import pygame, sys, time, picamera, datetime

from pygame.locals import *

# setup GPIO Stuff
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.IN)
prevState = GPIO.input(3)

# setup pygame stuff
pygame.init()
DISPLAYSURF = pygame.display.set_mode((0,0))
WHITE = (128,128,128)
RED = (255,0,0)
BLACK = (0,0,0)
fontObj = pygame.font.Font('freesansbold.ttf', 128)
textSurfaceObj = fontObj.render("3", True, RED)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (DISPLAYSURF.get_width() / 2, DISPLAYSURF.get_height() / 2)
pygame.mouse.set_visible(False)

#setup picamera stuff
#camera = picamera.PiCamera()

with picamera.PiCamera() as camera:
    camera.preview_fullscreen = True
    camera.preview_layer = 2
    camera.preview_alpha = 225
    camera.start_preview()
    
    while True:

        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        btnState = GPIO.input(3)

        while not (btnState == prevState):
            if (not btnState):
                time = str(datetime.datetime.now())
                filename = 'photos/' + time.replace(' ', '_') + '.jpg'
                for i in xrange(3, 0, -1):
                    DISPLAYSURF.fill(WHITE)
                    textSurfaceObj = fontObj.render(str(i), True, RED)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                    pygame.display.update()
                    pygame.time.wait(1000)

                DISPLAYSURF.fill(BLACK)
                pygame.display.update()
                camera.preview_alpha = 0
                camera.capture(filename)
                pygame.time.wait(100);
                camera.preview_alpha = 225
                DISPLAYSURF.fill(WHITE)
                pygame.display.update()

                prevState = btnState
            else :
                prevState = btnState

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    camera.stop_preview
                    camera.close()
                    pygame.quit()
                    sys.exit()

