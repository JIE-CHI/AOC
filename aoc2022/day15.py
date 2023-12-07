#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:02:43 2022

@author: jiechi
"""
S ={}
text = open('inputs/day15.txt').readlines()
closest = set()
for line in text:
    sensor, beacon = line.split(':')
    xs = int(sensor.split(',')[0].split('x=')[1])
    ys = int(sensor.split(',')[1].split('y=')[1])
    xb = int(beacon.split(',')[0].split('x=')[1])
    yb = int(beacon.split(',')[1].split('y=')[1])
    S[xs,ys] = (xb, yb, abs(xb-xs) + abs(yb-ys))
    if yb == 2000000:
        closest.add((xb, yb))  
        
def fn(Y):
    pos = []
    for s, b in S.items():
        if abs(s[1] - Y) <= b[2]:
            pos.append([s[0] - (b[2] - abs(s[1] - Y)), s[0] + (b[2] - abs(s[1] - Y))])
    b = []
    for begin,end in sorted(pos):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b

tot = 0
for i in fn(2000000):
    tot += i[1] - i[0] + 1
print(tot - len(closest))
Y = 0
flag = True
while(flag):
    b = fn(Y)
    for i in b:
        if 0 <i[1] < 4000000:
            print(4000000 * (i[1] + 1) + Y)
            flag = False
    Y += 1