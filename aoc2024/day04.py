#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:04:23 2024

@author: jiechi
"""

f_in = open('inputs/day04.txt').readlines()

# f_in = open('test.txt').readlines()

grids = []
for line in f_in:
    grids.append(list(line.strip()))
    
#..XMAS SAMX
def check_p1(grids, x,y):
    tot = 0
    if y + 4 <= Y :
        if grids[x][y:y+4] == ['X', 'M', 'A', 'S']:
            tot += 1
        if x+ 4 <= X :
            if (grids[x+1][y+1]  == 'M' and grids[x+2][y+2] == 'A' and grids[x+3][y+3] == 'S'):
                tot += 1
        if x >= 3:
            if grids[x-3][y+3]  == 'S' and grids[x-2][y+2] == 'A' and grids[x-1][y+1] == 'M':
                tot += 1
    if y >= 3:
        if grids[x][y-3:y+1] == ['S', 'A', 'M', 'X']:
            tot += 1
        if x+ 4 <= X :
            if (grids[x+1][y-1]  == 'M' and grids[x+2][y-2] == 'A' and grids[x+3][y-3] == 'S'):
                tot += 1     
        if x >= 3:
            if grids[x-3][y-3]  == 'S' and grids[x-2][y-2] == 'A' and grids[x-1][y-1] == 'M':
                tot += 1
    
    if x+ 4 <= X :
        if grids[x+1][y]  == 'M' and grids[x+2][y] == 'A' and grids[x+3][y] == 'S':
            tot += 1  
    if x >= 3:
        if grids[x-3][y]  == 'S' and grids[x-2][y] == 'A' and grids[x-1][y] == 'M':
            tot += 1
    return tot



def check_p2(grids, x,y):
    if 0 < x < X-1 and 0 < y < Y-1:
        if (grids [x-1][y-1] == 'M' and grids[x+1][y+1] == 'S') or (
               grids [x-1][y-1] == 'S' and grids[x+1][y+1] == 'M' ):
            if (grids [x-1][y+1] == 'M' and grids[x+1][y-1] == 'S') or (
                   grids [x-1][y+1] == 'S' and grids[x+1][y-1] == 'M' ):
                return 1
    return 0


X = len(grids)
Y = len(grids[0])
p1 = 0
p2 = 0
for row in range(X):
    for col in range(Y):
        if grids[row][col] == 'X' :
            p1 += check_p1(grids, row, col)
        if grids[row][col] == 'A' :
            p2 += check_p2(grids, row, col)
print(p1)
print(p2)
                       