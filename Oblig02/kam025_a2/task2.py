#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:51:24 2021

@author: kam025
"""
# Task 2 

import numpy as np # importing the best library for computations (mathematical)

print("\n1.") # Evenly spaced list

lower = 0 # first element of the list
upper = 7 # last element of the list
length = 12 # number of elements
space = (upper-lower)/(length-1) # equal spacing

# making the evenly spaced list:
ev_list = [lower + x*space for x in range(length)]
rev_list = [round(elem,3) for elem in ev_list] # rounding for nice display

print(f"List: {rev_list}")

print("\n2.") # Evenly spaced numpy array

ev_array = np.linspace(lower, upper, length)

print(f"Array: {ev_array}")

print(f"\n3.")

# Anything that can be iterated over is an iterable. 

def iterable_or_not(x): 
    """ Cheks if an object is an iterable.
    Returns true or false accordingly. Prints the class and the result. 
    """
    
    try: 
        iter(x)
    except TypeError:
        print(f"{type(x).__name__} is not an iterable.")
        iterable = False
    else:
        print(f"{type(x).__name__} is an iterable.")
        iterable = True
    return iterable

lower = 5       # first element
upper = 21      # last element
length = 13     # number of elements
ev_array = np.linspace(lower, upper, length)

print(f"This is your evenly spaced elements: \n{ev_array}\n")

if __name__ == "__main__":
        
    ev_list_iter = iterable_or_not(ev_list)
    ev_array_iter = iterable_or_not(ev_array)
    
    print("\nComment: The list is an original python class, and is more versatile \
than the ndarray class. Versatility comes with a cost (see e.g., Wolpert, D.H.,\
Macready, W.G. (1997), 'No Free Lunch Theorems for Optimization', IEEE Transactions \
on Evolutionary Computation 1, 67), and in this case the versatility of the list \
is that it can contain all kinds of elements, whereas the numpy array only accepts \
numbers. The array can then space the elements without throwing exceptions here \
and there, but the list cannot - because what is the space between 'red' and \
'blue'? In summary, a class is more effective the less versatile it is - always \
use numpy (number python) if you are working with numbers. ")
    
    

