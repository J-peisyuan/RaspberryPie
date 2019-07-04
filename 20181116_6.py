#!/usr/bin/python
import urllib2 as urllib
import json
import sys

location = None
if len(sys.argv) == 2:
    location = sys.argv[1]

response = urllib.urlopen('http://opendata.epa.gov.tw/ws/Data/AQI/?$format=json')

text = response.read()
list = json.loads(text)

#print(len(list))

for p in list:
   # print(p["County"] + p["SiteName"] + " : " + p["AQI"])
    tmp = p["County"] + p["SiteName"]
    if location is None:
        print (tmp + " : " + p["AQI"])
    elif location.decode("utf-8") == tmp:
        print (tmp + " : " + p["AQI"])
        break
