#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)
x = raw_input("please input")
y=int(x)
GPIO.output(15,y)
GPIO.Cleanup()
