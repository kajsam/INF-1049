#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:37:22 2021

@author: kam025
"""

import csv # to read the csv file
import matplotlib.pyplot as plt # to plot
import numpy as np # maths

# Task 2

# a-------------------------aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

def load_to_dict(filename):
    """ Imports data into dictionary.
    Input: filename (string)
    Output: data (dictionary)
    
    The keys are country names, the values are numpy arrays of income estimates,
    except one key, 'Time', which stores an array of years
    
    """
    data = [] # empty list
    dic_data = {} # empty dictionary
    
    with open(filename, 'r') as fp: # open file, define pointer
        reader = csv.reader(fp, delimiter = ",") # read csv file, entries separated by comma
        
        for line in reader: # for each line
            data.append(line) # add the line (a list) to data (a list)
            
            # first entry is the key, the rest of the entries are the values 
            # for that key, converted into integers
            dic_data[line[0]] = np.array(line[1:]).astype(int) 
            
        dic_data['Time'] = dic_data['country'] # add Time (at the end)
        del dic_data['country'] # delete 'country'
        
    return dic_data

# ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc ------ c -

def mean_income(dictionary):
    """ Calculates average income.
    Input: income data (dictionary)
    Output: mean income (dictionary)
    
    Creates a new dictionary with country names  as keys and their average
    income as values.
    """
    
    m_income = dictionary.copy() # copying the input dictionary
    
    del m_income['Time'] # delete 'Time' as it is not relevant
    
    for key, value in m_income.items(): # iterates keys and values
       
        m_income[key] = np.mean(m_income[key]) # replace value
            
    return m_income
        
# dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd - d -
        
def rank_income(dictionary):
    
    """ Rank countries by avarage income.
    Inout: average income (dictionary)
    Output: ranks and countries (dictionary)
    
    The output is not sorted, because it kinda defeats the logic of dictionaries.
    If you want sorted, do list. 
    """
    
    # making a list so that we can sort the mean income
    mean_income = [] # 
    for key in dictionary: # iterates through the dictionary
        mean_income.append(dictionary[key]) # add the value
        
    idx_income = np.argsort(mean_income) # indexing the income (starts at 0)
    
    idx_income = idx_income + 1 # shifts indexes by 1
   
    # making a dictionary where the key is the income rank, and the value is 
    # the country name
    ranked_mean = dict(zip(idx_income,list(dictionary.keys()))) 
    
    return ranked_mean
       
# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

def growth_rate(dictionary, start_year, end_year):
    
    """ Calculates average economic growth.
    Input:  income (dictionary)
            start_year (integer/float)
            end_year (integer/float)
    Output: list of 10 countries with highest growth rate
    
    """
    
    idx_start =  np.where(dictionary['Time'] == start_year)
    idx_end =  np.where(dictionary['Time'] == end_year)
    years = end_year - start_year # number of years
        
    del dictionary['Time'] # delete 'Time'
    
    g_rate = [] # empty list
    
    for key in dictionary: # iterates through dictionary
        # calculates growth rate
        g = (dictionary[key][idx_end]/dictionary[key][idx_start])**(1/years) - 1
        
        g_rate.append(g) # adds it to the list
        
    g_rate = np.array(g_rate) # converts to array
    g_rate = g_rate[:,0]    # flattens
    
    
    ord_g_rate = np.sort(g_rate) # sorted by growth rate
    idx_g_rate = np.argsort(g_rate) # indexed by growth rate
    
    countries = list(dictionary.keys()) # countries as a list
    # reorder list according to growth rate
    ord_countries = [countries[i] for i in list(idx_g_rate)]
    
    g_rate_10 = [] # empty list
    
    for i in range(1,11):
        # add list element - country name and growth rate
        g_rate_10.append([ord_countries[-i], ord_g_rate[-i]])
        
    return g_rate_10
    
# name-equals-main -----------------------------------------------------------
    

if __name__ == "__main__":
    
    # a ------------------------------------------------------------------ a -
    
    print("\n(a)")
    
    dictionary = load_to_dict("income_per_person.csv")
    
    print(f"The output is a {type(dictionary).__name__}.")
    
    prnt = input("Do you want to print the dictionary? (y/n) \n")
    
    if prnt == 'y':
        print(dictionary)
        input("Hit enter to proceed.")
    
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb -------------------- b -

    # Plotting time vs income for Oman and Vanuatu in same plot
    
    print("\n(b)")
    input("Take a look at the plot and hit enter to proceed.")
    
    plt.plot(dictionary['Time'],dictionary['Oman'], label = "Oman")
    plt.plot(dictionary['Time'],dictionary['Vanuatu'], label = "Vanuatu")
    plt.xlabel('Year')
    plt.ylabel('Income')
    
    plt.legend()
    plt.show()
    
# ccccccccccccccccccccccccccccccc ---------------------------------------- c -

    print("\n(c)")

    mean_dic = mean_income(dictionary)
    
    prnt = input("Do you want to print the mean income dictionary? (y/n) \n")
    
    if prnt == 'y':
        print(mean_dic)
        input("Hit enter to proceed.")
    
    
# dddddddddddddddddddddddddddddddddddddddd ------------------------------- d -

    print("\n(d)")
    
    rank_dic = rank_income(mean_dic)
    
    prnt = input("Do you want to print the ranked income dictionary? (y/n) \n")
    
    if prnt == 'y':
        print(rank_dic)
        input("Hit enter to proceed.")
    
# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

    print("\n(e)")
    
    start_year = 2009
    end_year = 2019
    
    rank_rate = growth_rate(dictionary, start_year, end_year)
    
    print(f"The 10 countries with highest growth from {start_year} to {end_year}: {rank_rate}")
    

    