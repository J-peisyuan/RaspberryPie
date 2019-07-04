#!/usr/bin/python2.7-cgi
import RPi.GPIO as GPIO
import time

pinLED = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.output(pinLED, 0)

print("Content-type:text/html")
print("")
print("Led off")

