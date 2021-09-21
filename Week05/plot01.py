#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:23:05 2021

@author: kam025
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 10

def g(x):
    return x + 2

if __name__ == "__main__":
    x1 = np.linspace(-5,5,393)
    x2 = np.linspace(-3, 3, 43)
    y = f(x1)
    z = g(x1)
    
   # for i in range(len(x1)):
   #     print("x=", x1[i], "y=", y[i])

            
    plt.plot(x1, y, label = "f(x)")
    plt.plot(x1, z, label = "g(x)")
    plt.axhline(0, color="red")
    plt.axvline(0, color="magenta")
    plt.legend()
    # plt.scatter(x1, y)
    plt.grid()
    plt.show()
    