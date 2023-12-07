#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:05:17 2022

@author: jiechi
"""
from copy import deepcopy
text = open('inputs/day13.txt').read()
pairs = text.split('\n\n')
def compare (a1, a2):
    if isinstance(a1, int) and isinstance(a2, int):
        if a1 == a2:
            return -1
        else:
            return a1 < a2
    else:
        if isinstance(a1, int):
            a1 = [a1]
        elif isinstance(a2, int):
            a2 = [a2]
        a1 = deepcopy(a1)
        a2 = deepcopy(a2)
        while(a1 and a2):
            v1 = a1.pop(0)
            v2 = a2.pop(0)
            res = compare(v1, v2)
            if  res ==  -1:
                pass
            else:
                return res
        if not (a1 or a2):
            return -1
        return a1 == []      
tot = 0
new = []
for i, pair in enumerate (pairs):
    list1, list2 = pair.strip().split('\n')
    list1 = eval(list1)
    list2 = eval(list2)
    new += [list1]
    new += [list2]
    if compare(list1, list2):
        tot += i + 1
    
print(tot)


new += [[[2]], [[6]]]

for i in range(len(new) - 1):
    sort = True
    for k in range(len(new) - i - 1):
        if not compare(new[k], new[k+1]):
            new[k], new[k+1] =new[k+1], new[k]
            sort = False
    if sort:
        break
print((new.index([[2]]) + 1) * (new.index([[6]]) + 1))

            
        
    
    
