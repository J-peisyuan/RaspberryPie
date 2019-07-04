#!/usr/bin/python2.7-cgi

import RPi.GPIO as GPIO
import time

pinBN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

channel = GPIO.wait_for_edge(pinBN,GPIO.RISING,timeout = 5000)

print("Content-type:text/html")
print("")

print('<html>')
print('<head>')
print('<meta http-equiv = "refresh" content = "1" />')
print('</head>')
print('<body>')
if channel is None:
    print("time out")
else:
    print("put down",channel)

print('</body>')
print('</html>')

GPIO.cleanup()
