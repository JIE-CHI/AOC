#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:22:14 2022

@author: jiechi
"""

text = open('inputs/day18.txt').readlines()
cubes = set()
for cube in text:
    x,y,z =  map(int, cube.strip().split(','))
    cubes.add((x,y,z))
directions = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0),
]

def near_cube(cube,direction):
    return tuple(x+y for (x,y) in zip(cube, direction))

ans = len(cubes) * 6
for c in cubes:
    for d in directions:
        if (near_cube(c,d)) in cubes:
            ans -= 1
print(ans)

cubes = {cube: 0 for cube in cubes}

mins = tuple(min(x) - 1 for x in zip(*cubes))
maxs = tuple(max(x) + 1 for x in zip(*cubes))

start = [mins]
visited = set()

while start:
    u = start.pop(0)  
    if u in visited:
        continue
    visited.add(u)
    for d in directions:
        v = near_cube(u, d)
        if all(a <= b <= c for a, b, c in zip(mins, v, maxs)):
            if v in cubes:
                cubes[v] += 1
            else:
                start.append(v)

print(sum(cubes.values()))

