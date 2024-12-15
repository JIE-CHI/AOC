#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:48:13 2024

@author: jiechi
"""
from collections import deque
f_in = open('inputs/day12.txt').readlines()
f_in = open('test.txt').readlines()

G = []
for line in f_in:
    G.append(list(line.strip()))

def get_price(r):
    area = len(r)
    tot = area * 4
    for (x,y) in r:
        for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            if (x+dx, y+dy) in r:
                tot -= 1
    return tot * area


def bfs(x,y):
    c = G[x][y]
    q = deque()
    q.append((x,y))
    visited = set()
    visited.add((x,y))
    while q:
        (x,y) = q.popleft()
        for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= x+dx < len(G) and 0<= y+dy < len(G[0]) and  G[x+dx][y+dy] == c:
                if not (x+dx, y+dy) in visited:
                    q.append((x+dx, y+dy))
                    visited.add((x+dx, y+dy))
        
    return visited
    

V = set()
R = []
for x in range(len(G)):
    for y in range(len(G[0])):
        if (x,y) not in V:
            r = bfs(x,y)
            R.append(r)
            V = V|r
            
p1 = 0 
for r in R:
    p1 += get_price(r)
        
print(p1)