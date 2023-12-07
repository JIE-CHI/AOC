#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:18:02 2021

@author: jiechi
"""
import numpy as np

f = open('./inputs/day6.txt', 'r')
data = list(map(int, f.read().split(',')))

# test = [3,4,3,1,2]
# data = test


data = np.asarray(data, dtype = int)

#naive method, store all the values at every timestep
def part1_solve(data, total_days):
    for i in range(total_days):
        new = np.count_nonzero(data == 0)
        data[np.where(data == 0)] = 7
        data = data - 1
        data = np.append(data, [8] * new)
    return len(data)


#part2 code can also be used for part1, 
#instead of having a very long list of values, 
#calculate the number of new ones each lantern fish at the initial state can have directly 
def part2_solve(data, total_days):
    calculated = {}
    count = len(data)
    for k in data:
        if not (k, 0) in calculated:
            calculated = calcu(k, 0, total_days, calculated)
        count += calculated[(k,0)]
    return count

def calcu (initial_sta, initial_day, total_days, calculated):
    if initial_sta >= total_days - initial_day:
        calculated.update({(initial_sta, initial_day): 0})
    else:
        new = (total_days - initial_day - initial_sta - 1) // 7 + 1 
        count = 0
        for i in range(new):
            if not (8, initial_day + initial_sta + 1 + i * 7) in calculated:
                calculated = calcu(8, initial_day + initial_sta + 1 + i * 7 , total_days, calculated)
            count += calculated[ (8, initial_day + initial_sta + 1 + i * 7)]
        calculated.update({(initial_sta, initial_day): count + new })
    return calculated



print("*************result for part 1*************")
print(part1_solve(data, 80))
print("*************result for part 2*************")
print(part2_solve(data, 256))

