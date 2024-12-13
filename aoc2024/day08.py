#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 01:03:35 2024

@author: jiechi
"""

from collections import defaultdict
f_in  = open('inputs/day08.txt').readlines()

p1 = set()
p2 = set()
maps = defaultdict(list)
for x,line in enumerate(f_in):
    for y,c in enumerate(line.strip()):
        if c != '.':
            maps[c].append((x,y))
            
def find (v1, v2, p1 = True, d1 = True, d2 = True):
    x1,y1 = v1
    x2,y2 = v2
    res = set()
    if d1 and 0 <= x1 - (x2 - x1) < X and 0 <= y1 - (y2 - y1) < Y:
        res.add((x1 - (x2 - x1) ,  y1 - (y2 - y1)))
        if not p1:
            res= res | find( (x1 - (x2 - x1) ,  y1 - (y2 - y1)), (x1,y1), False, True, False)
        
    if d2 and 0 <= x2 - (x1 - x2) < X and 0 <= y2 - (y1 - y2) < Y:
        res.add((x2 - (x1 - x2) ,  y2 - (y1 - y2)))
        if not p1:
            res= res | find((x2,y2), (x2 - (x1 - x2) ,  y2 - (y1 - y2)), False,  False, True)

    return res

X = len(f_in)
Y = len(f_in[0].strip())
for k,v in maps.items():
    for i1 in range(len(v) - 1):
        for i2 in range(i1+1, len(v)):
            p1 = p1|find(v[i1], v[i2], True)
            p2 = p2|find(v[i1], v[i2], False, True, True)
            p2.add(v[i1])
            p2.add(v[i2])
            
print(len(p1))
print(len(p2))