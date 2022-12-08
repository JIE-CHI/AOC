#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:57:22 2022

@author: jiechi
"""

real_aunt = {'children': 3 , 
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}
text = open('inputs/day16.txt').readlines()
aunts = []
for i in text:
    aunt = {}
    for k in real_aunt:
        if k in i:
            aunt[k] = int(i.split(k+': ')[1].split(',')[0])
    aunts.append(aunt)

def check1(aunt, real_aunt):
    for k,v in aunt.items():
        if v != real_aunt[k]:
            return False
    return True

def check2(aunt, real_aunt):
    for k,v in aunt.items():
        if k in ['cats', 'trees']:                
            if v <= real_aunt[k]:
                return False
        elif k in ['pomeranians', 'goldfish']:                
            if v >= real_aunt[k]:
                return False
        else:
            if v != real_aunt[k]:
                return False
    return True
for aunt in aunts:
    if check1(aunt, real_aunt):
        print(aunts.index(aunt) + 1)
        break
for aunt in aunts:
    if check2(aunt, real_aunt):
        print(aunts.index(aunt) + 1)
        break