#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import dht11

GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin = 18)

while True:
    r = h.read()
    if r.is_valid():
        data=str(r.temperature)  + "," + str(r.humidity) 
        print(data)
        break
    time.sleep(2)


