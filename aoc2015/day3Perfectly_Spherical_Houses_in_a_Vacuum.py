#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:24:38 2021

@author: jiechi
"""

f = open("inputs/day3.txt", 'r')
directions = f.read()

def part1_solve(directions):
    dim1 = 0
    dim2 = 0
    houses = {(0,0):1}
    #directions = '^v^v^v^v^v'
    for i in directions:
        if i == '>':
            dim1 += 1
        elif i == '<':
            dim1 -= 1
        elif i == '^':
            dim2 += 1
        elif i == 'v':
            dim2 -= 1
        if (dim1, dim2) in houses:
            houses[(dim1, dim2)] += 1
        else:
            houses.update({(dim1, dim2):1})
    return(len(houses))

# luckyones = 0
# for key, value in houses.items():
    
#     if value > 1:
#         luckyones += 1
# print(luckyones)

def part2_solve(directions):
    dim1 = [0, 0]
    dim2 = [0, 0]
    #[santa, robo]
    
    houses = {(0,0):2}
    for k, i in enumerate(directions):
        ind = k%2
        if i == '>':
            dim1[ind] += 1
        elif i == '<':
            dim1[ind] -= 1
        elif i == '^':
            dim2[ind] += 1
        elif i == 'v':
            dim2[ind] -= 1
        if (dim1[ind], dim2[ind]) in houses:
            houses[(dim1[ind], dim2[ind])] += 1
        else:
            houses.update({(dim1[ind], dim2[ind]):1})
    return (len(houses))

print("*************result for part 1*************")
print(part1_solve(directions))
print("*************result for part 2*************")
print(part2_solve(directions))