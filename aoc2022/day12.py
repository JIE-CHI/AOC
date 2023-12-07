#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:59:42 2022

@author: jiechi
"""

text = open('inputs/day12.txt').read()
graph = {}
m = 0
# text = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi'
for row in text.split("\n"):
    row = row.strip()
    n = 0
    for s in row:
        if s == 'S':
            start = (m,n)
        elif s == 'E':
            target = (m,n)
        graph[(m,n)] = s
        n += 1
    m += 1
graph[start] = 'a'
graph[target] = 'z'
def check (s1, s2, graph, part2):
    if not s2 in graph:
        return False
    else:
        if not part2:      
            return ord(graph[s1]) >= ord(graph[s2]) - 1
        else:
            return ord(graph[s1]) <= ord(graph[s2]) + 1
def adj (garph, node, part2):
    (x, y) = node
    adjs = []
    for rx, ry in [(-1,0),(0,1),(1,0),(0,-1)]:
        if check((x,y),(x + rx, y +ry), graph, part2):
            adjs.append((x + rx, y +ry))
    return adjs
def bfs(graph, node, target,part2 = False):
    visited = [node]
    queue = [node]
    dist = {node:0}
    while(queue):
        node = queue.pop(0)
        for i in adj(graph, node, part2):
            if i not in visited:
                visited.append(i)
                queue.append(i)
                dist[i] = dist[node]+1
                if part2:
                    if graph[i] == target:
                        return dist[i]
                else:                    
                    if i == target:
                        return dist[i]
    return 999999
                
print(bfs(graph, start, target))
print(bfs(graph, target, 'a', True))