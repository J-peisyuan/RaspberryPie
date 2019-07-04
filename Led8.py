#!/usr/bin/python2.7-cgi

import cgi, time
import RPi.GPIO as GPIO

pinBN = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN)
GPIO.setup(pinBN, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

channel = GPIO.wait_for_edge(pinBN,GPIO.RISING, timeout=5000)
        
print 'Content-type:text/text'
print

if channel is None:
    print '0'
else:
    print 'L'
GPIO.cleanup() 

