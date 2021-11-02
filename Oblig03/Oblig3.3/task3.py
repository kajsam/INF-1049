#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:53:34 2021

@author: kam025
"""

# Task 3

import numpy as np
from math import sin, pi
import matplotlib.pyplot as plt # for the plotting

# a) Signal with noise

delta_t = 0.01 # the distance between two timepoints
t = np.arange(0,10,delta_t) # all timepoints   
N = len(t) # number of timepoints 

w = np.random.normal(0,2,N+1) # ransom noise

f = 2 # some constant

y = [None]*(N) # pre-assign space for lists
x = [None]*(N)

# for all time points, make the signal, add noise
for i in range(N):
    x[i] = sin(2*pi*f*t[i])
    y[i] = x[i] + w[i]
    
# plot signal with and without noise
plt.plot(t, y, label = "signal with noise") # plotting
plt.plot(t, x, label = "signal") # plotting
plt.xlabel("time")    # labels
        
# b) 3-term moving average filter


n = 3 # length of the filter

S = [None]*N

for i in range(1,N-1): # for each time point except the first and the last
    s = 0
    for k in range(-1,2): # sum up the neighbouring signals
        s = s + y[i-k]
        
    S[i] = (1/n)*s # calculate the mean   
    

# c)


plt.plot(t, S, label = "filtered, 3-term")


# d)

def low_pass(M, y):
    """Moving average
    Input:  M - number of terms in each direction
            y - the noisy signal
    Output:  S - filtered signal
    """
        
    N = len(y) # length of signal
    
    for i in range(M,N-M): # for each time point except the M first and last
        s = 0
        for k in range(-M,M+1): # sum up the neighbouring signals
            s = s + y[i-k]
        
        S[i] = 1/(2*M+1)*s # calculate the mean   
        
    return S
        
M = [3, 11, 21] # M does not correspond to the length of the filter


for m in M:    
    S = low_pass(m, y)
    plt.plot(t, S, label = f"filtered {2*m-1}-term")


# print legends and grid, and show the plot
plt.legend() 
plt.grid()
plt.show()

# The figure in the assignment does not correspond to eq. 5, this one does. 

    
    



    
        
    
    
    