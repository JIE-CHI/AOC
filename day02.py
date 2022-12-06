#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:40:12 2022

@author: jiechi
"""

file_in = 'inputs/day02.txt'
text = open(file_in).read()
rounds = text.strip().split('\n')
shape = {'X':1, "Y":2, "Z":3}
res_shape = {'X':0, "Y":3, "Z":6}

score1 = 0 
score2 = 0
for i in rounds:
    oppon, me = i.split()
    score1 += shape[me]
    score2 += res_shape[me]
    if (oppon, me) in [('A', 'X'),('B','Y'),('C','Z')]:
        score1 += 3
    elif (oppon, me) in [('A', 'Y'),('B','Z'),('C','X')]:
        score1 += 6
    else:
        score1 += 0
    if (oppon,me) in [('B','X'), ('A', 'Y'), ('C', 'Z')] :
        score2 += 1
    elif (oppon,me) in [('C','X'), ('B', 'Y'), ('A', 'Z')] :
        score2 += 2
    else:
        score2 += 3
print(score1)
print(score2)
