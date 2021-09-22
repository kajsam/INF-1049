#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:47:55 2021

@author: kam025
"""

# Task 1

import numpy as np # importing numpy and naming it 'np' (by convention)

print("\n(a)") # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

v = [1, 2, 3, 4, 5] # this is a list with five elements

v5 = v*5 # multiplied with the scalar 5

print(f"List: {v5}") # the list is printed five times

print("\n(b)") # bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

v = np.array(v) # converting the list to an array

v5 = v*5 # multiplying each element with the scalar 5

print(f"Array: {v5}") # each element is 5 times as big

print("\n(c)") # ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

# 1 Taking the cosine of each element 

cosv = np.cos(v)                    # treats input as radians

with np.printoptions(precision=3):  # avoiding all those decimals in the print

    print(f"1. Cosine: {cosv}") 

# 2 Multiplication of two vectors

w = np.array([5, 1, 0, 1, 4]) # converting list to array

vw = v*w # element-wise multiplication

print(f"2. Multiplication: {vw}")

# 3 Addition

vplusw = v+w # element-wise addition
print(f"3. Addition: {vplusw}")

# 4 Boolean indexing

idx = w > 1 # values greater than 1 are TRUE

print(f"4. Values > 1: {w[idx]}")

# 5 Make vector

g = np.exp(w) # element-wise exponent

print(f"5. Exponent: {g}") 

# 6 Shape

shape = np.shape(g) # finds the shape of an array

print(f"6. Shape: {shape}")

print("\n(d)") # ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

matrix = np.array([[5, 1, 5], [1, 2, 3], [9, 2, 1], [10, 17, 4]])

print(f"Shape: {np.shape(matrix)}")

print(f"First column: {matrix[:,0]}") 

print("\n(e)") # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

idx = matrix > 4 # find values larger than 4

matrix[idx] = 0 # replace with 0

print(f"New matrix: \n{matrix}")

print("\n(f) and (g)") # fffffffffffffffffffff ggggggggggggggggggggggggggggggg

idx = matrix > 1 # find values larger than 1

matrix[idx] = 3 # replace with 3

matrix = np.reshape(matrix, (2,6)) # reshaping

print(f"Reshaped: \n{matrix}")



