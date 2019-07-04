#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import dht11
import urllib2


GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin = 18)

print "debug0"

try:
    print "debug1"
    r = h.read()
    print "debug2"

    for i in range(5):
        if r.is_valid():
            response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=MP622IJ8CNCOMA5M&field1=' + str(r.temperature) + '&field2=' + str(r.humidity))
            print response.read()
            print str(r.temperature) + "C /" + str(r.humidity) + "%"
            break
        else:
            print "error"
            time.sleep(2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
