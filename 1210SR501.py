#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pinSR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSR, GPIO.IN)

try: 
    while True:
        print(GPIO.input(pinSR))
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
    

