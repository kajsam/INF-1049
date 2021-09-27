#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:05:30 2021

@author: kam025
"""

# task 1

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

print(f"\n(a)")

sentence = ''
A = 'Luke,'
B = ' I'
C = ' am'
D = ' your father.'

sentence = sentence + A + B + C + D

print(sentence)

# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

print(f"\n(b)")

lst_sent = sentence.split()

print(lst_sent)

# cccccccccccccccccccccccccccccccccccccccccccccccccccc

print(f"\n(c)")

strp_sentence = sentence.strip('Luke')

print(strp_sentence)

# dddddddddddddddddddddddddddddddddddddddddddddddddddd

print(f"\n(d)")

print(sentence[0])

# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

print(f"\n(e)")

print(sentence[-5:])

# ffffffffffffffffffffffffffffffffffffffffffffffffffff

print(f"\n(f)")

num_your = sentence.count("your")

print(num_your)

# ggggggggggggggggggggggggggggggggggggggggggggggggggggg

print(f"\n(g)")

luke = sentence[0:4]

ekul = luke[::-1]

print(ekul)

# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

print(f"\n(h)")

line = ['Kari', 'Lars', 'Ada']

names = ','
names = names.join(line) 
print(names)

# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

print(f"\n(i)")

names = names.replace('Ada', 'Santa')

print(names)

