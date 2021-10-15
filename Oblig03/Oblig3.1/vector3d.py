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
# If we instead take the Vector3D objects to be matrices, then the element-wise 
# multiplication is the Hadamard product. But then they cannot be matrices, 
# because of the dot and cross products. They are some kind of shape-shifters. 

from math import sqrt


class Vector3D:
    def __init__(self, x, y, z):
        """Initialisation of a 3D vector class."""
        self.x = x 
        self.y = y
        self.z = z
            
    def __add__(self, other):
        """Vector addition for to instances of class Vector3D"""
  
        return Vector3D(self.x + other.x, self.y + other.y,  self.z + other.z)
    
    def __sub__(self, other):
        """Vector subtraction for to instances of class Vector3D"""
  
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
        """Returns the length of the vector as an attribute."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot(self, other):
        """Returns the dot product as an attribute."""
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        """Returns the cross product of two vectors as an attribute."""
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        
        return Vector3D(x, y, z)
        