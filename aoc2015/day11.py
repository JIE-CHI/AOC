#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:39:19 2022

@author: jiechi
"""

import string
alph = string.ascii_lowercase

incre3 = [alph[i:i+3] for i in range(len(alph)-2)] 

str1 = open("inputs/day11.txt").read().strip()

def check1(str1):
    for i in incre3:
        if i in str1:
            return True
    return False
    
def check2(str1):
    return len(set('iol') & set(str1)) == 0

def check3(str1):
    count = 0
    l1 = ''
    for a,b in zip(str1[0:-1], str1[1::]):
        if a == b and (a not in l1):
            count+=1
            l1 = a
        if count > 1:
            return True
    return False


def increment (str1):
    if str1 == '':
        return ''
    if str1[-1] < 'z':
        return str1[0:-1] + chr(ord(str1[-1])+1)
    else:
        return increment(str1[0:-1]) + 'a'

def f1(str1):
    
    while(1):
        if check1(str1) and check2(str1) and check3(str1):
            return(str1)
           
        else:
            str1 = increment(str1)
print(f1(str1))
print(f1(increment(f1(str1))))

        
        
