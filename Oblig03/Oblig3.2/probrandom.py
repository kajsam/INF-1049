#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 07:29:29 2021

@author: kam025
"""

# Task 1

import numpy as np # to access machine epsilon
import random # generating pseudo-random numbers

class ProbRandom:
    # ------------------------------------------------------------------ a ---
    def __init__(self, dataset, prob_list):
        """Initialisation of the ProbRandom class. 
        Input: dataset   - list of numbers
               prob_list - list of probabilities
        """
        
        # 'self' is the function calling on itself, and then the inputs are
        # attributed to the self
        self.dataset = dataset
        self.prob_list = prob_list
               
        # Checking if the two lists have the same length
        if len(self.dataset)!=len(self.prob_list):
            print(f"Length of dataset is {len(dataset)}, but length of probability \
list is {len(prob_list)}. They must be equal.")
            return
        
        # Checking if the sum of probabilites is 1.0 (within machine epsilon)
        if abs(sum(self.prob_list)-1) > np.finfo(float).eps: # machine epsilon
            print(f"The sum of probabilites must be 1.0, but it is {sum(P)}.")
            return
        
    # ------------------------------------------------------------------- b --    
    def random_data(self):
        """Picks one random element from the dataset with equal probability, \
and returns it. 
        """
        
        return random.choice(self.dataset)
    
    # ------------------------------------------------------------------- c --
    def prob_random_data(self):
        """Picks one random element from the dataset with assigned probability \
and returns it.
        """
        
        list_of_one = random.choices(self.dataset, self.prob_list)
        
        # the output from the choices function is now a list. return only the
        # element, not the list itself
        
        return list_of_one[0]

    
if __name__ == "__main__":
    
    # down here, I'm just creating an object of the class and calling its
    # functions to see that everything works
    
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    P = [0.025, 0.05, 0.075, 0.125, 0.225, 0.225, 0.125, 0.075, 0.05, 0.025]
    
    probA = ProbRandom(X,P)
    
    ProbRandom(X,P).random_data()
    ProbRandom(X,P).prob_random_data()