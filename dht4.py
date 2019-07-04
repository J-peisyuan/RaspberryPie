#!/usr/bin/python

import RPi.GPIO as GPIO
import time;time.time()
import dht11
import sqlite3

conn = sqlite3.connect("/home/pi/mydb.sqlite")
c = conn.cursor()

rs = c.execute("select * from dht11")
for row in rs:
    print row[0], row[1], row[2]

print "Content-type:text/html"
print
