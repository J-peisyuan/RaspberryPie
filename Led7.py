#!/usr/bin/python2.7-cgi
#coding=utf-8

import cgi
import RPi.GPIO as GPIO

form = cgi.FieldStorage()
led = form.getvalue('led')

if led is None:
    led = "1"

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

#LED亮滅
GPIO.output(15, int(led))

#以下兩行CGI專用
print "Content-type:text/text"
print


