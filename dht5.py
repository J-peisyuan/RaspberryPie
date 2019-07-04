#!/usr/bin/python
import sqlite3

conn = sqlite3.connect("/home/pi/mydb.sqlite")
c = conn.cursor()

rs = c.execute("select * from dht11 order by dd desc limit 1,10")

print "Content-type:text/html"
print

print'<html>'
print'<head>'
print'</head>'
print'<body>'
print'<table border="1">'
print'    <tr>'
print'        <td>T</td>'
print'        <td>H</td>'
print'        <td>DD</td>'
print'    </tr>'
		
for row in rs:	
   print'<tr>'
   print'    <td>' + str(row[0]) +'</td>'
   print'    <td>' + str(row[1]) +'</td>'
   print'    <td>' + str(row[2]) +'</td>'
   print'</tr>'
print'</table> '
    	
print'</body>'
print'</html>'
