#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:58:12 2021

@author: kam025
"""

def read_data(filename):
    
    mountains = {} # tom dictionary
    
    with open(filename, 'r', encoding = "utf8") as fp:
        keys = fp.readline() # leser foerste linje
        keys = keys.split()
        print(keys)
        
        for line in fp.readlines(): # separert paa linjeskift linez
            data = line.split()
            mountain_data = {}
            for key, value in zip(keys[1:], data[1:]):
                mountain_data[key] = value
            mountains[data[0]] = mountain_data
            
    for key, value in mountains.items():
        print(f"{key=} {value=}")
        
            
    
if __name__ == "__main__":
    
    read_data("fjell.csv")
    