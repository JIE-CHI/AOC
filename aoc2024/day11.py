#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:06:11 2024

@author: jiechi
"""

f_in = open('inputs/day11.txt').read().strip()

stones = list(map(int, f_in.split()))



M = {}

def dp(stone, t):
    if (stone, t) in M:
        return M[(stone, t)]
    if t == 0:
        res = 1
    elif stone == 0:
        res = dp(1, t-1)
    elif  len(str(stone))%2 == 0:
            num = str(stone)
            n1 = int(num[0:len(num)//2])
            n2 = int(num[len(num)//2::])  
            res = dp(n1, t-1) + dp(n2, t-1)
    else:
        res = dp(stone * 2024, t-1)
    M[(stone, t)] = res
    return res

p1 = p2 = 0 
for s in stones:
    p1 += dp(s,25)
    p2 += dp(s,75)
    
print(p1)
print(p2)