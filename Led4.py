#!/usr/bin/python

import RPi.GPIO as GPIO

pinPWM = 17
freq = 1
dc = 20


GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPWM, GPIO.OUT)

p=GPIO.PWM(pinPWM, freq)
p.start(dc)

raw_input("Press return to stop")
p.stop()
GPIO.cleanup()


