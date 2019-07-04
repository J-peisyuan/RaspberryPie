#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time
import dht99
import urllib2
import cgi 
GPIO.setmode (GPIO.BCM)
h = dht99.DHT11(pin = 18)

try:
    r = h.read()
    
    for i in range(5):
        if r.is_valid():
            data = 'api_key=MP622IJ8CNCOMA5M&field1=' + str(r.temperature) + '&field2=' + str(r.humidity)
           # print data
            request = urllib2.Request('https://api.thingspeak.com/update', data)
            response = urllib2.urlopen(request)
            # print response.read()
            print ("Content-type:text/json")
            print("")
            print "{\"temperature\":"  +  str(r.temperature) + ", \"humidity\":"  + str(r.humidity) +  "}"
            break
        else:
            time.sleep(2)

except KeyboardInterrupt:
    pass
GPIO.cleanup()

