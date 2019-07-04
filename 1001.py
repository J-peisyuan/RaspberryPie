#!/usr/bin/python

from gpiozero import MCP3008
import time

m = MCP3008(channel = 0)
while True:
    print (int(m.value * 10000))
    time.sleep(0.2)
