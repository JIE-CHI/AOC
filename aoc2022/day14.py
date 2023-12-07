#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:50:36 2022

@author: jiechi
"""

text = open('inputs/day14.txt').readlines()
# text = ['498,4 -> 498,6 -> 496,6',
# '503,4 -> 502,4 -> 502,9 -> 494,9']
# 24, 93
grid = {}
minx = 500
maxx = 500
maxy = 0
for line in text:
    points = line.split('->')
    for m, n in zip(points[0:-1], points[1::]):
        mx, my = list(map(int,m.split(',')))
        nx, ny = list(map(int,n.split(',')))
        minx = min(minx, min(nx, mx))
        maxx = max(maxx, max(nx, mx))
        maxy = max(maxy, max(ny, my))
        for x in range(min(mx, nx), max(mx,nx)+1):
            for y in range(min(my, ny), max(my,ny)+1):
                grid[x,y] = 1
maxy += 2     
start = (500, 0)

def move(pos, grid, part1):
    global minx, maxx, maxy
    (x,y) = pos
    if y+1 == maxy:
        return (0,0)
    if not (x,y+1) in grid:
        return (x,y+1)
    elif not (x-1, y+1) in grid:
        if part1 and x - 1 < minx:
            return (-1, -1) 
        else:
            return (x-1, y+1)
    elif not (x+1, y+1) in grid:
        if part1 and x+1 > maxx:
            return(-1,-1)
        else:
            return (x+1, y+1)
    return (0, 0)


from copy import deepcopy
def fn(start, grid, part1):
    grid = deepcopy(grid)
    tot = 0
    while (1):
        pos = start
        moved = True
        while(1):
            if move(pos, grid, part1) == (-1,-1):
                moved = False
                break
            elif move(pos, grid, part1) == (0,0):
                if pos == start:
                    moved = False
                    tot += 1
                grid[pos] = 1
                break
            else:
                pos = move(pos, grid, part1)
        if not moved:
            break
        tot += 1
    return tot
print(fn(start, grid, True))
print(fn(start, grid, False))
    
    
    