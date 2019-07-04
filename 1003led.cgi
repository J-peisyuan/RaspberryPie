#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time

pinLED = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED,GPIO.OUT)

for i in range(3):

