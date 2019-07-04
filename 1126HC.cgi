#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time

pinSR = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSR, GPIO.IN)

channel = GPIO.wait_for_edge(pinSR, GPIO.BOTH, timeout=10000)

print("content-type:text/html")
print("")

if channel is None:
    print("0")
else:
    print("1")

GPIO.cleanup()    


