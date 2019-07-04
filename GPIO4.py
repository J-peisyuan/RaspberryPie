#!/usr/bin/python
#coding=utf-8
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,0)

try:
    while True:
        input=GPIO.input(17)
        if(input):
           #GPIO.setup(4,GPIO.OUT)
            GPIO.output(4,1)
        else:
            GPIO.output(4,0)
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()


