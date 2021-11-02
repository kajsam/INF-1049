#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:28:19 2021

@author: kam025
"""

# Task 1

import numpy as np
from math import sqrt, pi, cos, sin # cooler than numpy
import matplotlib.pyplot as plt # for the plotting

# a) 

def diff_func(n, x0 = 3, x1 = 2):
    """A difference equation
        Input:  n - number of differences
                x0 - first entry
                x1 - second entry
        Returns - list of subsequent entries
    """
    x = [None]*(n+1) # pre-assign space for lists
    
    x[0] = x0 # first and second entry
    x[1] = x1
    
    # from third entry until last
    for i in range(2,n+1): 
        x[i] = 2 - 2*x[i-1] + 2*x[i-2]
    return x

# b)

def n_func(n):
    """A function
        Input: n - a number
        Returns a list f"""
        
    f = [None]*(n+1) # pre-assign space for lists
    
    for i in range(0,n+1):       
      f[i] = 2 + ((-sqrt(2))**i)*(cos(pi*i/4) - sqrt(3)/2*sin(pi*i/4))
    
    return f
    
if __name__ == "__main__":
    
    n = 7
    
    # a)
    x = diff_func(n)
    
    # b)
    f = n_func(n)
    
    xvec = np.linspace(0,n,n+1) # making a vector 
        
    plt.plot(xvec, x, label = "difference func") # plotting
    plt.plot(xvec, f, label = "other func") # plotting
    plt.xlabel("n")    # labels
    
    # print legends and grid, and show the plot
    plt.legend() 
    plt.grid()
    plt.show()
    