#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO

pinLED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.output(pinLED, 0)

print("content-type: text/html")
print("")

print("led off")


