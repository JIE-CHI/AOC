#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:24:56 2021

@author: jiechi
"""

f = open('inputs/day7.txt', 'r')
data = list(map(int, f.read().split(','))) 
# test = [16,1,2,0,4,2,7,1,2,14]
# data = test
data = dict((i, data.count(i)) for i in data)



def accum(num):
    
    return (1 + num) * num // 2

def part1_solve(data):
    minim_value  = float('inf')
    for i in range(1, max(data)+1):
        dis = 0
        for k in data:
            dis += data[k]  * abs(k - i)
        if dis < minim_value:
            minim_value = dis
            minim_point = i
    return(minim_value)

def part2_solve(data):
    minim_value  = float('inf')
    for i in range(1, max(data)+1):
        dis = 0
        for k in data:
            dis += data[k]  * accum(abs(k - i))
        if dis < minim_value:
            minim_value = dis
            minim_point = i
    return(minim_value)

print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))
