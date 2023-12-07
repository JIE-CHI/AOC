#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:39:19 2022

@author: jiechi
"""
def f1 (num):
    res=''
    s = num[0]
    count = 1
    for i in num[1::]:
        if i == s:
            count += 1
        else:
            res += str(count) + s
            s = i
            count = 1
    res += str(count) + s
    return res

def f2(num):
    digits = open('inputs/day10.txt').read()
    digits = digits.strip()
    for i in range(num):
        digits = f1(digits)
    return len(digits)
print(f2(40))
print(f2(50))