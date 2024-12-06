#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:02:53 2024

@author: jiechi
"""

from collections import Counter

f_in = open('inputs/day01.txt').readlines() 
lefts = []
rights = []

for line in f_in:
    lefts.append(int(line.split()[0]))
    rights.append(int(line.split()[1]))


lefts.sort()
rights.sort()
                
p1 = 0
for (l,r) in zip(lefts, rights):
    p1 += abs(l-r)
print(p1)

p2 = 0
counts = Counter(rights)
for i in lefts:
    p2 += i*counts[i]
print(p2)

  
        
        