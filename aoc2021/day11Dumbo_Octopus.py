#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:19:25 2021

@author: jiechi
"""


import numpy as np
f = open('inputs/day11.txt', 'r').read()
data = f.split('\n')
# test ='5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526'
# data = test.split('\n')
ar_data = np.zeros([10, 10], dtype = int)
for i in range(10):  
    row =  list(map(int, data[i]))
    ar_data[i] = row
    
def increase_one(ar_data, coord):
    x, y = coord
    if x == 0:
        if y == 0:
            ar_data[x+1][y] += 1
            ar_data[x+1][y+1] += 1
            ar_data[x][y+1] += 1
        elif y == len(ar_data[x]) -1:
            ar_data[x+1][y] += 1
            ar_data[x+1][y-1] += 1
            ar_data[x][y-1] += 1
        else:
            ar_data[x+1][y] += 1
            ar_data[x][y-1] += 1
            ar_data[x][y+1] += 1
            ar_data[x+1][y+1] += 1
            ar_data[x+ 1][y-1] += 1
    elif x == len(ar_data) -1:
        if y == 0:
            ar_data[x-1][y] += 1
            ar_data[x-1][y+1] += 1
            ar_data[x][y+1] += 1
        elif y == len(ar_data[x]) -1:
            ar_data[x-1][y] += 1
            ar_data[x-1][y-1] += 1
            ar_data[x][y-1] += 1
        else:
            ar_data[x-1][y] += 1
            ar_data[x][y-1] += 1
            ar_data[x][y+1] += 1
            ar_data[x-1][y+1] += 1
            ar_data[x-1][y-1] += 1
    else:
        if y == 0:
            ar_data[x-1][y] += 1
            ar_data[x-1][y+1] += 1
            ar_data[x][y+1] += 1
            ar_data[x+1][y] += 1
            ar_data[x+1][y+1] += 1

        elif y == len(ar_data[x]) -1:
            ar_data[x-1][y] += 1
            ar_data[x-1][y-1] += 1
            ar_data[x][y-1] += 1
            ar_data[x+1][y] += 1
            ar_data[x+1][y-1] += 1
        else:
            ar_data[x-1][y] += 1
            ar_data[x+1][y] += 1
            ar_data[x][y-1] += 1
            ar_data[x][y+1] += 1
            ar_data[x-1][y-1] += 1
            ar_data[x+1][y+1] += 1
            ar_data[x-1][y+1] += 1
            ar_data[x+ 1][y-1] += 1
    return ar_data
    

def check_flash(ar_data, flashed):
    coords = np.argwhere (ar_data > 9)    
    if len(coords) == len(flashed):
        return (ar_data, flashed)
    else:
        for coord in coords:
            if not coord.tolist() in flashed.tolist():
                ar_data = increase_one(ar_data, coord)
                flashed = np.append(flashed, coord).reshape(-1,2)
    return check_flash(ar_data, flashed)
    
def part1_solve(ar_data, steps = 3):
    count = 0
    for i in range(steps):
        ar_data = ar_data + 1
        ar_data, coords = check_flash(ar_data, np.asarray([], dtype = int))
        count += len(ar_data[np.where(ar_data > 9)])
        ar_data[np.where(ar_data > 9)] = 0
        
    return count

def part2_solve(ar_data):
    i = 1
    while(1):
        ar_data = ar_data + 1
        ar_data, coords = check_flash(ar_data, np.asarray([], dtype = int))
        if len(ar_data[np.where(ar_data > 9)]) == 10*10:
                 return i
        i += 1 
        ar_data[np.where(ar_data > 9)] = 0

print("*************result for part 1*************")
print(part1_solve(ar_data, steps =100))
print("*************result for part 2*************")
print(part2_solve(ar_data))