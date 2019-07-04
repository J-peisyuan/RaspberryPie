#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

for i in range(3):
    print("on")
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,0)
    time.sleep(1)

    
    print("off")
    GPIO.setup(17,GPIO.IN)
   #GPIO.output(17,1)
    time.sleep(1)

GPIO.cleanup()
