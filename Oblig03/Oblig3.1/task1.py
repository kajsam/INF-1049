#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 08:59:39 2021

@author: kam025
"""

# Task 1

# The class Cube is defined with the mandatory __init__ function, and three
# methods. Each method returns a float according to well-known equations. 

class Cube:
    def __init__(self, x, y, z, rho=997):
        """Initialisation of a cube object. 
        x, y, z are the lenghts of the sides.
        rho is the density (default: water)
        """
        
        # stores the four input parameters in 'self'
        self.x, self.y, self.z, self.rho = x, y, z, rho
        
    def volume(self):
        """Returns the volume of a cube object."""       
        return self.x*self.y*self.z
    
    def area(self):
        """Returns the surface area of cube object."""        
        return 2*(self.x*self.y + self.x*self.z + self.y*self.z)
    
    def mass(self):
        """Returns the mass of cube object."""      
        # when calling a function within the class: use self.
        V = self.volume()        
        return V*self.rho
    
if __name__ == "__main__":
    
    # a ------------------------------------------------------------------ a -   
    print('\na)')
    
    # making an instanse with specific measures. rho is a keyword argument.
    x = 2
    y = 0.5
    z = 0.5
    cubeA = Cube(x, y, z, rho=1.9)
    
    # the instance has now inherited all the functions of the class, and the 
    # functions can be called directly.
    print(f"Volume: {cubeA.volume()}")
    print(f"Area: {cubeA.area()}")
    print(f"Mass: {cubeA.mass()}")      
    
    # b ------------------------------------------------------------------ b -
    print('\nb)')
    
    # an instance made without specifying the density will be a water cube
    cubeB = Cube(x,y,z)
    
    print(f"Mass: {cubeB.mass()}.")
    print(f"The mass of the water cube is {cubeB.mass()-cubeA.mass()} kg \
heavier than the silica aerogel cube.")
    
    