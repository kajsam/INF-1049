#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:19:54 2021

@author: kam025
"""

# Task 3

# Comment: I am starting to wonder whether this is a vector - I am struggeling 
# making sense of the element-wise multiplication. Prolly this is not a vector
# in the common algebra sense, but in some informatic non-mathematical sense.
# We could take it as a point in R^3, and the element-wise multiplication is 
# then a transformation. If we instead take the Vector3D objects to be matrices, 
# then the element-wise multiplication is the Hadamard product. But they cannot 
# be matrices or points, because of the dot and cross products. They are some 
# kind of shape-shifters, which is perhaps what duck programming is all about. 

# A note on notation: Informatics-speak and mathematical notation overlap alot, 
# but of course, not with the same definitions for the same words. It's a bit 
# confusing for me, and perhaps for whoever reads this. 

from math import sqrt # to calculate the length of a vector


# Making a class whose instances are either points in a 3 dimensional real 
# space (R^3), or real matrices of size (3x1) or vectors in R^3. 

class Vector3D:
    def __init__(self, x, y, z):
        """Initialisation of a 3D vector class. 
        Input: x, y, z : 
                         - coordinates for point in R^3 or
                         - vector or
                         - elements of (3x1) matrix"""
        # 'self' is the function calling on itself, and then the inputs are
        # attributed to the self
        self.x = x 
        self.y = y
        self.z = z
            
    # For these special functions, whenever we have two objects of the same
    # class, e.g. 'v1' and 'v2' of class Vector3D, and an operation, e.g. '+', 
    # python will go looking for the '__add__' method in the class definition. 
    # Each special function takes the argument 'self'. Some of them also takes 
    # the input 'other' - this is for binary operations (an operation that takes 
    # two elements) like '+'. Some special functions only take 'self' as 
    # argument and only operates on one element.   
    
    # If the special function is a binary operator, it returns an instance of 
    # the vector3D class. E.g., v3 = v1 + v2, then v3 is a vector3D instance.
    # If the Vector3D class is not specified in the return, python recognizes 
    # e.g. a float or boolean and returns an object of that class. 
    
    # The three methods length(), dot() and cross() are not special functions. 
    # They are defined for every instance, and can be called as an attribute. 
    
    def __add__(self, other):
        """Element-wise addition for two instances of class Vector3D"""
        return Vector3D(self.x + other.x, self.y + other.y,  self.z + other.z)
    
    def __sub__(self, other):
        """Element-wise subtraction for two instances of class Vector3D"""
        return Vector3D(self.x - other.x, self.y - other.y,  self.z - other.z)
    
    def __mul__(self, other):
        """Element-wise multiplication for two instances of class Vector3D"""
        return Vector3D(self.x*other.x, self.y*other.y,  self.z*other.z)
    
    def __eq__(self, other):
        """Checks for elementwise equality. Returns true or false."""
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        """Returns the vector/matrix as a string."""
        return '[' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ']'
    
    def __repr__(self):
        """Returns the vector/matrix as a string, but with the class."""
        return 'Vector3D(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'  
    
    def length(self):
        """Returns the length of the vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot(self, other):
        """Returns the dot product."""
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        """Returns the cross product of two vectors."""
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        
        return Vector3D(x, y, z)
    
if __name__ == "__main__":
    
    # Here I've tested different varieties of the special functions and methods.
    
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(2, 3, 4)    
    
    veq = v1 == v2
    # print(type(veq)) # this is boolean
   