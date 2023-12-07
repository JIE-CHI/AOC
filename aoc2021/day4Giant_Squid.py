#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:25:04 2021

@author: jiechi
"""


import numpy as np
f = open("inputs/day4.txt", 'r')
data = f.read().strip()
num_input = list(map(int, data.split('\n\n')[0].split(',')))
grids = data.split('\n\n')[1::]
for i in range(len(grids)):
    table = grids[i].split('\n')
    grids[i] = np.array([list(map(int, k.split())) for k in table])
    
    
    
def part1_solve(num_input, grids):    
    grids_mark = np.zeros((len(grids),5,5))
    for num in num_input:
        for ind, grid in enumerate(grids):
            grids_mark[ind][np.where(grid == num)] = 1
            if 5 in np.sum(grids_mark[ind], axis = 0) or 5 in np.sum(grids_mark[ind], axis = 1):
                return (grid[np.where(grids_mark[ind] == 0)].sum() * num)
    
def part2_solve(num_input, grids):
    grids_mark = np.zeros((len(grids),5,5))
    win_list = []
    for num in num_input:
        for ind, grid in enumerate(grids):
            if not ind in win_list:
                grids_mark[ind][np.where(grid == num)] = 1
                if 5 in np.sum(grids_mark[ind], axis = 0) or 5 in np.sum(grids_mark[ind], axis = 1):
                    win_list.append(ind)
                    if len(win_list) == len(grids_mark):
                        return(grid[np.where(grids_mark[ind] == 0)].sum() * num)


print("*************result for part 1*************")
print(part1_solve(num_input, grids))
print("*************result for part 2*************")
print(part2_solve(num_input, grids))

