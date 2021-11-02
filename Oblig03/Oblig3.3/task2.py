#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:29:11 2021

@author: kam025
"""
import numpy as np
import matplotlib.pyplot as plt # for the plotting

# a) 

def fortune_func(p, n, c0 = 1000, x0 = 100000):
    """A difference equation
        Input:  p - annual interest rate
                n - number of years
                c - consumption per year
                x0 - fortune at start             
        Returns - list of fortune
    """
    x = [None]*(n+1) # pre-assign space for lists
    
    x[0] = x0
    
    # I can for the life of me not write an equation where I convert percent 
    # to proportion
    
    # fortune changing each year
    for i in range(1,n+1):
        x[i] = x[i-1] + p*x[i-1] - c0 
    return x

# b) 

def inflation_func(p, n, I, c0 = 1000, x0 = 100000):
    """A difference equation for fortune with inflation
        Input:  p - annual interest rate
                n - number of years
                I - inflation
                c0 - consumption at start year
                x0 - fortune at start             
        Returns - list of fortune
    """
    x = [None]*(n+1) # pre-assign space for lists
    c = [None]*(n+1)
    
    x[0] = x0
    c[0] = c0        
    
    
    # Spending changing according to inflation,
    # and fortune changing accordingly
    for i in range(1,n+1):
        c[i] = c[i-1] + I*c[i-1]
        x[i] = x[i-1] + p*x[i-1] - c[i] 
    return x

if __name__ == "__main__":
    p = 0.023   # interest rate
    n = 20      # number of years 
    
    # a)
    
    fortune = fortune_func(p, n)    # list of fortune
    xvec = np.linspace(0,n,n+1)     # the years   
    
    plt.plot(xvec, fortune, label = "fortune - no inflation") # plotting
    plt.xlabel("years")    # labels
    
    
    # print legends and grid, and show the plot
    plt.legend() 
    plt.grid()
    plt.show()
    
    # b) 
    
    I = np.linspace(0.01,0.07,5) # for five different inflation rates
    
    # calculate fortune, and plot in same plot
    for i in I:
        fortune = inflation_func(p, n, i)
        plt.plot(xvec, fortune, label = f"fortune - inflation {i}") # plotting
    
    plt.xlabel("years")    # labels
    
    
    # print legends and grid, and show the plot
    plt.legend() 
    plt.grid()
    plt.show()