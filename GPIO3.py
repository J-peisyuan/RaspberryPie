#!/usr/bin/python
#coding=utf-8
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(17,0)
GPIO.output(24,0)

try:
    while True:
        input=GPIO.input(4)
        input=GPIO.input(26)
        if(input):
            GPIO.output(17,1)
            GPIO.output(24,1)
        else:
            GPIO.output(17,0)
            GPIO.output(24,0)
        time.sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
