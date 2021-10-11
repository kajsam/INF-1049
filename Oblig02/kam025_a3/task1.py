#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:05:30 2021

@author: kam025
"""

# Task 1

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

print(f"\n(a)")

sentence = '' # creating an empty string

# defining four string variables
A = 'Luke,'
B = ' I'
C = ' am'
D = ' your father.'

sentence = sentence + A + B + C + D # concatenating them to a sentence

print(sentence)

# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

print(f"\n(b)")

# splitting the sentence at spaces (default), returns a list
lst_sent = sentence.split()

print(lst_sent)

# cccccccccccccccccccccccccccccccccccccccccccccccccccc

print(f"\n(c)")

# remove a specific string from a list of strings
strp_sentence = sentence.strip('Luke')

print(strp_sentence)

# dddddddddddddddddddddddddddddddddddddddddddddddddddd

print(f"\n(d)")

# Index '0' is the first letter in the sentence

print(sentence[0])

# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

print(f"\n(e)")

# The five last letters (I'd say '.' is a letter in this context), sliced from 
# place -5 and to the end

print(sentence[-5:])

# ffffffffffffffffffffffffffffffffffffffffffffffffffff

print(f"\n(f)")

# Counts how often a substring appears

num_your = sentence.count('your')

print(num_your)

# ggggggggggggggggggggggggggggggggggggggggggggggggggggg

print("\n(g)")

# Slices out Luke as the first four letters

luke = sentence[0:4]

# Reverses the order

ekul = luke[::-1]

print(ekul)

# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

print(f"\n(h)")

line = ['Kari', 'Lars', 'Ada'] # define a list

names = ',' # empty string
names = names.join(line) # put list into string
print(names)

# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

print(f"\n(i)")

# replace 'X' with 'Y'

names = names.replace('Ada', 'Santa')

print(names)

