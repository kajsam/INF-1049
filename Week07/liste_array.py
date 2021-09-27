#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:39:32 2021

@author: kam025
"""

import numpy as np

vec1 = [1, 2]
vec2 = [4, 3]

vec1 = np.array(vec1)
vec2 = np.array(vec2)

print(vec1 * vec2)

dor = np.dot(vec1, vec2)

print(f"dot {dor}")

