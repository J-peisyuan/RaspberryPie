#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time

pinBN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

channel = GPIO.wait_for_edge(pinBN,GPIO.RISING,timeout = 5000)

print("Content-type:text/html")
print("")


if channel is None:
    print("0")
else:
    print("1")


GPIO.cleanup()
