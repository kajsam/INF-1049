#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:45:38 2021

@author: kam025
"""

# Task 2

from math import sin, cos, pi # sinus, cosinus functions and pi
import matplotlib.pyplot as plt # for the plotting
import numpy as np # for the linspace-array used in the plotting


# The class Third_Derivative is defined. It's only purpose is to do numeric 
# approximations of third derivatives, using the Taylor expansion. We can then 
# use the special function __call__, and the instance is also a function. The 
# error of the Taylor expansion is of order h^2. Note that the the h^3 in the 
# nominator makes it non-robust to small h for f'''(x) far from 0, and that is 
# perhaps more important than the error term. 

class Third_Derivative:
    def __init__(self, f, h = 1E-5):
        """Initialisation of a third derivative object. 
        f is the function
        h is an arbitrarily small number
        """
        self.f = f
        self.h = float(h) # making sure h is a float for precision
        
    def __call__(self, x):
        """Approximates the third derivative in the point x."""
        
        f = self.f # just looks nicer
        h = self.h      
        return (-(1/2)*f(x-2*h) + f(x-h) - f(x+h) + (1/2)*f(x+2*h))/h**3
    
        
def plot_fun3der(fun_3der, exact_fun, start = -2*pi, stop=2*pi, steps = 1000):
    """This is a plot function for the third derivative.
    Arguments:  cos_3der - instance of class Third_Derivative
                exact_fun - the exact function
                start - plot starts
                stop - plot ends
                steps - number of points in the plot line"""
      
    # Checking if the third derivative is of correct class            
    if not isinstance(cos_3der, Third_Derivative):
        print("Your function is not of the 'Third_Derivative class. \n\
Make your own plot function!")
        return # exiting the function
                
    xvec = np.linspace(start, stop, steps) # the x-axis in plot
    vfunc = np.vectorize(cos_3der) # vectorizing (that's lazy)
    cos_3dervec = vfunc(xvec) # the numeric approx
    vsin = np.vectorize(exact_fun) # vectorizing the exact function
    sin_vec = vsin(xvec) # the true value    
    
    plt.plot(xvec, cos_3dervec, label = "approx") # plotting
    plt.plot(xvec, sin_vec, label = str(sin)) # plotting
    plt.xlabel("x")    # labels
    plt.ylabel(f"Cosine'''(x): h = {cos_3der.h}")
    
    # print legends and grid, and show the plot
    plt.legend() 
    plt.grid()
    plt.show()


if __name__ == "__main__":
    
    cos_3der = Third_Derivative(cos) # making an instance 
       
    x = 0.5*pi # choosing a point cos(x) far from 0 to check
    
    print(f"Third derivative of cosine in x = {x} is {cos_3der(x)}, approximated \
with {cos_3der.h}")    
    print(f"It is actually {sin(x)}")
    
    plot_fun3der(cos_3der, sin) # plotting the two functions
    
    # Let's see what happens with larger h:
    
    cos_3der = Third_Derivative(cos, h = 1E-3)
    
    print(f"Third derivative of cosine in x = {x} is {cos_3der(x)}, approximated \
with {cos_3der.h}")    
    print(f"It is actually {sin(x)}")
    
    plot_fun3der(cos_3der, sin)
    
    
    
    
    