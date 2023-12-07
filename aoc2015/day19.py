#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:53:09 2022

@author: jiechi
"""
import re

text = open('inputs/day19.txt').readlines()
rules = {}
for line in text:
    if line.strip() == '':
        break
    w1,w2 = line.strip().split(' => ')

    if w1 in rules: 
        rules[w1].append(w2)
    else:
        rules[w1] = [w2]
s = text[-1].strip()

r = set()
for w1,w2 in rules.items():
    for match in re.finditer(w1, s):
        for w in w2:
            r.add(s[0:match.start()] + w+ s[match.end()::] )
print(len(r))


#part2 https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/
s_list = re.findall('[a-zA-Z][^A-Z]*', s)
print(len(s_list) - s.count('Rn') - s.count('Ar') - 2 * s.count('Y') - 1)


