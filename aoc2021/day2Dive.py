#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:26:53 2021

@author: jiechi
"""
from pandas import read_excel
import numpy as np
# read input
file_path = './inputs/inputs.xlsx'
sheetname = 'day2' 
df = read_excel(file_path, sheet_name = sheetname, header=None)
data = df.iloc[:,0].values
# test = np.array(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
# data = test


def part1_solve(data, horiz = 0, depth = 0, aim = 0):
    for i in data:
        action, value = i.split()
        if action == 'forward':
            horiz += int(value)
        elif action == 'down':
            depth += int(value)
        elif action == 'up':
            depth -= int(value)
    return(horiz * depth)

def part2_solve(data, horiz = 0, depth = 0, aim = 0):
    for i in data:
        action, value = i.split()
        if action == 'forward':
            horiz += int(value)
            depth += int(value) * aim
        elif action == 'down':
            aim += int(value)
        elif action == 'up':
            aim -= int(value)
    return(horiz * depth)


print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))

