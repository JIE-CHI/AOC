#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:31:25 2022

@author: jiechi
"""

file_in = 'inputs/day06.txt'

text = open(file_in).read()
text = text.strip()

def f(str1, num):
    for i in range(len(str1)-num):
       if len(set(text[i:i+num])) == num:
           return(i+num)
           
print(f(text,4))
print(f(text,14))