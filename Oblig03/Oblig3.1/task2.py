#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:45:38 2021

@author: kam025
"""

# Task 2

from math import sin, cos, pi
import matplotlib.pyplot as plt # for the plotting
import numpy as np

class Third_Derivative:
    def __init__(self, f, h = 1E-5):
        """Initialisation of a third derivative object. 
        f is the function
        h is an arbitrarily small number
        """
        self.f = f
        self.h = float(h)
        
    def __call__(self, x):
        """Calculates the third derivative in the point x."""
        
        f = self.f # just looks nicer
        h = self.h
        
        return (-(1/2)*f(x-2*h) + f(x-h) - f(x+h) + (1/2)*f(x+2*h))/h**3


if __name__ == "__main__":
    
    cos_3der = Third_Derivative(cos, h = 1E-03)
    
    x = 0.5*pi
    print(f"Third derivative of cosine in x = {x} is {cos_3der(x)}")
    
    print(f"It is actually {sin(x)}")
    
    xvec = np.linspace(-2*pi, 2*pi, 1000) # the array
    
    vfunc = np.vectorize(cos_3der) # vectorizing (that's lazy)
    
    cos_3dervec = vfunc(xvec)
    
    vsin = np.vectorize(sin)
    
    sin_vec = vsin(xvec)
        
    
    plt.plot(xvec, cos_3dervec, label = "approx")
    plt.plot(xvec, sin_vec, label = "exact")
    plt.xlabel("x")   
    plt.ylabel("Cosine'''(x)")
    
    plt.legend()
    plt.grid()
    plt.show()
    
    