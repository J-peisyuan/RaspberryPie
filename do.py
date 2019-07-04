#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
p = GPIO.PWM(14, 50)
p.start(50)

p.ChangeFrequency(784)
time.sleep(1)

p.ChangeFrequency(659)
time.sleep(1)

p.ChangeFrequency(659)
time.sleep(1)

p.ChangeFrequency(698)
time.sleep(1)

p.ChangeFrequency(587)
time.sleep(1)

p.ChangeFrequency(587)
time.sleep(1)

p.ChangeFrequency(523)
time.sleep(1)

p.stop()
GPIO.cleanup()
