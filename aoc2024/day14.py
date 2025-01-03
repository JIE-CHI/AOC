#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 02:03:34 2025

@author: jiechi
"""
from collections import Counter
f_in = open('inputs/day14.txt').readlines()
# f_in = open('test.txt').readlines()
points = []
for line in f_in:
    ps,vs = line.strip().split()
    p = list(map(int, ps.split('=')[1].split(',')))
    v = list(map(int, vs.split('=')[1].split(',')))
    points.append((p,v))

X = 101
Y = 103

def solve(seconds):
    P = []
    for i in range(len(points)):
        (p,v) = points[i]
        x = (v[0]*seconds+p[0])%X
        y = (v[1]*seconds+p[1])%Y
        P.append((x,y))
    
    q1 = q2 = q3 = q4 =0
    
    for (x,y) in P:
        if x < (X-1)/2 and y < (Y-1)/2:
            q1 += 1
        elif x < (X-1)/2 and y > (Y-1)/2:
            q2 += 1
        elif x > (X-1)/2  and y < (Y-1)/2:
            q3 += 1
        elif x > (X-1)/2 and y > (Y-1)/2:
            q4+=1
            
    return (q1 * q2 * q3 * q4)
    
p1 = solve(100)
print(p1)

lowest = p1
best = 100
for sec in range(10000):
    res = solve(sec)
    if res < lowest:
        lowest = res
        best = sec
print(best)    