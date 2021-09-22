#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:47:34 2021

@author: kam025
"""

import numpy as np
import time # to check how fast/slow things are going

# Task 3

print("\n(a)") # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

lower = 0 # lower bound
upper = 2*np.pi # upper bound
length = 10 # number of elements

# The exercise requires an array between 0 and 2pi, so I'm adding and subtracting
# the machine epsilon relative to the even space including 0 and 2pi

space = (upper-lower)/length

# array between lower and upper
lower = lower + np.spacing(space)
upper = upper - np.spacing(space)

x = np.linspace(lower, upper, length)

print(x)


# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

def f_loop(x):
    f = np.zeros(len(x)) 
    for i in range(len(x)):
        if x[i] > np.pi:
            f[i] = -1
        else:
            f[i] = np.cos(x[i])
    return f
    

def f_not_vec(x): 
    """This function takes a single input x and applies f() """
    
    if x > np.pi:        # test if it is larger than pi
        return -1           # return -1
    else:
        return np.cos(x) # return cosinus
            
# ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

def f_manual_vec(x):
    """Takes an array x and applies f() to each element."""
    f = np.ones(len(x))     # makes an array of same size as x
    f = f*-1                # multiply by -1
    idx = x<=np.pi          # finds values smaller than pi
    
    f[idx] = np.cos(x[idx]) # assign cos(x) value
    
    return f                # return array

# dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

# vectorizing a function

vfunc = np.vectorize(f_not_vec)


if __name__ == "__main__":
    
    print("\n(b)") 
    
    t = time.time()             # start time
    f = np.zeros(len(x))        # declare array
    for i in range(len(x)):     # run function for each element
        f[i] = f_not_vec(x[i])
    elapsed = time.time() - t   # end time - start time
    print(f"Loop-call: {elapsed}. f: {f}")
    
    print("\n(c)") 
    t = time.time()             # start time
    f = f_manual_vec(x)
    elapsed = time.time() - t   # end time - start time
    print(f"Element-wise: {elapsed}. f: {f}")
    
    print("\n(d)")
    t = time.time()             # start time
    f = vfunc(x) 
    elapsed = time.time() - t   # end time - start time
    print(f"Vectorized: {elapsed}. f: {f}")
    
    
    print("\n") 
    t = time.time()             # start time
    f = f_loop(x)
    elapsed = time.time() - t   # end time - start time
    print(f"For-loop: {elapsed}. f: {f}")
    
    print("Comment: By calculating f(x) for an array with 1,000,000 elements, \
we clearly see that the looped call is the slowest, followed by a conventional \
for-loop. The element-wise operations are fastest, and the vectorized function \
in between.")
    
    
    
    
        