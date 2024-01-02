# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-25 17:44:10
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-02 17:27:27
grids = []
total = 1
with open('inputs/day21.txt') as f:
    for line in f:
        line = line.strip()
        grids.append(list(line))

for x, row in enumerate(grids):
    for y, c in enumerate(row):
        if c == 'S':
            S = (x,y)
        elif c == '.':
            total += 1

from collections import deque
queue = deque()
shortest_path = {}
queue.append((S,0))

while(queue):
    node, d = queue.popleft()
    if len(shortest_path) == total:
        break
    (x,y) = node
    if grids[x][y] == '#' or node in shortest_path:
        continue
    shortest_path[node] = d
    if x > 0:
        queue.append(((x-1,y),d+1))
    if x < len(grids)-1:
        queue.append(((x+1,y),d+1))
    if y > 0:
        queue.append(((x,y-1),d+1))
    if y < len(grids[x])-1:
        queue.append(((x,y+1),d+1))
p1 = 0
for node, d in shortest_path.items():
    if d%2==0 and d<65:
        p1 += 1
print(p1)
##part 2 from https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
full_odd = len({k: v for k, v in shortest_path.items() if v%2 == 1})
full_even = len({k: v for k, v in shortest_path.items() if v%2 == 0})
corner_odd = len({k: v for k, v in shortest_path.items() if v%2 == 1 and v > 65})
corner_even = len({k: v for k, v in shortest_path.items() if v%2 == 0 and v > 65})
n = ((26501365 - (len(grids)// 2)) // len(grids)) 
p2 = ((n+1)*(n+1)) * full_odd + (n*n) * full_even - (n+1) * corner_odd + n * corner_even
print(p2)