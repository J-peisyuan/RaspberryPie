#!/usr/bin/python
import sqlite3

conn = sqlite3.connect("mydb.sqlite")
c = conn.cursor()

t = ("18","60","120000",)
c.execute("insert into dht11 values(?,?,?)",t)
conn.commit()
