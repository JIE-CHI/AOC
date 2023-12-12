# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-11 13:22:49
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-11 15:28:11
import numpy as np
from itertools import combinations
grids = []
lines = open('inputs/day11.txt').readlines()
for i in lines:
    grids.append(list(i.strip()))
grids = np.asarray(grids)

emp_r = []
emp_c = []
for r,row in enumerate(grids):
    if np.all(row == '.'):
        emp_r.append(r)
for c,col in enumerate(grids.T):
    if np.all(col == '.'):
        emp_c.append(c)

galaxy = []
for r in range(len(grids)):
    for c in range(len(grids[0])):
        if grids[r][c] == '#':
            galaxy.append((r,c))
pairs = list(combinations(galaxy,2))

def find_len(x):
    p = 0
    for (a1,a2) in pairs:
        for r in emp_r:
            if min(a1[0],r,a2[0]) != r and  max(a1[0],r,a2[0]) != r:
                p += x-1
        for c in emp_c:
            if min(a1[1],c,a2[1]) != c and  max(a1[1],c,a2[1]) != c:
                p += x-1
        p += (abs(a2[1] - a1[1]) + abs(a2[0]-a1[0]))
    return p

print(find_len(2))
print(find_len(10**6))