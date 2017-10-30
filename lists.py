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

alpha2 = ["g", "i", "h"]
alpha2.sort()
print(alpha2)

alpha.insert(2, "c")
alpha.insert(3, "d")
print(alpha)

alpha = ''.join(alpha)
alpha2 = ''.join(alpha2)
print(alpha)
print(alpha2)

alphabet = alpha + alpha2
print(alphabet)