#!/usr/bin/python

from adxl345 import ADXL345
import time

adxl345 = ADXL345()

try:
    while True:
        axes = adxl345.getAxes(True)
        print "ADXL345 on address 0x%x:" % (adxl345.address)

        print " x = %.3fG" % ( axes['x'] ) 
        print " y = %.3fG" % ( axes['y'] ) 
        print " z = %.3fG" % ( axes['z'] ) 

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

