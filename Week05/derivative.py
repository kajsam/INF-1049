#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:14:34 2021

@author: kam025
"""

import numpy as np
import matplotlib.pyplot as plt

from bisection01 import f

# def f(x):
#    return -x**2 + 10

def derivative(f, low, high, dx):
    space = int(1/dx*(high-low))
    x = np.linspace(low, high, space)
    y = f(x)
    dy = np.zeros(len(x))
    for i in range(len(dy)-1):
        dy[i] = (y[i+1] - y[i]) / dx
        
    return x, y, dy

def square_integral(f, low, high, eps):
    space = int(1/dx*(high-low))
    x = np.linspace(low, high, space)
    y = f(x)
    integ = np.zeros(len(x))
    s = 0
    for i in range(1, len(y)):
        s += y[i] * eps
        integ[i] = s
    return integ

def trapeziod_integral(f, low, high, eps):
    space = int(1/dx*(high-low))
    x = np.linspace(low, high, space)
    y = f(x)
    integ = np.zeros(len(x))
    s = 0
    for i in range(1, len(y)-1):
        s += (y[i] + y[i+1]) /2 * eps
        integ[i] = s
    return integ


    
if __name__ == "__main__":
    low = -5
    high = 5
    dx = 0.1
    x1, y1, dy1 = derivative(f, low, high, dx)
    
    s1 = square_integral(f, low, high, dx)
    print(s1[-2])
    
    s2 = trapeziod_integral(f, low, high, dx)
    print(s2[-2])
    
    plt.plot(x1[:-1], y1[:-1], label = "fun")
    plt.plot(x1[:-1], dy1[:-1], label = "der")
    plt.plot(x1[:-1], s1[:-1], label = "integ")
    plt.plot(x1[:-1], s2[:-1], label = "trap")
    plt.axhline(0, color="red")
    plt.axvline(0, color="magenta")
    
    plt.legend()
    plt.grid()
    plt.show()
    


# 59.24
