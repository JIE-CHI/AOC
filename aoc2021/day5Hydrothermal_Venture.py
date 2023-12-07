#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:14:31 2021

@author: jiechi
"""

from pandas import read_excel
import numpy as np

filepath = './inputs/inputs.xlsx'
sheetname = 'day5'
df = read_excel(filepath, sheet_name = sheetname, header = None)
rawdata = df.iloc[:,0].values
# test = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
# rawdata = test
data = []
grid_len = 0
for i in rawdata:
    x1, y1 = list(map(int, i.split('->')[0].split(',')))
    x2, y2 = list(map(int, i.split('->')[1].split(',')))
    grid_len = max (x1, x2, y1, y2, grid_len)
    data.append([x1, y1, x2, y2])


def part1_solve(data, grid_len):
        
    grid = np.zeros ([grid_len+1, grid_len+1])
    
    for line in data:
        x1, y1, x2, y2 = line
        
        
        if x1 == x2:
            y1, y2 = sorted([y1,y2])
            grid[x1][y1:y2+1] += 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            grid[x1:x2+1][:,y1] += 1
    return np.count_nonzero(grid>=2)

def part2_solve(data, grid_len):
    
    grid = np.zeros ([grid_len+1, grid_len+1])
    for line in data:
        x1, y1, x2, y2 = line
        
        
        if x1 == x2:
            y1, y2 = sorted([y1,y2])
            grid[x1][y1:y2+1] += 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            grid[x1:x2+1][:,y1] += 1
    
    
        else:
            if x1<x2:
                if y1<y2:
                    for i in range(x2-x1+1):
                        grid[x1+i][y1+i] += 1
                else:
                    for i in range(x2-x1+1):
                        grid[x1+i][y1-i] += 1
            else:
                if y1 < y2:
                    for i in range(x1-x2+1):
                        grid[x1-i][y1+i] += 1
                else:
                    for i in range(x1-x2+1):
                        grid[x1-i][y1-i] += 1
    return np.count_nonzero(grid>=2)
                        
                        
print("*************result for part 1*************")
print(part1_solve(data, grid_len))
print("*************result for part 2*************")
print(part2_solve(data, grid_len))

