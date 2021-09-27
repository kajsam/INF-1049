#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:37:22 2021

@author: kam025
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

# Task 2

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

def load_to_dict(filename):
    
    data = []
    dic_data = {}
    
    with open(filename, 'r') as fp:
        reader = csv.reader(fp, delimiter = ",")
        
        for line in reader:
            data.append(line) # list of lists
            
            dic_data[line[0]] = np.array(line[1:]).astype(int)
            
        dic_data['Time'] = dic_data['country'] # add Time (at the end)
        del dic_data['country'] # delete 'country'
        
    return dic_data

# cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

def mean_income(dictionary):
    
    del dictionary['Time'] # delete 'Time'
    
    for key, value in dictionary.items():
        # do something with value
        dictionary[key] = np.mean(dictionary[key])
        
    print(dictionary)
    
    return dictionary
        
# ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        
def rank_income(dictionary):
    
    print(type(dictionary))
    
    mean_income = []
    for key in dictionary:
        mean_income.append(dictionary[key])
        
    idx_income = np.argsort(mean_income)
    
    print(type(idx_income[0]))
    
    
    #ranked_mean = {k: dictionary[k] for k in idx_income}
        
    
    #print(ranked_mean)
    
        

if __name__ == "__main__":
    
    dictionary = load_to_dict("income_per_person.csv")
    print(dictionary.keys())
    print(type(dictionary['Afghanistan']))
    
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

    plt.plot(dictionary['Time'],dictionary['Oman'], label = "Oman")
    plt.plot(dictionary['Time'],dictionary['Vanuatu'], label = "Vanuatu")
    
    plt.legend()
    plt.show()
    
# ccccccccccccccccccccccccccccccc

    mean_dic = mean_income(dictionary)
    
# ddddddddddddddddddddddddddddddddddddddddd

    rank_dic = rank_income(mean_dic)
    

    