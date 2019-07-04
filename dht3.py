#!/usr/bin/python
import RPi.GPIO as GPIO
import time;time.time()
import dht11
import sqlite3

conn = sqlite3.connect("/home/pi/mydb.sqlite")
c = conn.cursor()


GPIO.setmode(GPIO.BCM)
h = dht11.DHT11(pin=18)

try:
    r = h.read()
    if r.is_valid():
        t = (r.temperature, r.humidity, time.time(),)
        c.execute("insert into dht11 values (?,?,?)",t)

        conn.commit()

except KeyboardInterrupt:
    pass

GPIO.cleanup()

