#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:41:30 2025

@author: jiechi
"""

from collections import deque
f_in = open('inputs/day20.txt').readlines()
# f_in = open('test.txt').readlines()
G = []
for x,line in enumerate(f_in):
    if 'S' in line:
        (sx, sy) = (x, line.index('S'))
    G.append(list(line.strip()))
    


q = deque()
q.append((sx,sy,[(sx,sy)]))
visited = {(sx,sy)}

while q:
    x,y,p = q.popleft()
    for (dx,dy) in ([(-1,0), (1,0), (0,1), (0,-1)]):
        next_x = x+dx
        next_y = y+dy
        if G[next_x][next_y] == '#'  or (next_x, next_y) in visited:
            continue
        path = p + [(next_x, next_y)]
        q.append((next_x, next_y, path))
        visited.add((next_x, next_y))


def save(p, p1 = True):
    (x1,y1) = path[p]
    res = []
    for i in range(p+1, len(path)):
        (x2,y2) = path[i]
        if p1:
            if (abs(x2-x1) + abs(y2-y1) == 2):
               res.append(i-p-2)
        else:
            if 2<= (abs(x2-x1) + abs(y2-y1)) <= 20:
               res.append(i-p-(abs(x2-x1) + abs(y2-y1)))
    return res



p1 = 0
for p in range(len(path) - 2):
    for r in save(p):
        if r >= 100:
            p1 += 1
print(p1)
            
p2 = 0
for p in range(len(path) - 2):
    for r in save(p, p1= False):
        if r >= 100:
            p2 += 1
print(p2)  
    


