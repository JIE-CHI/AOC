#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:20:25 2021

@author: jiechi
"""

import numpy as np

f = open('./inputs/day9.txt', 'r')
nums = f.read().strip().split('\n')
# test = '2199943210\n3987894921\n9856789892\n8767896789\n9899965678'
# nums = test.split('\n')

data = np.zeros([len(nums), len(nums[0].strip())])


for i in range(len(nums)):
    row = list(map(int, nums[i].strip()))
    data[i] = row
    

        
def part1_solve(data):
    count = 0
    for m in range(len(data)):
        for n in range(len(data[m])):
            if m == 0:
                if n == 0:
                    if data[m][n] < min(data[m][n+1], data[m+1][n]):
                        count = count + 1 + data[m][n]
                elif n == len(data[m]) -1:
                    if data[m][n] < min(data[m][n-1], data[m+1][n]):
                        count = count + 1 + data[m][n]
                else:
                    if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m+1][n]):
                        count = count + 1 + data[m][n]
            elif m == len(data)-1:
                if n == 0:
                    if data[m][n] < min(data[m][n+1], data[m-1][n]):
                        count = count + 1 + data[m][n]
                elif n == len(data[m]) -1:
                    if data[m][n] < min(data[m][n-1], data[m-1][n]):
                        count = count + 1 + data[m][n]
                else:
                   if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m-1][n]):
                        count = count + 1 + data[m][n]
            elif n == 0:
                if data[m][n] < min(data[m][n+1], data[m+1][n], data[m-1][n]):
                        count = count + 1 + data[m][n]
            elif n == len(data[m]) -1:
                if data[m][n] <  min(data[m][n-1], data[m-1][n], data[m+1][n]):
                        count = count + 1 + data[m][n]
            else:
                if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m+1][n], data[m-1][n]):
                        count = count + 1 + data[m][n]
    return count

def check_all(data, coord, path):
    up = check_up(data, coord, path)
    down = check_down(data, coord, path)
    left = check_left(data, coord, path)
    right = check_right(data, coord, path)
    path.extend([up[0], down[0], left[0], right[0]])
    return (path, up[1] + down[1] + left[1] + down[1])

def check_up(data, coord, path):
    m, n = coord
    if m ==0 or data[m-1][n] ==9:
        return (None, 0)
    else:
        return ((m-1,n), (1 + check_all(data, (m-1, n), path)[1])) if data[m][n] < data[m -1][n] else (None, 0)

def check_down(data, coord, path):
    m, n = coord
    if m == len(data) -1 or data[m+1][n] ==9:
        return (None, 0)
    else:
        return ((m+1, n), (1 + check_all(data, (m+1, n), path)[1])) if data[m][n] < data[m +1][n] else (None, 0)
def check_left(data, coord, path):
    m, n = coord
    if n == 0 or data[m][n-1] ==9:
        return (None, 0)
    else:
        return ((m, n-1), (1 + check_all(data, (m, n-1), path)[1])) if data[m][n] < data[m][n -1] else (None, 0)

def check_right(data, coord, path):
    m, n = coord
    if n == len(data[m]) -1 or data[m][n+1] ==9:
        return (None, 0)
    else:
        return ((m, n+1),(1 + check_all(data, (m, n+1), path)[1])) if data[m][n] < data[m][n +1] else (None, 0)


def get_basin(data, coord):
    path = []
    m, n = coord
    path, basin_size = check_all(data, coord, path)
    path = list(filter(None, path))
    return len(set(path)) + 1
     


def part2_solve(data):
    basins = []
    for m in range(len(data)):
        for n in range(len(data[m])):
            if m == 0:
                if n == 0:
                    if data[m][n] < min(data[m][n+1], data[m+1][n]):
                        basins.append(get_basin(data, (m, n)))
                elif n == len(data[m]) -1:
                    if data[m][n] < min(data[m][n-1], data[m+1][n]):
                        basins.append(get_basin(data, (m, n)))
                else:
                    if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m+1][n]):
                        basins.append(get_basin(data, (m, n)))
            elif m == len(data)-1:
                if n == 0:
                    if data[m][n] < min(data[m][n+1], data[m-1][n]):
                        basins.append(get_basin(data, (m, n)))
                elif n == len(data[m]) -1:
                    if data[m][n] < min(data[m][n-1], data[m-1][n]):
                        basins.append(get_basin(data, (m, n)))
                else:
                   if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m-1][n]):
                        basins.append(get_basin(data, (m, n)))
            elif n == 0:
                if data[m][n] < min(data[m][n+1], data[m+1][n], data[m-1][n]):
                        basins.append(get_basin(data, (m, n)))
            elif n == len(data[m]) -1:
                if data[m][n] <  min(data[m][n-1], data[m-1][n], data[m+1][n]):
                        basins.append(get_basin(data, (m, n)))
            else:
                if data[m][n] <  min(data[m][n-1], data[m][n+1], data[m+1][n], data[m-1][n]):
                        basins.append(get_basin(data, (m, n)))
    basins = sorted(basins, reverse=True)[0:3]
    return basins[0] * basins[1] * basins[2]
print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))
                
            
        
        
        