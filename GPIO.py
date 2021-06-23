from grovepi import *
import time

port = 4
pinMode(port, "OUTPUT")

try:
    while 1:
        for i in range(256):
            analogWrite(port, i)
            time.sleep(0.01)

except:
    analogWrite(port, 0) 
