#!/usr/bin/python

import urllib2 as urllib
import json

response = urllib.urlopen('http://opendata.epa.gov.tw/ws/Data/AQI/?$format=json')

text = response.read()
list = json.loads(text)

print(len(list))

for p in list:
    print(p["County"] + p["SiteName"] + " : " + p["AQI"])

