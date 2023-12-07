#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:30:51 2022

@author: jiechi
"""

text = open('inputs/day10.txt').readlines()


cycles = [20 + i * 40 for i in range(6)]
cycle_one = [i - 1 for i in cycles]
tot = 0
cycle = 1
x = 1
pixel = ''
for line in text:
    pos = (cycle-1) % 40 
    if pos in [x-1, x, x+1]:
        pixel += '#'
    else:
        pixel += '.'
    if cycle in cycles:
        tot += x * cycle
    if line.startswith('noop'):
        cycle += 1     
    else:
        if cycle in cycle_one:
            tot += x * (cycle + 1)     
        pos = (cycle) % 40 
        if pos in [x-1, x, x+1]:
            pixel += '#'
        else:
            pixel += '.'       
        value = int(line.split()[1])
        x += value
        cycle += 2
print(tot)
for i in range(len(pixel)//40):
    print(pixel[i*40:40*(i+1)])
    
        