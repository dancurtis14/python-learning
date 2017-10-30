# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:29:29 2017

@author: GB121361
"""

from pprint import pprint as pretty_print
from copy import copy, deepcopy

nums_2d = [
        [1,2,3,4],
        [5,6,7,8,9]
]

print(nums_2d[1][3])

print(nums_2d)
pretty_print(nums_2d)

letters = ["A", "B", "C", "D", "E"]
letters_2d = [copy(letters), copy(letters), copy(letters)]
pretty_print(letters_2d)
letters_2d[0][0] = "F"
pretty_print(letters_2d)