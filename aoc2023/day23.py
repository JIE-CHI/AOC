# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-03 14:39:30
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-03 23:52:35

grids = []
with open('inputs/day23.txt') as f:
    for line in f:
        grids.append(line.strip())
S = (0, grids[0].index('.'))
E = (len(grids) -1, grids[-1].index('.'))

def next_node(node, p1 = True):
    ds = [(-1,0), (1,0), (0,-1), (0,1)]
    sym = ['^', 'v', '<', '>']
    adj = []
    (x,y) = node
    if  (not p1) or grids[x][y] == '.':
        for d in ds:
             if 0 <= x+d[0] < len(grids) and 0<=y+d[1]<len(grids[0]) and grids[x+d[0]][y+d[1]] != '#':
                adj.append((x+d[0],y+d[1]))
    else:
        d = ds[sym.index(grids[x][y])]
        adj.append((x+d[0],y+d[1]))
    return adj

points1 = set([S, E])
points2 = set([S, E])
for x, r in enumerate(grids):
    for y, c in enumerate(r):
        if grids[x][y] != '#' and len(next_node((x,y))) > 2:
            points1.add((x,y))
        if grids[x][y] != '#' and len(next_node((x,y), False)) > 2:
            points2.add((x,y))

def build_graph(points, p1 = True):
    graph = {p:{} for p in points}
    for p in points:
        (x,y) = p
        seen = set([p])
        stack = [(x,y,0)]
        while stack:
            r,c,n = stack.pop()
            if n>0 and (r,c) in points:
                graph[p][(r,c)] = n
                continue
            for (nx, ny) in next_node((r,c),p1):
                if(nx,ny) not in seen:
                    stack.append((nx,ny,n+1))
                    seen.add((nx,ny))
    return graph

graph1 =  build_graph(points1)
graph2 = build_graph(points2, False)  

visited = set()
def dfs(node, graph):  
    if node == E:
        return 0
    ans = -float('inf')
    visited.add(node)
    for x in graph[node]:
        if x not in visited:
            ans = max(ans, dfs(x,graph) + graph[node][x])
    visited.remove(node)
    return ans
print(dfs(S, graph1))
visited.clear()
print(dfs(S, graph2))