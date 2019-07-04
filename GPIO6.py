#!/usr/bin/python
#coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(17,0)
try:
    def bn_click(channel):
        GPIO.remove_event_detect(channel)
        for i in range(2):
            GPIO.output(17,1)
            time.sleep(0.5)
            GPIO.output(17,0)
            time.sleep(0.5)


        GPIO.add_event_detect(channel, GPIO.FALLING, callback=bn_click, bouncetime=200)   
    GPIO.add_event_detect(4, GPIO.FALLING, callback=bn_click, bouncetime=200)   

    while True:
        time.sleep(1000)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

