#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:17:07 2021

@author: jiechi
"""

from pandas import read_excel
import numpy as np
# read input
file_path = './inputs.xlsx'
sheetname = 'day3' 
df = read_excel(file_path, sheet_name = sheetname, header=None)
data = df.iloc[:,0].to_numpy(dtype='str')
# test = np.array(['100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
# data = test

def find_max_length(data):
    length = 0
    for i in data:
        length = max(length, len(i))
    return length


def fill_in_data (data_array, data):
    for i in range(len(data)):
        for j in range(-1, -1*len(data[i])-1, -1):
            data_array[i][j] = int(data[i][j])
    return data_array
                                   

#format the data as libreoffice loses leading zeros
data_array = np.zeros([len(data),find_max_length(data)])
data_array = fill_in_data (data_array, data)


def find_rating (array, ind, flag):
    # flag = True: oxgen, False: co2
    array_sum = np.sum(array,axis = 0)
    if (array_sum[ind] >= len(array)/2):
        if flag:
            keep = 1
        else:
            keep = 0
    else:
        if flag:
            keep = 0
        else:
            keep = 1
    if len(array[np.where(array[:,ind] == keep)])>1:
        return find_rating (array[np.where(array[:,ind] == keep)], ind+1, flag)
    else:
        dec = 0
        for i in array[np.where(array[:,ind] == keep)][0]:
            dec = dec*2 + i
        return dec

def part1_solve(data_array):
    
    data_sum = np.sum(data_array,axis = 0)
    avg = len(data_array) / 2
    gamma = ''
    epsilon = ''
    for i in data_sum:
        if i > avg:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    return(int(gamma, 2) * int(epsilon, 2))

def part2_solve(data_array):
    oxgen = find_rating(data_array, 0, True)
    co2 = find_rating(data_array, 0, False)
    return int(oxgen * co2)

print("*************result for part 1*************")
print(part1_solve(data_array))
print("*************result for part 2*************")
print(part2_solve(data_array))

