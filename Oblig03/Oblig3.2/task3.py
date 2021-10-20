#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:49:56 2021

@author: kam025
"""

# Task 3

import numpy as np
import random    
    
class Games:
    def __init__(self, players, cash):
        """Initialisation of the GAmes class. 
        Input: players   - list of names 
               cash - and their corresponding amount of cash 
        """
        
        # 'self' is the function calling on itself, and then the inputs are
        # attributed to the self
        self.players = players
        self.cash = cash
        
        # Checking if the two lists have the same length
        if len(self.players)!=len(self.cash):
            print(f"There are {len(players)} players, but {len(cash)} accounts.\
They must be as many accounts as playsers.")
            return
    
    def make_dictionary(self):
        """Returns a dictionary from the two inputs of the class."""
        
        dic_data = {} # empty dictionary
        
        # create the dictionary
        for i in range(len(self.players)): 
            dic_data[self.players[i]] = int(self.cash[i])
            
        return dic_data
    
    def dice(self, guess, win, loose):
        """Throwing a dice and adjusting the players' accounts accordingly.
        Input:  guess - players' guesses
                win - amount you gain if you win
                loose - price to pay if you loose"""
                
        # throw a dice
        throw = random.randint(1, 6)
        
        # make a boolean indicating who guessed correctly
        a = np.array(guess)== throw
        
        # an array of zeros
        add = np.zeros((len(self.cash), 1))
        add[a] = win # gain for the winner
        add[np.invert(a)] = loose # loss for the loosers
        
        # update the cash list
        self.cash = self.cash + np.transpose(add[0,:])
        
        # get the dictionary
        dic_data = Games.make_dictionary(self)
        
        # update the dictionary
        for i in range(len(self.players)):
            dic_data[self.players[i]] = int(self.cash[i])
            
        return dic_data
    
    def lottery(self, price):
        """One of the players will win the price (input). Returns an updated
        dictionary."""
        
        # pick one of the playsers at random
        pick = random.randint(0, len(self.players)-1)
        
        # get the dictionary
        dic_data = Games.make_dictionary(self)
        
        # update the players' wallet content
        self.cash[pick] = self.cash[pick] + price
        
        # update the dictionary
        dic_data = Games.make_dictionary(self)
        
        # and return it
        return dic_data
                  
if __name__ == "__main__":
    
    players = ['Iris', 'Katja', 'Olena', 'Karina', 'Marko']
    cash = [105, 467, 543, 765, 363]
    
    gameA = Games(players, cash)
    
    print(gameA.make_dictionary())
    
    print(gameA.dice([4, 3, 6, 4, 4], 100, -25))
    
    price = 250
    print(gameA.lottery(price))
            
            
        