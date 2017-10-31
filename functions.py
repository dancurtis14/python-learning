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

def count_vowels(s, i=0):
    if (i == len(s)): return 0
    c = s[i]
    if c in 'aeiou':
        return count_vowels(s, i+1)+1
    return count_vowels(s, i+1) + 1

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

    