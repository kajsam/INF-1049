#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:09:20 2021

@author: kam025
"""

# Task2

import random # to generate random numbers
import matplotlib.pyplot as plt # for the plotting


def random_walk(n, x0 = 0, y0 = 0):
    """A random walk on a plane.
        Input:  n - number of steps
                x0, y0 - starting point. default (0,0)
        Returns - lists locations in x and y direction
    """
    x = [None]*n # pre-assign space for lists
    y = [None]*n
     
    x[0] = x0 # starting point
    y[0] = y0
     
    for i in range(n-1): # take n-1 random steps
        
        # pick at random the length of the step
        r_leftclosed = random.random() # Random  number in the range [0.0, 1.0).        
        r = 1-r_leftclosed # right-closed as the assignment requires
         
        x[i+1] = x[i] + 2*r -1 # take a step in the x direction
         
        r_leftclosed = random.random() # Return the next random floating point number in the range [0.0, 1.0).
        r = 1-r_leftclosed # right-closed as the assignment requires
     
        y[i+1] = y[i] + 2*r -1 # take a step in the x direction
         
    return x, y
        
if __name__ == "__main__":
    n = 1000 # number of steps
    
    dust = 10 # number of dust particles
    
    for i in range(dust):
        x, y = random_walk(n) #         
    
        plt.plot(x, y) # plotting

    plt.grid()
    plt.show()
   
   
   
   
   