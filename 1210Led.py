#!/usr/bin/python

import paho.mqtt.subscribe as subscribe
import RPi.GPIO as GPIO

pinLED = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)

def getmsg(client, userdata, message):
    print((message.topic, message.payload))
    if message.payload == '1':
        GPIO.output(pinLED, 1)

    else:
        GPIO.output(pinLED, 0)

subscribe.callback(getmsg, "home/test")
