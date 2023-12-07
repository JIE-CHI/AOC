#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 01:41:44 2022

@author: jiechi
"""

text = open('inputs/day20.txt').read().strip()
num = int(text)

from collections import defaultdict     
house = defaultdict(int)
for i in range(1, num//10):
    for j in range(i, num//10, i):
        house[j] += i*10  
for j in range(1, num//10):
    if house[j] >= num:
        print(j)
        break
house = defaultdict(int)
for i in range(1, num//10):
    for j in range(i, num//10, i):
        if j <= i*50:
            house[j] += i*11   
for j in range(1, num//10):
    if house[j] >= num:
        print(j)
        break
                