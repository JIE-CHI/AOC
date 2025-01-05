#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:20:20 2025

@author: jiechi
"""

A = 729
B = 0
C = 0

program = list(map(int, '0,1,5,4,3,0'.split(',')))
A = 27575648
program = list(map(int, '2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0'.split(',')))
p = 0


def combo(operand, A,B,C):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    else:
        print(operand)
p1 = []
while (p < len(program)):
    ins = program[p]
    operand = program[p+1]
    if ins == 0:
        A = A >> combo(operand, A, B, C)
    elif ins == 1:
        B = B ^ operand
    elif ins == 2:
        B = combo(operand, A, B, C) & 7
    elif ins == 3:
        if A != 0:
            p = operand
            continue
    elif ins == 4:
        B = B ^ C
    elif ins == 5:
        p1.append(str(combo(operand, A, B, C)&7))
    elif ins == 6:
        B = A >> combo(operand, A, B, C)
    elif ins == 7:
        C = A >> combo(operand, A, B, C)    
    p += 2

print(','.join(p1))   


#2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0

def solve(nums, ans):
    if nums == []:
        return ans
    for b in range(8):
        a = ans << 3 | b
        b = a % 8
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        if b % 8 == nums[-1]:
            rest = solve(nums[:-1], a)
            if rest == -1: 
                continue
            return rest
    return -1

print(solve(program,0))
