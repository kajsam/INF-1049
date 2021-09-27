#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:41:50 2021

@author: kam025
"""

def vec_flip(v):
    #v = [-v[0], -v[1]] # overskriver
    v[0] = -v[0] # gaar inn og endrer objektet
    v[1] = -v[1]
    
if __name__ == "__main__":
    vv = [1, 2]
    vec_flip(vv)
    print(vv)
    
    
# som matlab'er er dette litt rart. overskrive/endre ok,
# maa bare huske at indeksering endrer objektet. men at vv blir
# flippa uten retur - det er nesten saa det gjoer vondt.