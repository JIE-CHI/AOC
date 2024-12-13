#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:35:37 2024

@author: jiechi
"""

f_in = open('inputs/day09.txt').read().strip()
# f_in = '2333133121414131402'
files = []
lens = []
ii = 0
spaces = []
lens = []
s0 = 0
for i,c in enumerate(f_in):
    if i%2 == 0:
        files += [ii] * int(c)

        lens.append((s0, ii, int(c)))
        ii += 1
    else:
        files += ['.'] * int(c)
        spaces.append((s0,int(c)))
    s0 += int(c)
        
def p1(files):
    k1 = 0 
    k2 = len(files) - 1
    p1 = 0
    while(k1<k2):
        if files[k1] != '.':
            p1 += files[k1] * k1
            k1 += 1
        else:
            files[k1] = files[k2]
            k2 -= 1
    return p1

print(p1(files.copy()))
def p2(files):
    for f in lens[::-1]:
        si = 0
        while(si < len(spaces)):
            s = spaces[si]
            if s[0] > f[0]:
                break
            if s[1] >= f[2]:
                files[s[0]:s[0]+f[2]] = [f[1]] * f[2]
                files[f[0]:f[0]+f[2]] = ['.'] * f[2]
                spaces[si] = (s[0]+f[2], s[1]-f[2])
                break
            si += 1
    
    p2 = 0 
    for i,c in enumerate(files):
        if c != '.':
            p2 += i*c
    return p2
print(p2(files.copy()))
    
            
            
    
    


        
    
    
    