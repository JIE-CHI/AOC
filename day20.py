#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:45:30 2022

@author: jiechi
"""

text = open('inputs/day20.txt').readlines()
nums = list(map(int, text))
def fn(part1):
    if part1:
        n = 1
        T = 1
    else:
        n = 811589153
        T = 10
    init1 = {(i,v* n):i for i,v in enumerate(nums)}
    init2 = {i:(i,v* n) for i,v in enumerate(nums)}
    for t in range(T):
        for (i, v), p in init1.items():
            if v == 0:
                continue
            pos = (p + v) % (len(nums) - 1)
            if pos < p:
                if pos == 0:
                    for k1 in range(p+1, len(nums)):
                        init1[init2[k1]] -= 1 
                        init2[k1-1] = init2[k1]
                    init1[i,v] = len(nums) -1
                    init2[len(nums) -1] = (i,v)  
                    continue
                for k1 in reversed(range(pos, p)):
                    init1[init2[k1]] += 1 
                    init2[k1+1] = init2[k1]
            else:
        
                for k1 in range(p+1, pos+1):
                    init1[init2[k1]] -= 1 
                    init2[k1-1] = init2[k1]
            init1[i,v] = pos
            init2[pos] = (i,v)
    for k,v in init2.items():
        if v[1] == 0:
            return(init2[(k + 1000) % len(nums)][1] + init2[(k + 2000) % len(nums)][1] +  init2[(k + 3000) % len(nums)][1])

print(fn(True))
print(fn(False))
    
    
    
    
    
    

