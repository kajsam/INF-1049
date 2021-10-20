#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:54:03 2021

@author: kam025
"""

# Lurt tips

print(dir(str))

a = "hello"
print(a.upper())
print(a.capitalize())

print(dir(a))

print(type(a))

# Input function

input_string = 'rt' #input("Type something: ")

print(f"Input = {input_string}")

input_number = '4' # input("Type a number: ")

if input_number.isdigit():
    input_number = int(input_number)
    print(f"Input number: {input_number}")
else:
    print(f"{input_number} is not a number")
    
in_string = '4, 5' # input("Enter inputs separated by comma: ")

numbers = in_string.replace(" ", "").split(",")

print(f"Input is: {numbers=}")

numbers = []

while len(numbers) < 0:
    number = input(f"Enter number {len(numbers)+1}: ")
    
    if not number.isdigit():
        print("Not valid")
        continue
    
    numbers.append(int(number))
    
print(f"Got numbers: {numbers}")

# File input

file_handle = open("artofwar.txt", "r")

print(dir(file_handle))

file_handle.close()

# try except finally

with open("artofwar.txt", "r", encoding="utf8") as file_handle:
    textdata = file_handle.read()
    
# print(textdata)

# Command line arguments

# parser argparse.ArgumentParser



