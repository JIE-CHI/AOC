# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-16 15:58:48
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-16 19:03:25
from collections import deque

lines = open('inputs/day16.txt').readlines()
grids = []
for line in lines:
    grids.append(list(line.strip()))

def find_neighbour(grids, s, d):
    x,y = s 
    if x > len(grids) -1 or x < 0 or y > len(grids[x]) - 1 or y < 0:
        return []
    if grids[x][y] == '.':
        return [(x+d[0], y+d[1],d)]
    if grids[x][y] == '-':
        if d in [(0,1),(0,-1)]:
            return [(x+d[0], y+d[1],d)]
        else:
            return [(x,y-1,(0,-1)), (x,y+1,(0,1))]
    if grids[x][y] == '|':
        if d in [(0,1),(0,-1)]:
            return [(x-1,y,(-1,0)), (x+1,y,(1,0))]
        else:
            return [(x+d[0], y+d[1],d)]
    if grids[x][y] == '/':
        d = (d[1] * -1, d[0] * -1)
        return [(x+d[0], y+d[1],d)]
    if grids[x][y] == "\\":
        d = (d[1], d[0])
        return [(x+d[0], y+d[1],d)]

def bfs(visited, grids, node): 
    visited = set()
    visited.add(node)
    queue = deque([node])     
    while queue:          
        x,y,d = queue.popleft()
        for neighbour in find_neighbour(grids,(x,y),d):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited
 
def count(grids,v):
    nodes = set()
    for c in v:
        if -1 < c[0] < len(grids) and -1 < c[1] < len(grids[0]) :
            nodes.add((c[0],c[1]))
    return len(nodes)

v = bfs([], grids, (0, 0, (0,1))) 
p1 = count(grids,v)
print(p1)
p2 = 0
seen = set()
for x in range(len(grids)):
    for y,d in zip([0, len(grids[0])-1],[1, -1]):
        v = bfs([], grids, (x,y, (0,d))) 
        p2 = max(p2, count(grids,v))

for y in range(len(grids[0])):
    for x,d in zip([0, len(grids)-1],[1, -1]):
        v = bfs([], grids, (x, y, (d,0))) 
        p2 = max(p2, count(grids,v))
print(p2)
