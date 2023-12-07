#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:56:46 2021

@author: jiechi
"""
import itertools


f = open('./inputs/day8.txt', 'r')
lines = f.read().strip().split("\n")
# test = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
# lines =test
display_list = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

len_digit_dict = {}
for i in display_list:
    if len(i) in len_digit_dict:
        len_digit_dict[len(i)].append(i)
    else:
        len_digit_dict.update({len(i):[i]})

unique_digits = [k for k,v in len_digit_dict.items() if len(v) == 1]
# unique_digits = [1, 4, 7, 8]


def part1_solve(lines):
    count = 0
    for line in lines:
        output = line.strip().split('|')[1]        
        for i in output.split():
            if len(i) in unique_digits:
                count += 1
    return count

def check(signals, mapping):
    for signal in signals:
        converted = [mapping[i] for i in signal]
        converted = ''.join(sorted(converted))
        if not converted in display_list:
            return False
    return True
        

def bruteforce (signals):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    possible_maps = itertools.permutations(chars)
    for map_i in possible_maps:
        mapping = {chars[i]:map_i[i] for i in range(len(chars))}
        if check(signals, mapping):
            return mapping
        

#in a brute force way
def part2_solve(lines):
    count = 0
    for line in lines:
        left = line.strip().split('|')[0].split()
        right = line.strip().split('|')[1].split()
        left.extend(right)
        mapping = bruteforce(left)
        temp=''
        for i in right:
            converted = [mapping[char] for char in i]
            converted = ''.join(sorted(converted))
            temp = temp + str(display_list.index(converted))
        count += int(temp)
    return count
            

            
            
print("*************result for part 1*************")
print(part1_solve(lines))
print("*************result for part 2*************")
print(part2_solve(lines))
        