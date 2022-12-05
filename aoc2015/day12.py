#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:20:58 2022

@author: jiechi
"""

import json

with open('inputs/day12.txt') as f:
    d = json.load(f)


def read_json(k, nored):
    if type(k) in [int, str]:
        return [k]
    else:
        res = []
        if type(k) == dict:
            if nored:
                if 'red' in k.values():
                    return []
            for i in k:
                res.extend(read_json(i, nored))
                res.extend(read_json(k[i], nored))
        else:
            
            for i in k:
                res.extend(read_json(i, nored))
        return res


tot1 = 0
tot2 = 0
for k in read_json(d, False):
    if type(k) == int:
        tot1 += k
print(tot1)
for k in read_json(d, True):
    if type(k) == int:
        tot2 += k
print(tot2)