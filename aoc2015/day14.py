#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:32:25 2022

@author: jiechi
"""

file_in = open('inputs/day14.txt').readlines()
deers = {}
for i in file_in:
    words = i.split()
    deers[words[0]] = (int(words[3]), int(words[6]), int(words[-2]))
seconds = 2503
def cal(deers, seconds):
    fast = ('', 0)
    for k,v in deers.items():
        dist = seconds // (v[1] + v[2]) * v[0] * v[1]
        if seconds % (v[1] + v[2]) <= v[1]:
            dist += v[0] *  (seconds % (v[1] + v[2]))
        else:
            dist += v[0] * v[1]
        if fast[1] < dist:
            fast = (k, dist)
    return fast
print(cal(deers,seconds)[1])
scores = {i:0 for i in deers}  
for i in range(1, seconds+1):
    scores[cal(deers, i)[0]] += 1
print(max(scores.values()))
    
    
    
    