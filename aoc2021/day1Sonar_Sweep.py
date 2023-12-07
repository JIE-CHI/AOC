#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:01:27 2021

@author: jiechi
"""

from pandas import read_excel
import numpy as np

# read input
file_path = './inputs/inputs.xlsx'
sheetname = 'day1' 
df = read_excel(file_path, sheet_name = sheetname, header=None)
data = df.iloc[:,0].values
#test = np.array([199,200,208,210,200,207,240,269,260,263])
#data = test

def part1_solve(data):
    prev_data = data[0:-1]
    post_data = data[1::]
    diff = post_data - prev_data
    count=0
    for i in diff:
        if i > 0:
            count += 1
    return(count)

def part2_solve(data):
    #get sum
    data_new = data[0:-2] + data[1:-1] + data[2::]
    return (part1_solve (data_new))

print("*************result for part 1*************")
print(part1_solve(data))
print("*************result for part 2*************")
print(part2_solve(data))


