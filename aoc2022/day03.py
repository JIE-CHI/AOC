#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:34:59 2022

@author: jiechi
"""
import string

letters = string.ascii_lowercase + string.ascii_uppercase
file_in = 'inputs/day03.txt'
text = open(file_in).readlines()
sum1 = 0
sum2 = 0
for line in text:
    line = line.strip()
    l = len(line)
    p1 = line[0:l//2]
    p2 = line[l//2::]
    for i in set(p1):
        if i in p2:
            sum1 += letters.index(i)+1
print(sum1)
            
for i in range(len(text)):
    if i%3 == 0:
        n1 = text[i].strip()
    elif i%3 == 1:
        n2 = text[i].strip()
    else:
        n3 = text[i].strip()
        for k in set(n1):
            if (k in n2) and (k in n3):
                sum2 += letters.index(k) + 1
print(sum2)