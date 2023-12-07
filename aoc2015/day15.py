#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:19:50 2022

@author: jiechi
"""

from itertools import product

text = open('inputs/day15.txt').readlines()
recipe = {}
for i in text:
    name = i.split(':')[0]
    words = i.split(',')
    cap, dur, fla, tex, cal = [int(words[m].split()[-1]) for m in range(len(words))]
    recipe[name] = [cap, dur, fla, tex, cal]

def cal(recipe, comb):
    cap, dur, fla, tex, cals = [0]* 5
    for (name, v) in comb:
        cap += recipe[name][0] * v
        dur += recipe[name][1] * v
        fla += recipe[name][2] * v
        tex += recipe[name][3] * v
        cals += recipe[name][4] * v
    return [cap * dur * fla * tex, cals] if (cap>0 and dur >0 and fla >0 and tex>0) else [0,0]
        
        
    
names = list(recipe.keys())
score1 = 0
score2 = 0
for comb in product(range(101), repeat = 3):
    if sum(comb) <= 100:
        comb += (100 - sum(comb),)
        res, cals =  cal(recipe, [(names[i], comb[i]) for i in range(len(names))])
        score1 = max(score1,res)
        if cals == 500:
            score2 = max(score2, res)
print(score1)
print(score2)
    
        
    