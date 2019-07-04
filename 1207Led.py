#!/usr/bin/python

import RPi.GPIO as GPIO

pinLED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)

while True:
    GPIO.output(pinLED, int(raw_input()))
