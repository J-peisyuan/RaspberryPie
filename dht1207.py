#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import dht11,os


GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin = 18)

while True:
    r = h.read()
    if r.is_valid():
        data = str(r.temperature) + "C/" + str(r.humidity) + "%" 
        print (data)
        os.system("mosquitto_pub -t dht -m " + data)
        #break
        time.sleep(5)
