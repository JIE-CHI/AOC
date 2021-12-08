#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:39:37 2021

@author: jiechi
"""

from pandas import read_excel

filepath = './inputs/inputs.xlsx'
sheetname = 'day8'
df = read_excel(filepath, sheet_name = sheetname, header = None)
str_list = df.iloc[:,0].values
# test = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
# str_list = test
str_list = [r"{}".format(i) for i in str_list]
def count_charsofcode(string):

    return len(r"{}".format(string)) 
def count_charinmemory(string):
    string = string [1:-1]
    count = 0
    passflag = True
    for char in range(len(string)):
        if string[char] == '\\' and passflag:
            if string[char+1] == '\\' :
                passflag = False
            elif string[char+1] == '\"':
                pass
            elif string[char+1] == 'x':
                count -= 2
            else:
                count += 1
                passflag = True
        else:
            count += 1
            passflag = True
    return count

def count_charencoded(string):
    string = string [1:-1]
    count = 6
    passflag = True
    for char in range(len(string)):
        if string[char] == '\\' and passflag:
            if string[char+1] == '\\' :
                count += 3
                passflag = False
            elif string[char+1] == '\"':
                count += 3
            elif string[char+1] == 'x':
                count += 2
            else:
                count += 1
                passflag = True
        else:
            count += 1
            passflag = True
    return count

def part1_solve(str_list):
    charofcode = 0
    charinmemor = 0
    for i in str_list:
        charofcode += count_charsofcode(i)
        charinmemor += count_charinmemory(i)
    return charofcode-charinmemor
        
def part2_solve(str_list):
    charencoded = 0
    charofcode = 0
    for i in str_list:
        charofcode += count_charsofcode(i)
        charencoded += count_charencoded(i)
    return charencoded-charofcode       
        
print("*************result for part 1*************")
print(part1_solve(str_list))
print("*************result for part 2*************")
print(part2_solve(str_list))
