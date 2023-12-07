#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:32:17 2022

@author: jiechi
"""

file_in = 'inputs/day04.txt'
text = open(file_in).readlines()
total1 = 0
total2= 0
for pair in text:
    elf1, elf2 = pair.strip().split(',')
    e11, e12 = elf1.split('-')
    e21, e22 = elf2.split('-')
    e11, e12, e21, e22 = [int(x) for x in [e11, e12, e21, e22]]
    if (e11 >= e21 and e12 <= e22) or (e11 <= e21 and e12 >= e22):
        total1 += 1
    if not(e11 > e22 or e21 > e12):
        total2 += 1


print(total1)
print(total2)