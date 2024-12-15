#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:24:29 2024

@author: jiechi
"""
from collections import deque


f_in = open('inputs/day10.txt').readlines()

G = []
S = []
for x,line in enumerate(f_in):
    line = list(map(int, line.strip()))
    G.append(line)
    for y, c in enumerate(line):
        if c == 0:
            S.append((x,y))

def bfs(G, s):
    q = deque()
    visited = set()
    visited.add(s)
    q.append(s)
    tot = 0
    while q: 
        curr = q.popleft()
        x,y = curr
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            dx, dy = d
            if 0 <= x + dx < len(G) and 0 <= y+dy < len(G[0]) and G[x+dx][y+dy] - G[x][y] == 1:
                if not (x+dx, y+dy) in visited:
                    q.append((x+dx, y+dy))
                    visited.add((x+dx, y+dy) )
                    if  G[x+dx][y+dy] == 9:
                        tot += 1
    return tot

M = {}
def dp(G,s):
    x, y = s
    if s in M:
        return M[s]
    if G[x][y] == 9:
        return 1
    tot = 0
    for d in [(-1,0), (1,0), (0,-1), (0,1)]:
        dx, dy = d
        if 0 <= x + dx < len(G) and 0 <= y+dy < len(G[0]) and G[x+dx][y+dy] - G[x][y] == 1:
            tot += dp(G,(x+dx, y+dy))
    M[s] = tot 
    return tot

p1 = p2 = 0
for s in S:
    p1 += bfs(G,s)
    p2 += dp(G,s)

print(p1)
print(p2)