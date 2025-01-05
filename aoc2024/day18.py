#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:18:40 2025

@author: jiechi
"""


from collections import deque
from copy import deepcopy
f_in = open('inputs/day18.txt').readlines()
points = []
for line in f_in:
    x, y = list(map(int, line.strip().split(',')))
    points.append((x,y))
G = []
for x in range(71):
    row = []
    for y in range(72):
        row.append('.')
    G.append(row)

steps = 1024
for step in range(steps):
    x,y = points[step]
    G[x][y] = '#'
    
def bfs(G):

    q = deque()
    q.append((0, 0, 0))
    visited = set()
    visited.add((0,0))
    while q:
        x,y,step = q.popleft()
        for (dx,dy) in [(-1,0), (1,0), (0,1), (0,-1)]:
            next_x = x+dx
            next_y = y+dy
            next_step = step+1    
            if not (0<=next_x<71 and 0 <= next_y<71):
                continue
            if next_x == next_y == 70:
                return next_step
            if (next_x, next_y) in visited:
                continue
            if G[next_x][next_y] == '.':
                q.append((next_x, next_y, next_step))
            visited.add((next_x, next_y))
print(bfs(G))


for num in range(1024, len(points)):
    x,y = points[num]
    G[x][y] = '#'
    G_copy = deepcopy(G)
    if bfs(G_copy) is None:
        print(x,y)
        break

