#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:45:50 2022

@author: jiechi
"""

file_in = open('inputs/day13.txt').readlines()
table = {}
people = set()
for line in file_in :
    words = line.strip().split()
    people.add(words[0])
    sign = -1 if words[2] == 'lose' else 1
    table[(words[0], words[-1][0:-1])] = sign * int(words[3])

    
import itertools
possible = list(itertools.permutations(list(people)))

def calc(seats, table):
    score = 0
    seats.insert(0, seats[-1])
    seats.append(seats[1])
    # print(seats)
    for i in range(1, len(seats) -1 ):
        score += table[(seats[i], seats[i-1])]
        score += table[(seats[i], seats[i+1])]
    return score
score = 0
for i in itertools.permutations(list(people)):
    score = max(score, calc(list(i), table))
print(score)
for i in people:
    table[(i, 'me')] = 0
    table[('me', i)] = 0

people.add('me')
score = 0
for i in itertools.permutations(list(people)):
    score = max(score, calc(list(i), table))
print(score)