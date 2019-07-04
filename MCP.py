#!/usr/bin/python

from gpiozero import MCP3008
import time

m = MCP3008(channel=0)
while True:
    print (m.value)
    time.sleep(0.2)
