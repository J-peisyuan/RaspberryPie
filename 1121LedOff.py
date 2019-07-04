#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pinLED = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.output(pinLED, 0)

print("Led off")

