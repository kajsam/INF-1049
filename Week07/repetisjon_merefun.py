#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:11:39 2021

@author: kam025
"""

def hei(navn):
    print(f"hei {navn}")
    
def fem():
    return 5

def summer(x, y):
    s = x + y
    d = x - y
    return s, d
    
if __name__ == "__main__":
    navn = "Kajsa"
    
    print(navn)
    svar = hei(navn)
    
    print(svar)
    
    tall = fem()
    print(tall)
    
    sm, df = summer(3,4)
    print(sm)
    print(df)
    
    