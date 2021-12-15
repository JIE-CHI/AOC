#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:34:49 2021

@author: jiechi
"""
from collections import defaultdict, Counter
f = open('./inputs/day14.txt', 'r').read()
start, inst = f.strip().split('\n\n')
inst_dict = defaultdict()
for i in inst.split('\n'):
    inst_dict[i.split(' -> ')[0]] = i.split('->')[1].strip()

def part1_solve(start, inst_dict, steps):
    for _ in range(steps):
        new_line = start[0]
        for i, k in zip(start, start[1::]):
            if i+k in inst_dict:
                new_line = new_line + inst_dict[i+k] + k
            else:
                new_line = new_line + k
        start = new_line
    res = Counter(new_line)
    return max(res.values())  - min(res.values())



def part2_solve(start, inst_dict, steps):
    C1 = Counter()
    for i in range(len(start)-1):
        C1[start[i]+start[i+1]] += 1
    for _ in range(steps):
        C2 = Counter()
        for k in C1:
            C2[k[0]+inst_dict[k]] += C1[k]
            C2[inst_dict[k]+k[1]] += C1[k]
        C1 = C2
    C3 = Counter()
    for k in C1:
        C3[k[0]] += C1[k]
    C3[start[-1]] += 1
    return max(C3.values())-min(C3.values())

print("*************result for part 1*************")
print(part1_solve(start, inst_dict, 10))
print("*************result for part 2*************")
print(part2_solve(start, inst_dict, 40))

                