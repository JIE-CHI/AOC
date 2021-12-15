#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:55:56 2021

@author: jiechi
"""

f = open('./inputs/day13.txt', 'r').read()
positions, instructions = f.split('\n\n')
dots = []
for i in positions.split('\n'):
    x,y = map(int, i.split(','))
    dots.append((x,y))

def fold(dots, axis, value):
    new_dots = []
    for i in dots:
        if axis == 'x':
            if i[0] < value:
                new_dots.append(i)
            else:
                new_dots.append((2 * value - i[0], i[1]))
        elif axis == 'y':
            if i[1] < value:
                new_dots.append(i)
            else:
                new_dots.append((i[0], 2 * value - i[1]))
            
    return set(new_dots)                
        

def part1_solve(instructions, dots, p1):
    
    for i in instructions.strip().split('\n'):
        axis, value = i.split('=')
        dots = fold(dots, axis[-1], int(value))
        if p1:
            return len(dots)
    return dots
    

def part2_solve(instructions, dots):
    dots = part1_solve(instructions, dots, False)
    max_x = max_y = 0
    for i in dots:
        max_x = max(max_x, i[0])
        max_y = max(max_y, i[1])
    
    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            if (x,y) in dots:
                line += '*'
            else:
                line += '.'
        print(line)
        
print("*************result for part 1*************")
print(part1_solve(instructions, dots, True))
print("*************result for part 2*************")
part2_solve(instructions, dots)