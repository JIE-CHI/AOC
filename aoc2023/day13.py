# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-13 15:00:19
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-13 15:49:33
import numpy as np

lines = open('inputs/day13.txt').read()
parts = lines.split("\n\n")

def scan (grids,x, p2 = False):
    left =x
    right = x+1
    diff = 0
    while(left >=0 and right < len(grids)):
        if not p2 and np.sum(grids[left] != grids[right]) > 0:
            return False
        diff += np.sum(grids[left] != grids[right])
        if diff > 1:
           return False 
        left -= 1
        right += 1
    if p2:
        return diff == 1
    return True

p1 = 0
p2 = 0
for part in parts:
    grids = []
    for line in part.strip().split("\n"):
        grids.append(list(line))
    grids = np.asarray(grids)
    for x in range(len(grids)-1):
        if scan(grids,x):
            p1 += (x+1)*100
        if scan(grids,x, 1):
            p2 += (x+1)*100
    for y in range(len(grids[0])-1):
        if scan(grids.T,y):
            p1 += y+1
        if scan(grids.T,y, 1):
            p2 += y+1
print(p1)
print(p2)