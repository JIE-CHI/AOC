#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 21:16:38 2024

@author: jiechi
"""

import string
allowed = set(string.digits + ',' + ')')


f_in = open('inputs/day03.txt').read()
# f_in = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
possible_muls = f_in.split('mul(')


def cal(p1 = True, do = 1):
    res = 0 
    for i,mul in enumerate(possible_muls):
        if p1:
            do = 1 
        if do > 0 and i > 0 and ')' in mul:
            span = mul.split(')')[0]
            if set(span) <= allowed and ',' in mul:
                num1, num2 = span.split(',')
                res += int(num1) * int(num2) 
        do_i = mul.rfind('do()')
        not_i = mul.rfind("don't()")
        
        if do > 0 and (not_i > do_i):
            do = -1
        elif do < 0   and (not_i < do_i):
            do = 1
    
    print(res)

cal()
cal(p1 = False)




