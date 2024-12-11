#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:39:20 2024

@author: jiechi
"""

f_in = open('inputs/day06.txt').readlines()
# f_in = open('test.txt').readlines()
G = []

for r, line in enumerate(f_in):
    if '^' in line:
        S = (r, line.index('^'))
    G.append(list(line.strip()))


D = [(-1, 0), (0,1), (1,0), (0,-1) ]
i = 0

def check(S,i):
    r,c = S
    p2 = set()
    while (0 < r < len(G)-1 and  0 < c < len(G[0])-1):
        d = D[i%4]
        if G[r+d[0]][c+d[1]] in ['.', '^']:
            r += d[0]
            c += d[1]
            if (r,c, d) in p2:
                return True
            else:
                p2.add((r,c, d))
        else:
            i+= 1
    return False


r,c = S
p2 = 0 
p1 = set([S])


while (0 < r < len(G)-1 and  0< c < len(G[0])-1):  
    d = D[i%4]
    if G[r+d[0]][c+d[1]] in ['.', '^']:
        if not(r+d[0], c+d[1]) in p1:
            G[r+d[0]][c+d[1]] = 'O'
            if check((r,c),i):    
                p2 += 1
            G[r+d[0]][c+d[1]] = '.'
        r += d[0]
        c += d[1]
        p1.add((r,c))
    else:
        i+= 1
        
print(len(p1))
print(p2)