#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:12:26 2021

@author: jiechi
"""
from collections import defaultdict, Counter, deque
f = open('inputs/day12.txt', 'r').read().strip()
paths = f.split('\n')
path_dict = {}
for path in paths:
    left, right = path.split('-')
    if left in path_dict:
        path_dict[left].append(right)
    else:
        path_dict.update({left:[right]})
    if right in path_dict:
        path_dict[right].append(left)
    else:
        path_dict.update({right:[left]})
    
final_path = []

    
E = path_dict 

def solve(p1):
    start = ('start', set(['start']), None)
    ans = 0
    Q = deque([start])
    while Q:
        pos, small, twice = Q.popleft()
        if pos == 'end':
            ans += 1
            continue
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end'] and not p1:
                Q.append((y, small, y))
    return ans
print(solve(p1=True))
print(solve(p1=False))
    