#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:53:25 2022

@author: jiechi
"""

file_in = 'inputs/day01.txt'
text = open(file_in).read()
cals = text.strip().split('\n\n')
elf_cals = []
for cal in cals:
    elf = 0
    for num in cal.split('\n'):
        elf += int(num)
    elf_cals.append(elf)

elf_cals = sorted(elf_cals, reverse=True)
print(elf_cals[0])
print(sum(elf_cals[0:3]))
    
