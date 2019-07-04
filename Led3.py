#!/usr/bin/python
#coding=utf-8

import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(17,0)
GPIO.output(24,0)

class MyClass(threading.Thread):
    def __init__(self, channel):
        threading.Thread.__init__(self)
        self.channel=channel

    def run(self):
        ledPin = 24
        if self.channel == 4:
            ledPin = 17

        for i in range(3):
            GPIO.output(ledPin,1)
            time.sleep(0.5)
            GPIO.output(ledPin,0)
            time.sleep(0.5)

try:
    def bn_click(channel):
        MyClass(channel).start()

    GPIO.add_event_detect(4,GPIO.FALLING, callback=bn_click, bouncetime=200)
    GPIO.add_event_detect(26,GPIO.FALLING, callback=bn_click, bouncetime=200)

    while True:
        time.sleep(1000)

except KeyboardInterrupt:
    pass
GPIO.cleanup()
