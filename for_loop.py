# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:31:09 2017

@author: GB121361
"""

odds = [1,3,5,7,9,11]

print(range(len(odds)))
for index in range(len(odds)):
    print("Index: {:d}, Odd Number: {:d}".format(index, odds[index]))