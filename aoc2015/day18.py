#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:04:46 2022

@author: jiechi
"""

text = open('inputs/day18.txt').readlines()
grids = [list(line.strip()) for line in text]

def get_neighbors(x,y,grid):
    res = 0
    for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            if m==n==0:
                continue
            if len(grid) > x+m >= 0 and len(grid[0])> y+n >=0 :
                if grid[x+m][y+n] == '#':
                    res+=1
    return res

steps = 100
for step in range(steps):
    off = set()
    on = set()
    for x in range(len(grids)):
        for y in range(len(grids[0])):
            if grids[x][y] == '#' and (get_neighbors(x, y, grids) not in [2,3]):
                off.add((x,y))
            elif grids[x][y] == '.' and get_neighbors(x, y, grids) ==3:
                on.add((x,y))
    for (m,n) in off:
        grids[m][n] = '.'
    for (m,n) in on:
        grids[m][n] = '#'
print (sum(x.count('#') for x in grids))


grids = [list(line.strip()) for line in text]
grids[0][0] = grids[0][99] = grids[99][0] = grids[99][99] = '#'
for step in range(steps):
    off = set()
    on = set()
    for x in range(len(grids)):
        for y in range(len(grids[0])):
            if grids[x][y] == '#' and (get_neighbors(x, y, grids) not in [2,3]):
                off.add((x,y))
            elif grids[x][y] == '.' and get_neighbors(x, y, grids) ==3:
                on.add((x,y))
    for (m,n) in off:
        grids[m][n] = '.'
    for (m,n) in on:
        grids[m][n] = '#'
    grids[0][0] = grids[0][99] = grids[99][0] = grids[99][99] = '#'
print (sum(x.count('#') for x in grids))
                
                
                
                                       