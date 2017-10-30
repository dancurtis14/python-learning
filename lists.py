# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:54:39 2017

@author: GB121361
"""

numbers = [5,6,7,8,9,0]
names = ["Yo", "Dawg", "Whats", "good"]

alpha = ["a", "b", "c", "d"]
alpha.append("e")
alpha.append("f")
d_index = alpha.index("d")
print("D_index = " + str(d_index))
del alpha[d_index]

alpha.remove("c")
print(alpha)
