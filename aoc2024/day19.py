#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:06:54 2025

@author: jiechi
"""
from collections import defaultdict
f_in = open('inputs/day19.txt').read()

patterns, designs = f_in.split("\n\n")
patterns = patterns.split(', ')
designs = designs.strip().split("\n")

max_len = 0
for i in patterns:
    max_len = max(max_len, len(i))

mem = {}
def check(design):
    if design == '': return 1
    if design in mem:
        return mem[design]
    tot = 0
    for i in range(min(max_len, len(design))+ 1):
        if design[0:i] in patterns:
            tot += check(design[i:])
    mem[design] = tot
    return tot
p1 = p2 = 0 
for d in designs:
    p = check(d)
    if p >0: p1 += 1
    p2 += p
print(p1)
print(p2)