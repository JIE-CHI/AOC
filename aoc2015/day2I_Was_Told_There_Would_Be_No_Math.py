#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:54:01 2021

@author: jiechi
"""

from pandas import read_excel

filepath = './inputs/inputs.xlsx'
sheetname = 'day2'
df = read_excel(filepath, sheet_name = sheetname, header = None)
data = df.iloc[:,0].values



def find_small(numbers):
    n1 = n2 = float('inf')
    for n in numbers:
        if n <= n1:
            n1, n2 = n, n1
        elif n < n2:
            n2 = n
    return n1, n2

def part1_solve(data):
    area = 0
    for i in data:
        l, w, h = [int(k) for k in i.split('x')]    
        n1, n2 = find_small([l, w, h])
        area += 2 * (l * w + l * h + w * h) + n1 * n2
    return area

def part2_solve(data):
    length = 0
    for i in data:
        l, w, h = [int(k) for k in i.split('x')]    
        n1, n2 = find_small([l, w, h])
        length += 2 * (n1 + n2) + l * w * h
        
    return length

print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))

    