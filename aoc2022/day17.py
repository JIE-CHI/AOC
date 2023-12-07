#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:32:06 2022

@author: jiechi
"""
from itertools import groupby

directions = open('inputs/day17.txt').read().strip()
# directions = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
d_len = len(directions)
def get_rock(i,y):
    if i == 0:
        return [(2,y), (3,y), (4,y), (5,y)]
    elif i == 1:
        return [(2,y+1), (3,y), (3,y+1), (3,y+2), (4,y+1)]
    elif i == 2:
        return [(2,y), (3,y), (4,y), (4,y+1), (4, y+2)]
    elif i == 3:
        return [(2,y), (2,y+1), (2,y+2), (2,y+3)]
    elif i == 4:
        return [(2,y), (3,y), (2,y+1), (3,y+1)]

def move(direction, rock, R):
    if direction == '>':
        if max([x for (x,y) in rock]) == 6:
            return rock
        new_rock = [(x+1,y) for (x,y) in rock]
    elif direction == '<':
        if min([x for (x,y) in rock]) == 0:
            return rock
        new_rock = [(x-1,y) for (x,y) in rock]
    elif direction == 'v':
        return  [(x,y-1) for (x,y) in rock]
    elif direction == '^':
        return[(x,y+1) for (x,y) in rock]
    if set(new_rock) & set(R):
        return rock
    else:
        return new_rock
    

def get_shape(R):
    R.sort()
    grouped = groupby(R, key=lambda v:v[0])
    maximums = [max(groups) for value, groups in grouped]
    y_min = min([y for (x,y) in maximums])
    shape = set()
    for (x,y) in R:
        if y >= y_min:
            shape.add((x,y - y_min))
    return frozenset(shape)

def fn(I):
    R = [(x,0) for x in range(7)]    
    i = 0
    d = 0
    r = frozenset(R)
    V = {(i,d,r): (i,max([y for (x,y) in R]))}
    seen = False
    while(i < I):
        topy = max([y for (x,y) in R])
        rock = get_rock(i%5, topy +4)
        while (1):
            rock = move(directions[d%d_len], rock, R)
            d += 1
            rock = move('v', rock, R)
            if set(rock) & set(R):
                rock = move('^', rock, R)
                R += rock
                shape = get_shape(R)
                if not seen and (i%5, (d-1)%d_len, shape) in V:
                    seen = True
                    i1, y1 = V [(i%5, (d-1)%d_len, shape)]
                    dy = max([y for (x,y) in R]) - y1
                    k = (I - i)//(i - i1)
                    i = i1 + (i - i1) * k
                    R =[(x, y + dy * (k -1)) for (x,y) in R]
                else:
                    V [(i%5, (d-1)%d_len, shape)] = (i, max([y for (x,y) in R]))
                break
        i += 1
    return max([y for (x,y) in R])
print(fn(2022))
print(fn(1000000000000))
        
    
    
    
            