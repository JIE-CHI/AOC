#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:36:50 2025

@author: jiechi
"""

import numpy as np

f_in = open('inputs/day13.txt').readlines()

machines = []

for line in f_in:
    if line.startswith('Button A'):
        ax = int(line.split(',')[0].split('X+')[-1])
        ay = int(line.split(',')[1].split('Y+')[-1])
    elif line.startswith('Button B'):
        bx = int(line.split(',')[0].split('X+')[-1])
        by = int(line.split(',')[1].split('Y+')[-1])
    elif line.startswith('Prize'):
        px = int(line.split(',')[0].split('X=')[-1])
        py = int(line.split(',')[1].split('Y=')[-1])
        machines.append((ax,ay,bx,by,px,py))

# machines = [(94,34,22,67,8400,5400), (26,66,67,21,12748,12176), (17,86,84,37,7870,6450),(69,23,27,71,18641,10279)]
def solve(p1 = True):
    tot = 0
    eps = 1e-4
    for m in machines:
        (ax,bx,ay,by,px,py) = m
        x = np.array([[ax,ay], [bx,by]])
        y = np.array ([[px, py]]).T
        if not p1:
            y =  np.array ([[px + 10000000000000, py+10000000000000]]).T
        res = np.linalg.solve(x,y)
        a = res[0,0]
        b = res[1,0]

        if abs(a - round(a)) < eps and abs(b - round(b)) < eps and a>=0 and b>=0:
            if not p1 or (100>=round(a) and 100>=round(b)):
                if (np.dot(x, np.array([[round(a),round(b)]]).T) == y).all():
                    tot +=  round(a)*3 + round(b)
    return tot
print(solve())
print(solve(False))