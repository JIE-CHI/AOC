#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:57:22 2021

@author: jiechi
"""

from pandas import read_excel
import numpy as np
filepath = './inputs/inputs.xlsx'
sheetname = 'day7'
df = read_excel(filepath, sheet_name = sheetname, header = None)
instructions = df.iloc()[:,0].values

# test = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'e LSHIFT 2 -> f', 'f RSHIFT 2 -> g', 'NOT g -> h', 'NOT g -> i']
# instructions = test

def rules (logic, inputs):
    if logic == 'OR':
        return inputs[0] | inputs[1]
    elif logic == 'NOT':
        return ~inputs[0]
    elif logic == 'AND':
        return inputs[0] & inputs[1]
    elif logic == 'LSHIFT':
        return inputs[0] << inputs[1]
    elif logic == 'RSHIFT':
        return inputs[0] >> inputs[1]

    

def calculate (booklet, key):

    if key.isdigit():
        return (booklet, np.uint16(key))
    elif len(booklet[key]) == 1:
        _, res = calculate(booklet, booklet[key][0])
        
    elif len(booklet[key]) == 2:
        _, input1 =  calculate(booklet, booklet[key][1])
        res = rules(booklet[key][0], [input1])
      
    elif len(booklet[key]) == 3:
        _, input1 =  calculate(booklet, booklet[key][0])
        _, input2 = calculate(booklet, booklet[key][2])
        res = rules(booklet[key][1], [input1, input2])
    if type(res) == np.uint16:
            booklet[key] = [str(res)]
    return (booklet, res)

def part1_solve(instructions, key):
    booklet = {}
    for inst in instructions:
        left, right = inst.split('->')
        left = left.split()
        right = right.strip()
        booklet.update({right:left})
    return calculate(booklet, 'a')[1]
    

def part2_solve(instructions, key):
    value = part1_solve(instructions, 'a')
    booklet = {}
    for inst in instructions:
        left, right = inst.split('->')
        left = left.split()
        right = right.strip()
        booklet.update({right:left})
    booklet.update({'b':[str(value)]})
    return (calculate(booklet, 'a')[1])
    


print("*************result for part 1*************")
print(part1_solve(instructions, 'a'))
print("*************result for part 2*************")
print(part2_solve(instructions, 'a'))
        
        
    