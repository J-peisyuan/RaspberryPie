#!usr/bin/python 

import RPi.GPIO as GPIO
import time,threading

leftBN = 4
rigthBN = 3
leftLED = 15
rightLED = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(leftBN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightBN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(leftLED,GPIO.OUT)
GPIO.setup(rightLED,GPIO.OUT)

def ledOn(pin):
    GPIO.output(pin, 1)
    time.sleep(3)
    GPIO.output(pin, 0)

def bnClick(channel):
    threading.Thread(target=ledOn, args=[leftLED if channel == leftBN else rightLED]).start()

GPIO.add_enent_detect(leftBN, GPIO.BOTH, callback=bnClick)
GPIO.add_enent_detect(rightBN, GPIO.BOTH, callback=bnClick)

try:
    while True:
        time.slep(1000000)

except KeyboardInterrupt:
    pass
GPIO.cleanup()
