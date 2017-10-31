# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:42:32 2017

@author: GB121361
"""

from math import pi

def sphere_vol(r):
    return (4/3)*pi*r*r*r

def cube_vol(l,w,h):
    return l*w*h

def cone_vol(r,h):
    return(pi*r*r)*h/3