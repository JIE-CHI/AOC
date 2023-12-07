#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:52:58 2022

@author: jiechi
"""

from copy import deepcopy
text = open('inputs/day11.txt').read() 
monkeys = text.split("\n\n")
M0={}
def op(s, old):
    op1, op2 = s.split()
    if op2 == 'old':
        op2 = old
    if op1 == '*':
        return old * int(op2)
    elif op1 == '+':
        return old + int(op2)
    elif op1 == '-':
        return old - int(op2)
for i in monkeys:
    lines = i.split("\n")
    num = int(lines[0].split()[1][0:-1])
    starts = lines[1].split('Starting items:')[1]
    starts = [int(i) for i in starts.split(',')]
    operation = lines[2].split('new = old')[1]
    test = int(lines[3].split()[-1])
    true = int(lines[4].split()[-1])
    false = int(lines[5].split()[-1])
    M0[num] = {'items' : starts, 'op': operation, 'test': test, 'true':true, 'false': false}
div = 1
for k,v in M0.items():
    div *= v['test']
for rounds in [20, 10000]:
    M = deepcopy(M0)
    counts = [0 for i in range(len(M))]
    for i in range(rounds):
        for k,m in M.items():
            for item in m['items']:
                counts[k] += 1
                w = op(m['op'],item)
                if rounds == 20:  
                    w //= 3
                w %= div
                if w % m['test'] == 0:
                    M[m['true']]['items'].append(w)
                else:
                    M[m['false']]['items'].append(w)
            m['items'] = []
    print(sorted(counts)[-1] * sorted(counts)[-2])