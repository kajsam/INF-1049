#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:01:35 2021

@author: kam025
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = -x**2 + 5*x - 3
    return y

if __name__ == "__main__":
    # y = f(5) # kaller funksjonen
    
    # for i in range(10):
    #    print(f(i))    
    
    x_values = np.linspace(-4, 5, num=10)
    y_values = f(x_values)
    
    print(y_values)
    
    plt.plot(x_values, y_values)
    plt.scatter(x_values, y_values)
    plt.show()
    
    # print(x_values)
    
    # print(y)