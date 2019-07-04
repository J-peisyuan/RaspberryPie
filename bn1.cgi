#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time, cgi

form = cgi.FieldStorage()
times = form.getvalue("times")

if times is None:
    times = "1"

pinLed = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)

for i in range(int(times)):
    GPIO.output(pinLed, 1)
    time.sleep(0.5)
    GPIO.output(pinLed, 0)
    time.sleep(0.5)

GPIO.cleanup()

print("Content-type:text/html")
print("")

print("led on")
