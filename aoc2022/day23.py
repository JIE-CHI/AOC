# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-24 19:17:23
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-24 22:17:07
lines = open('inputs/day23.txt').readlines()

elves = set()
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '#':
            elves.add((x,y))
# N, S, W, E
directions = {'N':(-1,0), 'S':(1,0), 'W':(0, -1), 'E':(0, 1), 'NE':(-1,1), 'NW':(-1,-1), 'SE':(1,1), 'SW':(1,-1)}


rules = {'N': ['N','NE', 'NW'],'S': ['S', 'SE', 'SW'], 'W': ['W', 'NW', 'SW'], 'E':['E', 'NE', 'SE']}
order = ['N', 'S', 'W', 'E']
from copy import deepcopy

for i in range(10000):
    seen = set()
    twice = set()
    for (x, y) in elves:
        if all((x+directions[d][0],y+directions[d][1]) not in elves for d in directions):
            continue
        else:
            for k in order:
                v = rules[k]
                if all((x+directions[i][0],y+directions[i][1]) not in elves for i in v):
                    next_p = (x+directions[k][0], y+directions[k][1])
                    if next_p in seen:
                        twice.add(next_p)
                    else:
                        seen.add(next_p)
                    break
    new_elves = deepcopy(elves)
    for (x, y) in elves:
        if all((x+directions[d][0],y+directions[d][1]) not in elves for d in directions):
            continue
        else:
            for k in order:
                v = rules[k]
                if all((x+directions[i][0],y+directions[i][1]) not in elves for i in v):
                    next_p = (x+directions[k][0], y+directions[k][1])
                    if next_p not in twice:
                        new_elves.remove((x,y))
                        new_elves.add(next_p)
                    break
    if elves == new_elves:
        print(i+1)
        break
    elves = new_elves
    first = order.pop(0)
    order.append(first)

    if i == 9:
        minX = min(x for (x,y) in elves)
        maxX = max(x for (x,y) in elves)
        minY = min(y for (x,y) in elves)
        maxY = max(y for (x,y) in elves)
        print((maxX  - minX + 1) * (maxY - minY + 1) - len(elves))









