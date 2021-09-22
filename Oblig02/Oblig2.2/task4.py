#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:42:48 2021

@author: kam025
"""

import numpy as np # for everything numbers
import matplotlib.pyplot as plt # for the plotting

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# loads file, specifying delimiter and skipping first 4 rows

data = np.loadtxt("glob_temp_anom_1.csv", delimiter = ",", skiprows = 4)

# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

# plots data[:,0] on x-axis, data[:,1] on y-axis, and gives a label to the plot
plt.plot(data[:,0], data[:,1], label = "anomalies")
plt.xlabel("Year")              # labels x axis
plt.ylabel("Temperature")       # labels y axis
    
plt.legend()                    # prints lables
plt.grid()                      # adds grid
plt.show()                      # displays plot

# ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

# repeating the same for 'glob_temp_anom_2'
# only difference is that temperature is in 2nd row

data2 = np.loadtxt("glob_temp_anom_2.csv", delimiter = ",", skiprows = 4)

time = data2[:,0]+data2[:,1]/12 # adding month to year

plt.plot(time, data2[:,2], label = "anomalies2")
plt.xlabel("Year")   
plt.ylabel("Temperature")
    
plt.legend()
plt.grid()
plt.show()

# ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

# plotting both curves in same plot

plt.plot(data[:,0], data[:,1], label = "anomalies")
plt.plot(time, data2[:,2], label = "anomalies2")
plt.xlabel("Year")   
plt.ylabel("Temperature")
    
plt.legend()
plt.grid()
plt.show()

print("Comment: The vertical lines are repeated measurements within the same \
year/month.")
