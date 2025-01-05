#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 00:32:38 2025

@author: jiechi
"""
import heapq
from copy import deepcopy

def solve(G, s, p1 = True):
    q = [s]
    visited = set()
    lowest = float('inf')
    paths = set()
    while q:
        score, x, y, dx, dy, path = heapq.heappop(q)
        visited.add((x, y, dx, dy))
        if (x,y) == end:
            if p1:
                return score
            if score > lowest:
                return paths                
            else:
                lowest = score
                paths |= set(path)
        for (cost, next_dx, next_dy) in [(1, dx, dy), (1001, -dy, dx), (1001, dy, -dx)]:
            next_x = x + next_dx
            next_y = y + next_dy
            next_score = cost + score
            
            if G[next_x][next_y] == '#' or (next_x, next_y, next_dx, next_dy) in visited: 
                continue
            next_path = deepcopy(path)
            next_path.append((next_x, next_y))
            heapq.heappush(q, (next_score, next_x, next_y, next_dx, next_dy, next_path))

f_in = open('inputs/day16.txt').readlines()
# f_in = open('test.txt').readlines()
G = []
for x,line in enumerate(f_in):
    if 'S' in line:
        start = (0, x, line.index('S'),  0, 1, [(x, line.index('S'))])
    if 'E' in line:
        end = (x, line.index('E'))
    G.append(list(line.strip()))
    
print(solve(G,start, p1=True))
print((solve(G,start, p1=False)))

            
