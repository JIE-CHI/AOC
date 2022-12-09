#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:24:05 2022

@author: jiechi
"""

text = open('inputs/day17.txt').readlines()
containers = [int(i.strip() ) for i in text]

combs = []
def subset_sum(numbers, target, partial=[]):
    global combs
    s = sum(partial)
    if s == target: 
        combs.append(partial)
    if s >= target:
        return 
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
subset_sum(containers, 150)
print(len(combs))
mini = 150
tot2 = 0
for i in combs:
    if len(i) > mini:
        pass
    elif mini == len(i) :
        tot2 += 1
    else:
        mini =  len(i)
        tot2 = 1
print(tot2)
        