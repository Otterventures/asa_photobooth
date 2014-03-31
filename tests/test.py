import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(3,GPIO.IN)

prevState = GPIO.input(3)

while True:
    btnState = GPIO.input(3)
    while not (btnState == prevState):
        if (not btnState):
            print "button pressed"
            prevState = btnState
        else :
            print "buttom released"
            prevState = btnState
