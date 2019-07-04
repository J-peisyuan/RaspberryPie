#!/usr/bin/python

import threading

class MyClass(threading.Thread):
    def __init__(self, str):
        threading.Thread.__init__(self)
        self.str=str
    
    def run(self):
        for i in range(150):
            print self.str

MyClass("A").start()
MyClass("B").start()
