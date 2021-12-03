#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:11:42 2021

@author: jiechi
"""
from pandas import read_excel

filepath = './inputs/inputs.xlsx'
sheetname = 'day5'

df = read_excel(filepath, sheet_name=sheetname, header=None) 
data = df.iloc[:,0].values

vowels = 'aeiou'
not_allow = ['ab', 'cd', 'pq', 'xy']

def check_if_nice(string):
    for i in not_allow:
        if i in string:
            return False
    vowel_count = 0
    for i in string:
        if i in vowels:
            vowel_count += 1
            if vowel_count == 3:
                for i in range(len(string)-1):
                    if string[i] == string[i+1]:
                        return True
    return False

def check_if_nice2(string):
    for i in range(len(string)-1):
        pair = string[i:i+2]
        if pair in string[i+2::]:
            for i in range(len(string)-2):
                if string[i] == string[i+2]:
                    return True
    return False


def part1_solve(data):
    res = 0
    for i in data:
        if check_if_nice(i):
            res += 1
    return res

def part2_solve(data):
    res = 0
    for i in data:
        if check_if_nice2(i):
            res += 1
    return res

print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))
