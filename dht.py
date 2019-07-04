#!/usr/bin/python

import RPi.GPIO as GPIO
import time, dht11

GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin=18)

try:
    while True:
        r = h.read()
        if r.is_valid():
            print str(r.temperature) + "C /" + str(r.humidity) + "%"
            time.sleep(5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
        
