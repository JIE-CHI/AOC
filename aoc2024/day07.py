#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:04:33 2024

@author: jiechi
"""

f_in = open('inputs/day07.txt').readlines()

p1 = 0 
p2 = 0

def check(left, nums, p1=True):
    if len(nums) == 1:
        return left == nums[0]
    if len(nums) == 2:
        if not p1 and left == int(str(nums[0]) + str(nums[1])):
            return True
        return left == (nums[0] + nums[1]) or left == (nums[0] * nums[1])
    
    if  check(left, [nums[0] + nums[1]] + nums[2::], p1) or check(left, [nums[0] * nums[1]] + nums[2::], p1):
        return True
    if not p1:
        return check(left, [int(str(nums[0]) + str(nums[1]))] + nums[2::], p1) 
              

for line in f_in:
    left, right = line.split(': ')
    left = int(left)
    nums = list(map(int, right.split()))
    if check(left, nums):
        p1 += left
    if check(left, nums, False):
        p2 += left
print(p1)
print(p2)
