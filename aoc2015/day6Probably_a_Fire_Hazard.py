#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:50:41 2021

@author: jiechi
"""

from pandas import read_excel
import re
import numpy as np


filepath = 'inputs/inputs.xlsx'
sheetname = 'day6'
df = read_excel(filepath, sheet_name = sheetname, header = None)
instructions = df.iloc[:,0].values
#instructions = ['turn on 499,499 through 500,500']
# coords = re.findall(r'[0-9]+', instructions)

def part1_solve(instructions):
    grid = np.full([1000,1000], -1)
    for i in instructions:
        x1, y1, x2, y2 =[int(k) for k in re.findall(r'[0-9]+', i)]
        if 'turn on' in i:
            grid[x1:x2+1,y1:y2+1] = 1
        elif 'turn off' in i:
            grid[x1:x2+1,y1:y2+1] = -1
        elif 'toggle' in i:
            grid[x1:x2+1,y1:y2+1] *= -1
    return (np.sum(grid) + 1000 * 1000)/2

def part2_solve(instructions):
    grid = np.full([1000,1000], 0)
    for i in instructions:
        x1, y1, x2, y2 =[int(k) for k in re.findall(r'[0-9]+', i)]
        if 'turn on' in i:
            grid[x1:x2+1,y1:y2+1] += 1
        elif 'turn off' in i:
            grid[x1:x2+1,y1:y2+1] -= 1
            grid[x1:x2+1,y1:y2+1] [grid[x1:x2+1,y1:y2+1] <0] = 0
        elif 'toggle' in i:
            grid[x1:x2+1,y1:y2+1] += 2
    return np.sum(grid)

print("*************result for part 1*************")
print(part1_solve(instructions))
print("*************result for part 2*************")
print(part2_solve(instructions))
