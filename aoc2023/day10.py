# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-10 20:47:52
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-12 17:52:49
lines = open('inputs/day10.txt').readlines()
grids = []

x = 0
for i in lines:
    grids.append(list(i.strip()))
    if 'S' in i:
        S = (x, list(i).index('S'))
    x += 1
visited = []
queue = []
step = 0
grids[S[0]][S[1]] = '7'
def find_neighbour(x,y,grids):
    neigh = []
    if x > 0:
        if grids[x][y] in ['|', 'L' ,'J']:
            neigh.append((x-1,y))
    if x < len(grids)-1:
        if grids[x][y] in ['|', '7' ,'F']:
            neigh.append((x+1,y))
    if y > 0:
        if grids[x][y] in ['-', '7' ,'J']:
            neigh.append((x,y-1))
    if y < len(grids[0]) -1:
        if grids[x][y] in ['-', 'L' ,'F']:
            neigh.append((x, y+1))
    return neigh

def bfs(visited, grids, node,step = 0):
    visited.append(node)
    queue.append((node[0], node[1],step))
    while queue:
        x,y,step = queue.pop(0)
        neigh = find_neighbour(x,y,grids)
        for neighbour in neigh:
            x,y = neighbour
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append((x,y,step+1))
    return visited,step

points, p1 = bfs(visited, grids,S)
print(p1)
points = sorted(points)
p2 = 0

for x in range(len(grids)):
    c_in = False
    for y in range(len(grids[0])):
        if (x,y) in points:
            if grids[x][y] in ['|', '7', 'F']:
                c_in = not c_in
        else:
            if c_in:
                p2+=1
print(p2)
 


    
    

