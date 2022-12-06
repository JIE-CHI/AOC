#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 04:54:48 2022

@author: jiechi
"""
import copy

file_in = 'inputs/day05.txt'

text = open(file_in).readlines()
text = [i.strip() for i in text]
elem = {}

for i in range(9):
    elem[i+1] = []

def move(item, start, end, elem, reverse):
    if reverse:
        for i in range(item-1, -1, -1):
            elem[end].insert(0, elem[start][i])
    else:
        for i in range(item):
            elem[end].insert(0, elem[start][i])
    del elem[start][0:item]
    return elem

for line in text:
    if line == '':
        elem2 = copy.deepcopy(elem)
    elif line[0] == '[':
        for char in range(len(line)-2):
            if char%4 == 0:
                if line[char+1] != ' ':
                    elem[char//4 +1].append(line[char+1])
    else:
        if 'move' in line:
            k = line.split() 
            elem = move(int(k[1]), int(k[3]),int(k[-1]), elem, False)
            elem2 = move(int(k[1]), int(k[3]),int(k[-1]), elem2, True)
  
res1 = [elem[i][0] for i in elem]
res2 = [elem2[i][0] for i in elem2]
print(''.join(res1))
print(''.join(res2))             
                    
                    
                
    
            
    