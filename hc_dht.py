#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)

try:
    while True:
        GPIO.input(14)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
