#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:18:10 2021

@author: jiechi
"""
import numpy as np
f_in = open('inputs/day25.txt', 'r').read().strip()
#f_in = open('inputs/test.txt', 'r').read().strip()
lines = f_in.split('\n')
grids = np.chararray((len(lines), len(lines[0])), unicode = True)

for i in range(len(lines)):
    for k in range(len(lines[0])):
        grids[i][k] = lines[i][k]

move = True
step = 0
print(grids)
while move:
    empty = np.zeros(grids.shape)
    moved = np.zeros(grids.shape)
    step += 1
    move = False
    for i in range(len(grids)):
        for j in range(len(grids[0])):
            if grids[i][j] == '>' and moved[i][j] == 0:
                if j < len(grids[0]) - 1:
                    next_j = j + 1
                else:
                    next_j = 0
                if grids[i][next_j] == '.' and empty[i][next_j] == 0:
                    empty[i][j] = 1
                    grids[i][j] = '.'
                    grids[i][next_j] = '>'
                    moved[i][next_j] = 1
                    move = True
      #              print(grids)
    empty = np.zeros(grids.shape)
    moved = np.zeros(grids.shape)
    for j in range(len(grids[0])):
        for i in range(len(grids)):
            if grids[i][j] == 'v' and moved[i][j] == 0:
                if i < len(grids) - 1:
                    next_i = i + 1
                else:
                    next_i = 0
                if grids[next_i][j] == '.' and empty[next_i][j] == 0:
                    empty[i][j] = 1
                    grids[i][j] = '.'
                    grids[next_i][j] = 'v'
                    moved[next_i][j] = 1
                    move = True

print(step)