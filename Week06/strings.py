#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:01:51 2021

@author: kam025
"""

s = "This is a string"

print(s[0])
print(s[2])

print(s[:4])

for elem in s:
    print(elem, end = " ") # mellomrom mellom hver bokstav istedetfor newline
    
print("\nSplit:")
    
print(s.split())


s = "This,is,a,string"

print(s.split(","))

print(s.split(",", maxsplit = 2))


s = "This is a string"

ssplit = s.split()

print("\nJoin:")

s = "-".join(ssplit)

print(f"{s} \n")

s = "There are some who call me ... Tim"

s = s.replace("Tim", "The Black Knight") #replace all
s = s.replace("The", "The Black Knight", 2) # replace first 2

print(s)

print("are" in s)
print("Tim" in s)

print("here" in s)
print("tim" in s)
print(type(s))

s = s.split()

print(s)
print(type(s))
print("here" in s)














