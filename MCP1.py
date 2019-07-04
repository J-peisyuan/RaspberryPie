#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,1)
GPIO.output(14, GPIO.LOW)
time.sleep(2)
GPIO.setup(14,GPIO.HIGH)

GPIO.cleanup()

print "done"

