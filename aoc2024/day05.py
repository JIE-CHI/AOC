#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:05:29 2024

@author: jiechi
"""
from collections import defaultdict
from functools import cmp_to_key

f_in = open('inputs/day05.txt').read()
# f_in = open('test.txt').read()
rules, updates = f_in.split('\n\n')
Rs = defaultdict(int)

for line in rules.split('\n'):
    nums = list(map(int, line.split('|')))
    Rs[nums[0], nums[1]] = 1
    
# for x in Rs.keys():
#     for y, yl in Rs.items():
#         if x in yl:
#             Rs[y]= set(Rs[x]) | set(Rs[y])
          

def check(update):
    for num in range(len(update)-1):
        for prev in range(num+1, len(update)):
            if Rs[update[prev] , update[num]] == 1:
                return False
    return True


def cmp(x,y):
    if Rs[x,y] == 1:
        return -1
    elif Rs[y,x] == 1:
        return 1
    return 0
    
    
p1 = 0
p2 = 0
for line in updates.strip().split('\n'):
    update = list(map(int, line.split(',')))
    if check(update):
        p1 += update[len(update)//2]
    else:
        update = sorted(update, key=cmp_to_key(cmp))
        p2 += update[len(update)//2]

print(p1)
print(p2)
                
        
    