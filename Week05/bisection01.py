#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:10:13 2021

@author: kam025
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 10

def bisect(f, a , b, eps):
    midpoint = a
    while not abs(0-f(midpoint)) < eps:
        midpoint = (a+b) / 2
        if f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint
    return midpoint

if __name__ == "__main__":
    a = 0
    b = 4
    eps = 0.0001
    root = bisect(f, a, b, eps)
    
    print(root)