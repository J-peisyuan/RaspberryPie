#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import dht11 
import urllib2
import json

GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin=18)

text = open("t.json").read()


try:
    r=h.read()
    if r.is_valid():
        data = 'api_key=MP622IJ8CNCOMA5M&field1='+str(r.temperature)+ '&field2='+str(r.humidity)+''
        print data
        request = urllib2.Request('https://api.thingspeak.com/update', data)
        response = urllib2.urlopen(request)
        print response.read()
        print str(r.temperature)+"C/"+str(r.humidity)+"%"

        list = json.loads(text)
        for p in list:
            print p["field1"],p["field2"]

except KeyboardInterrupt:
    pass

GPIO.cleanup()

