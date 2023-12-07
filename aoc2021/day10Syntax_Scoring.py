#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:22:28 2021

@author: jiechi
"""

f = open('inputs/day10.txt', 'r').read()
lines = f.split('\n')

def part1_solve(lines):
    count = 0
    for line in lines:
        line = line.strip()
        line_track = []
        for idx, char in enumerate(line):
            if char == ')':
                if line_track[-1] == '(':
                    del line_track[-1]
                else:
                    count += 3
                    break
            elif char == '}':
                if line_track[-1] == '{':
                    del line_track[-1]
                else:
                    count += 1197
                    break
            elif char == ']':
                if line_track[-1] == '[':
                    del line_track[-1]
                else:
                    count += 57
                    break
            elif char == '>':
                if line_track[-1] == '<':
                    del line_track[-1]
                else:
                   count += 25137
                   break
            else:
                line_track.append(char)
    return count


def part2_solve(lines):
    count = []
    for line in lines:
        line = line.strip()
        line_track = []
        complete = True
        for idx, char in enumerate(line):
            if char == ')':
                if line_track[-1] == '(':
                    del line_track[-1]
                else:
                    complete = False
                    break
            elif char == '}':
                if line_track[-1] == '{':
                    del line_track[-1]
                else:
                    complete = False
                    break
            elif char == ']':
                if line_track[-1] == '[':
                    del line_track[-1]
                else:
                    complete = False
                    break
            elif char == '>':
                if line_track[-1] == '<':
                    del line_track[-1]
                else:
                    complete = False
                    break
            else:
                line_track.append(char)
        if complete:
            sub = 0
            for i in line_track[::-1]:
                if i == '(':
                    sub = sub * 5 + 1
                elif i == '[':
                    sub = sub * 5 + 2
                elif i == '{':
                    sub = sub * 5 + 3
                elif i == '<':
                    sub = sub * 5 + 4
            count.append(sub)       
    return sorted(count)[(len(count)+1) // 2]

              
print("*************result for part 1*************")
print(part1_solve(lines))
print("*************result for part 2*************")
print(part2_solve(lines))
                         
