#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinDS = 17
pinSTCP = 27
pinSHCP = 22

GPIO.setup(pinDS, GPIO.OUT)
GPIO.setup(pinSTCP, GPIO.OUT)
GPIO.setup(pinSHCP, GPIO.OUT)

data = [[1,1,1,1,0,0,1,1],
        [0,0,1,1,1,1,1,1],
        [1,0,1,1,0,1,1,1],
        [0,1,1,0,0,1,1,1],
        [1,1,1,0,0,1,1,1],
        [1,0,1,1,0,1,1,1],
        [0,1,1,0,0,0,0,1],
        [0,0,0,0,0,0,0,0]]


try: 
    for i in range(len(data)):
        GPIO.output(pinSTCP, 0)
        for j in range(len(data[i])):

            GPIO.output(pinSHCP, 0)
            GPIO.output(pinDS, data[i][j])
            GPIO.output(pinSHCP, 1)
        GPIO.output(pinSTCP, 1)
        time.sleep(1)

except KeyboardInterrupt:
    pass

time.sleep(2)
GPIO.cleanup()


