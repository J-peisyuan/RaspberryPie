#!/usr/bin/python
#coding=utf8
import speech_recognition as sr
bgsound = 5

r= sr.Recognizer()

with sr.Microphone() as source:
    print("1")
    r.adjust_for_ambient_noise(source, duration=bgsound)
    print("2")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language="zh-TW")
    print("3:")
    print(text)
except sr.UnknownValueError:
    print("4")
except sr.RequestError as e:
    print("5: {0}".format(e))
 
