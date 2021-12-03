#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:02:27 2021

@author: jiechi
"""

import hashlib

secret_key = 'yzbqklnj'

def solve(key, i):
    
    num=0
    while (1):
        md5res = hashlib.md5((key + str(num)).encode('utf-8')).hexdigest()
        if md5res[0:i] == '0' * i:
            return num
        num += 1
        
        
    
print("*************result for part 1*************")
print(solve(secret_key, 5))
print("*************result for part 2*************")
print(solve(secret_key, 6))