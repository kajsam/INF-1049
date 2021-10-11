#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:34:48 2021

@author: kam025
"""

import numpy as np

def y(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2

class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
        
    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
    
def make_table(f, tstop, n):
    for t in np.linspace(0, tstop, n):
        print(t, f(t))
        
def g(t):
    return np.sin(t)*np.exp(-t)

class VelocityProfile:
    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = \
            beta, mu0, n, R
            
    def value(self, r):
        beta, mu0, n, R = \
            self.beta, self.mu0, self.n, self.R
        n = float(n) # ensure float division
        v = (beta/2.0*mu0)**(1/n)*(n/(n+1))*\
            (R**(1+1/n) - r**(1+1/n))
        return v
    
class SelfExplorer:
    """Class for computing a*x."""
    def __init__(self, a):
        self.a = a
        print('init: a=%g, id(self)=%d' % (self.a, id(self)))
        
    def value(self, x):
        print('value: a=%g, id(self)=%d' % (self.a, id(self)))
        return self.a*x
    
class Account:
    def __init__(self, name, account_number, initial_amount):
        self._name = name # underscore - skal ikke evalueres/manipuleres paa utsida
        self._no = account_number
        self._balance = initial_amount
        
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
        
    def get_balance(self):
        return self._balance
    
    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self._name, self._no, self._balance)
        print(s)
        
class Circle:
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R
        
    def area(self):
        return np.pi*self.R**2
    
    def circumference(self):
        return 2*np.pi*self.R
        
if __name__ == "__main__":
    
    t = 0.2
    v0 = 3
    pos = y(t,v0)
    
    print(pos)
    
    y = Y(v0=3) # create instance (object)
    pos = y.value(0.2)
    
    print(pos)
    print(y.v0)
    
   #  make_table(g, 2*np.pi, 11)
    
    y = Y(6.5)
    # make_table(y.value, 2*np.pi, 11)
    
    v = VelocityProfile(R = 1, beta = 0.06, mu0 = 0.02, n = 0.1)
    print(v.value(r = 0.1))
    
    v = SelfExplorer(3)
    v.value(4)
    
    SelfExplorer.value(v, 4) # ikke bruk
    
    s1 = SelfExplorer(1)
    id(s1)
    
    a1 = Account('Kajsa', 176, 500)
    a2 = Account('Anders', 342, 350)
    
    print("a1's balance:", a1._balance) # not good
    
    a1.dump()
    
    b1 = a1.get_balance()
    print(b1)
    
    c = Circle(2, -1, 5)
    print(c.area())
    
    print(f"A circle with radius {c.R}.")
    
    