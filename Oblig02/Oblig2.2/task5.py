#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:24:46 2021

@author: kam025
"""

# Task 5

import numpy as np # calculations, yeah!
import matplotlib.pyplot as plt # for the plotting

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# Creates a function that calculates a sum using a for-loop and iterative 
# updating of 'sum'

def f_sum(x):
    """ Calculates a sum"""
    
    sum = 0
    
    for n in range(1,6): #from 1 to 5
        
        sum = sum + 2/(n*np.pi) * (np.cos(n*np.pi/2) -1) * np.sin(n*x/2)
    
    sum = -sum
    
    return sum

# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

# creates an array of length 500, closed at the lower end, open at the upper.
# uses the machine epsilon to decide on where to stop

lower = -2*np.pi    # start
upper = 6*np.pi     # stop (not including)
length = 500
space = (upper-lower)/length # spacing to find machine epsilon
upper = upper - np.spacing(space) # updated stop

x = np.linspace(lower, upper, length) # the array

# creates a function that plots, labels and shows
def f_plot(x,f):
    # plots x on x-axis, f on y-axis, and gives a label to the plot
    plt.plot(x, f, label = "function")
    plt.xlabel("x")              # labels x axis
    plt.ylabel("f(x)")           # labels y axis
    
    plt.legend()                    # prints lables
    plt.grid()                      # adds grid
    plt.show()                      # displays plot

# cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

# The same function as above, only that N is now an input
def f_sum_N(x,N):
    """ Calculates a sum"""
    
    sum = 0
    
    for n in range(1,N+1): #from 1 to N
        
        sum = sum + 2/(n*np.pi) * (np.cos(n*np.pi/2) -1) * np.sin(n*x/2)
    
    sum = -sum
    
    return sum


if __name__ == "__main__":
    
    # bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    
    # Calculates f(x) and plots
    
    f = f_sum(x)
    f_plot(x,f)    
    
    # dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    
    # Calculates f(x, N) and plots
    
    for N in [3, 6, 30, 1000]:

        f = f_sum_N(x, N)
        f_plot(x,f)
    
    










