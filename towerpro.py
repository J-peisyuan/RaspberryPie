#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 50)
p.start(0)

p.ChangeDutyCycle(2.5)
time.sleep(0.4)

p.ChangeDutyCycle(12)
time.sleep(0.4)

p.ChangeDutyCycle(7.25)
time.sleep(0.4)

p.stop()
GPIO.cleanup()
