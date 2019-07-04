#!/usr/bin/python

import urllib2 as urllib
import json

#response = urllib.urlopen('http://www.apple.com.tw')

response = urllib.urlopen('http://opendata.epa.gov.tw/ws/Data/AQI/?$format=json')
text = response.read()
print(text)
#list = json.loads(text)
#print(len(list))
#for p in list:
 #   print(p["County"]+p["SiteName"]+":"+ p["AQI"])
#print(response.read())


