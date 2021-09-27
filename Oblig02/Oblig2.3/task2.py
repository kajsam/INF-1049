#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:37:22 2021

@author: kam025
"""

import csv
import matplotlib.pyplot as plt

# Task 2

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

def load_to_dict(filename):
    
    data = []
    dic_data = {}
    
    with open(filename, 'r') as fp:
        reader = csv.reader(fp, delimiter = ",")
        
        
    
        for line in reader:
            data.append(line) # list of lists
            
            dic_data[line[0]] = line[1:]
            
        dic_data['Time'] = dic_data['country'] # add Time (at the end)
        del dic_data['country'] # delete 'country'
        
    return dic_data
        

if __name__ == "__main__":
    
    dictionary = load_to_dict("income_per_person.csv")
    
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

    