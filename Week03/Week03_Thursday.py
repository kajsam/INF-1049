#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:35:15 2021

@author: kam025
"""

from random import uniform

def f(x):
    
    return 2*x - 5

f0 = f(0)

print(f0)
print()

for i in range(0,1):
    print(f(i))
    
def summer(a,b):
    return a + b

print(summer(2,5))
print()

def siHei():
    return "hei"

print(siHei())
print()

def summerOppTil(N):
    s = 0
    for i in range(0,N):
        s = s + 1
    return s

# print(s) # NameError: name 's' is not defined

print(summerOppTil(4))
print()

x_verdier = []
y_verdier = []
    
for i in range(0,10):
    x_verdier.append(i)
    y_verdier.append(f(i))
    
for i in range(len(x_verdier)):
    print(x_verdier[i], y_verdier[i])  
print()

for x, y in zip(x_verdier, y_verdier):
    print(x,y)
print()

if 1 == 2:
    print("oioi")
else:
    print("ja!")
print()

kjoleskap = "Tomt"

if kjoleskap == "Tomt":
    print("Kjop mat!")
elif kjoleskap == "Halvtomt":
    print("Hjelp")
else:
    print("Hjeeeeelp")
print()

alder = -10

if alder > 0 and alder <= 6:
    print("himan")
elif alder > 6:
    print("skul")
else:
    print("old")
print()

a = -5
b = 2
c = 1



def f(a, b, c):
    discr = b**2 - 4*a*c
    
    if discr > 0:
        return 2
    elif discr == 0:
        return 1
    else:
        return 0


print(f(2,-5,2))
print()


def F(t):
    N0 = 100
    vr = 2
    return N0 * vr**t

for t in range(10):
    print("Tid", t, "torsk", F(t))
print()

def F(t):
    
    beste_kvote = 0
    antall_ved_beste = 0
    kvote = 0.0
    step = 0.01
    for i in range(0,100):
        kvote = kvote + step
        N0 = 100
        N = N0
        vr = 2
        S = 1000000   
        uttak = 0
    
        for i in range(t):
            d = uniform(0.0, 0.05)
            uttak = uttak + N*kvote
            N = N + N*vr * (1-N/S) * (1-d) - uttak
        if uttak > antall_ved_beste:
            antall_ved_beste = uttak
            beste_kvote = kvote 
        
    return [beste_kvote, antall_ved_beste]

res = F(100)
print("Beste kvote:", res[0]*100, "%.")
print("Antall fisket:", res[1])
print()

for t in range(30):
    print("Tid", t, "torsk", F(t))
print()





    

    




