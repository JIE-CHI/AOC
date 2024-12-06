#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:16:51 2024

@author: jiechi
"""

def check(nums, part1 = True):
    flag = None
    for i in range(len(nums)-1):
        if flag == None:
            flag = (nums[i] > nums[i+1])
        if 1 <= abs(nums[i] - nums[i+1]) <= 3 and (nums[i] > nums[i+1]) == flag:
            pass              
        else:
            if part1:
                return False
            else:
                
                return check(nums[1:], part1=True) | check(nums[:i] + nums[i+1 :], part1=True) | check( nums[:i+1] + nums[i+2 :], part1=True)
    return True


f_in = open('inputs/day02.txt').readlines()
p1 = 0 
for line in f_in:
    if check(list(map(int, line.split())), part1=True):
        p1 += 1
print(p1)

p2 = 0 
res_nums = []
for line in f_in:
    if check(list(map(int, line.split())), part1=False):
        p2+= 1
        res_nums.append(line)
        
print(p2)
    