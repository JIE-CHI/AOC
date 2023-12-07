#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:32:08 2021

@author: jiechi
"""

f = open("inputs/day1.txt",'r') 
data = f.read()

def part1_solve (data):
    floor = 0
    for i in data:
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
    return floor

def part2_solve(data):
    floor = 0
    for k,i in enumerate(data):
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
        if floor == -1:
            return k

print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))
