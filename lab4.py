#!/usr/bin/python 
import RPi.GPIO as GPIO
import time

pinBN = 17
pinBNY = 4
pinLED = 24
pinLEDY = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinBNY,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pinLED,GPIO.OUT)
GPIO.setup(pinLEDY,GPIO.OUT)

GPIO.output(pinLED,0)
GPIO.output(pinLEDY,0)


try:
  while True:
     if GPIO.input(pinBN):
       GPIO.output(pinLED,1)
       time.sleep(0.5)
       GPIO.output(pinLED,0)
       time.sleep(0.5)
       GPIO.output(pinLED,1)
       time.sleep(0.5)
       GPIO.output(pinLED,0)
       time.sleep(0.5)
       GPIO.output(pinLED,1)
       time.sleep(0.5)
       GPIO.output(pinLED,0)
     elif GPIO.input(pinBNY):
       GPIO.output(pinLEDY,1) 
       time.sleep(0.5)
       GPIO.output(pinLEDY,0)
       time.sleep(0.5)
       GPIO.output(pinLEDY,1)
       time.sleep(0.5)
       GPIO.output(pinLEDY,0)
       time.sleep(0.5)
       GPIO.output(pinLEDY,1)
       time.sleep(0.5)
       GPIO.output(pinLEDY,0)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
