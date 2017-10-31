# -*- coding: utf-8 -*-
import datetime as dt

PI  = 3.141592

def circle_area(r):
    return PI*r*r

print(circle_area(5))
print(circle_area(7))
print(circle_area(9))

def add(*numbers):
    total = 0 
    for n in numbers:
        total += n
    return total

print(add(3,4,5))

def record_time(message, time = dt.datetime.now()):
    print("{:}, time: {:}".format(message,time))

record_time("It is the morning")
record_time("It is the morning", "October 31st, 2017")
