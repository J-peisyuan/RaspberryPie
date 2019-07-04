#!/usr/bin/python3

import urllib.request as urllib

keyword = u'特別獎</td>                                <td><span class="t18Red">' 
response = urllib.urlopen('http://invoice.etax.nat.gov.tw/')
html = str(response.read().decode("utf-8"))

#print(html)

index_begin = html.find(keyword) + len (keyword)
index_end = index_begin + 8

#print((index_begin, index_end))

print(html[index_begin: index_end])
