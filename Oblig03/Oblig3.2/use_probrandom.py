#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:32:28 2021

@author: kam025
"""

# Task 1 ---------------------------------------------------------------- d --

# This program uses the ProbRandom class to create two Python lists of integers,
# randomP and probRandomP, reflecting the number of times each element in the 
# data list is picked at random

from probrandom import ProbRandom # importing the class
import matplotlib.pyplot as plt # for the plotting 
import numpy as np # to go from count to proportion

if __name__ == "__main__":
    
    # Input data list and probability
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    P = [0.025, 0.05, 0.075, 0.125, 0.225, 0.225, 0.125, 0.075, 0.05, 0.025]

    n = 1000 # number of repetitions

    objA = ProbRandom(X, P) # creating the object once
    
    # calling the function n times
    random_list = [objA.random_data() for _ in range(n)]
    
    # creating a list of the desired length (at least in matlab, it is much
    # faster than expanding and object in a for loop)
    randomP = [None] * len(X)
    
    # counting how many of each element 
    for i in range(len(X)):
        randomP[i] = random_list.count(X[i])
    # and we have the list     
    
    # calling the function n times
    prob_random_list = [objA.prob_random_data() for _ in range(n)]
    
    probRandomP = [None] * len(X) # pre-assigning space

    for i in range(len(P)):
        probRandomP[i] = prob_random_list.count(X[i]) # counting
    # and we have the list     

    # ------------------------------------------------------------------- e --
    prop = np.array(probRandomP)/n # from counts to proportions
    
    # just plotting, nothing new here
    plt.plot(X, P, label = "input probabilites") # plotting
    plt.plot(X, prop, label = f"observed proportions, n = {n}") # plotting
    plt.xlabel("x values")    # labels
    plt.ylabel(f"Probability/Proportion")
    
    # print legends and grid, and show the plot
    plt.legend() 
    plt.grid()
    plt.show()
