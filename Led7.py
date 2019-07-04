#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pinBN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(pinBN):
            print "down" 
        time.sleep(0.1)
    except KeyboardInterrupt:
        pass
GPIO.cleanup() 
