#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:10:14 2022

@author: jiechi
"""
from collections import deque
text = open('inputs/day19.txt').readlines()
bp = {}
for line in text:
    words = line.strip().split()
    ro_o = int(words[6])
    rc_o = int(words[12])
    rob_o = int(words[18])
    rob_c = int(words[21])
    rg_o = int(words[27])
    rg_ob = int(words[30])
    bp[int(words[1][0:-1])] = (ro_o, rc_o, rob_o, rob_c, rg_o, rg_ob)


def fn(s, T):
    ro_o, rc_o, rob_o, rob_c, rg_o, rg_ob = s
    
    S = deque([(0, 0, 0, 0, 1, 0, 0, 0, T)])
    visited = set()
    g_max = 0
    ro_max = max(ro_o, rc_o, rob_o, rg_o)
    while(S):
        o, c, ob, g, ro, rc, rob, rg, T = S.popleft()
        if o >= T*ro_max-ro*(T-1):
            o = T*ro_max-ro*(T-1)
        if c>=T*rob_c-rc*(T-1):
            c = T*rob_c-rc*(T-1)
        if ob>=T*rg_ob - rob*(T-1):
            ob = T*rg_ob - rob*(T-1)
        if (o, c, ob, g, ro, rc, rob, rg, T) in visited or T==-1:
            continue
        visited.add((o, c, ob, g, ro, rc, rob, rg, T)) 
        T -= 1
        S.append((o+ro, c+rc, ob+rob, g+rg, ro, rc, rob, rg, T))
        if o >= ro_o and ro < ro_max:
            S.append((o-ro_o+ro, c+rc, ob+rob, g+rg, ro+1, rc, rob, rg, T))
        if o >= rc_o and rc < rob_c:
            S.append((o-rc_o+ro, c+rc, ob+rob, g+rg, ro, rc+1, rob, rg, T))
        if o >= rob_o and c >= rob_c and rob < rg_ob:
            S.append((o-rob_o+ro, c-rob_c+rc, ob+rob, g+rg, ro, rc, rob+1, rg, T))
        if o>=rg_o and ob>=rg_ob:
            S.append((o-rg_o+ro, c+rc, ob-rg_ob+rob, g+rg, ro, rc, rob, rg+1, T))
            
        g_max = max(g, g_max)
    return g_max
     
tot = 0   
for k,v in bp.items():
    print(k)
    tot  += k * fn(v, 24)
print(tot)

tot2 = 1 
for k,v in bp.items():
    tot2 *= fn(v, 32)
    if k == 3:
        break
print(tot2)