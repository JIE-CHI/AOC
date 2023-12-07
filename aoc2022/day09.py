#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:52:59 2022

@author: jiechi
"""
from math import floor,ceil
motions = open('inputs/day09.txt').readlines()
grids = {(0,0):1}

def move_head(head, direction):
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'L':
        head[0] -= 1
    elif direction == 'R':
        head[0] += 1
    return head
def move_tail(head, tail):
    if head[0] < tail[0]:
        tail[0] = floor((head[0] + tail[0])/2) 
    else:
        tail[0] = ceil((head[0] + tail[0])/2)
    if head[1] < tail[1]:
        tail[1] = floor((head[1] + tail[1])/2)
    else:
        tail[1] = ceil((head[1] + tail[1])/2)
    return tail
def check_tail(head, tail):
    return False if abs(head[0] - tail[0]) <2 and  abs(head[1] - tail[1]) <2 else True

head  = [0,0]
tail = [0,0]

for motion in motions:
    direction, steps = motion.split()
    for i in range(int(steps)):
        head = move_head(head, direction)
        if check_tail(head, tail):
            tail = move_tail(head, tail)
            if tuple(tail) in grids:
                grids[tuple(tail)] += 1
            else:
                grids[tuple(tail)] = 1
print(len(grids))

knots = {i:[0,0] for i in range(10)}
grids2 = {(0,0):1}
for motion in motions:
    direction, steps = motion.split()
    for i in range(int(steps)):
        knots[0] = move_head(knots[0], direction)
        for k in range(9):
            if check_tail(knots[k], knots[k+1]):
                knots[k+1] = move_tail(knots[k], knots[k+1])
                if k == 8:
                    if tuple(knots[k+1]) in grids2:
                        grids2[tuple(knots[k+1])] += 1
                    else:
                        grids2[tuple(knots[k+1])] = 1
            else:
                break
print(len(grids2))

            
            
            