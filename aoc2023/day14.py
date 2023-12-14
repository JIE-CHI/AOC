# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-14 14:13:02
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-14 16:11:53
lines = open('inputs/day14.txt').read()
grids = []
for line in lines.strip().split("\n"):
    grids.append(list(line.strip()))
import numpy as np
grids = np.asarray(grids)

def tilt(grids):
    grids = grids.T
    for x in range(len(grids)):
        y1 = 0
        for y2 in range(len(grids[x])):
            if grids[x][y2] == 'O' and y1 < y2:
                grids[x][y2] = '.'
                grids[x][y1] = 'O'         
            elif grids[x][y2] == '#':
                y1 = y2
            while(y1 < len(grids[x]) and grids[x][y1] != '.' ):
                y1 += 1
    return grids.T

def cal_load(grids):
    res = 0
    for x in range(len(grids)):
        for y in range(len(grids[x])):
            if grids[x][y] == 'O':
                res += len(grids) - x
    return res

cycles = 1000000000
seen = {}
seen_cycle = {}
for cycle in range(1, 1+cycles):
    #north
    grids = tilt(grids)
    if cycle == 1:
        print(cal_load(grids))
    #west
    grids = tilt(grids.T).T
    #south
    grids = np.flipud(tilt(np.flipud(grids)))
    #east
    grids = np.rot90(tilt(np.rot90(grids,1)),3) 
    if grids.tobytes() in seen:
        break
    seen[grids.tobytes()] = cycle
    seen_cycle[cycle] = np.copy(grids)

first = (cycles - seen[grids.tobytes()])%(cycle - seen[grids.tobytes()])+seen[grids.tobytes()]
print(cal_load(seen_cycle[first]))
