#!/usr/bin/python

import cgi

form = cgi.FieldStorage()
text = form.getvalue("text")

print "Content-type:text/text"
print

#print text
#print "[echo]" + text
print "hello " + text

