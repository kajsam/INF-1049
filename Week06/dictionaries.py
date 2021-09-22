#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:37:49 2021

@author: kam025
"""

d = {"Store Lakselvtind": 1616, "Lille Blaamann" : 844, "Buren" :765}

print(d)

print(d["Buren"])

print("Buren" in d)

d["Storstolpan"] = 977

print(d)

# key er unik og verdien overskrives

del d["Buren"]

print(d)

d.pop("Lille Blaamann")

print(d)

mountains = {"Store Lakselvtind": 1616, "Lille Blaamann" : 844, "Buren" :765}
mountains["Storstolpan"] = 977

print(mountains.keys())
print(mountains.values())
print(mountains.items())

for k in mountains: # keys as default
    print(k)
    
for value in mountains.values():
    print(f"{value}")
    
for key, value in mountains.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
    
# can map to more complex stuff, e.g. dictionaries

mountains={"Store Lakselvtinden": {"height":1616,"ATES":3,"max_steepness":50},
           "Lille Blåmannen":     {"height":844,"ATES":1,"max_steepness":27},
           "Buren":{"height":802,"ATES":2,"max_steepness":35},
           "Storstolpan": {"height":977,"ATES":2,"max_steepness":35}}

print(mountains)

for mountain, data in mountains.items():
    print(f"Mountain: {mountain}")
    print(data)
    
for mountain, data in mountains.items():
    print(f"Mountain: {mountain}")
    
    for attr, value in data.items():
        print(f"{attr}: {value}")
    print()
    
    















