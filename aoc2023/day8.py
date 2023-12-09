# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-08 13:22:15
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-09 19:12:58
lines = open('inputs/day8.txt').readlines()
inst = lines[0].strip()
graph = {}
starts = []
for i in lines[2::]:
    i = i.strip()
    k = i.split()[0]
    left = i.split()[2][1:-1]
    right = i.split()[-1][0:-1]
    graph[k] = [left, right]
    if k[-1] == 'A':
        starts.append(k)
d= {'L':0, 'R':1}
def find_steps(start, end):
    i = 0
    p= 0
    while(start != end):
        start = graph[start][d[inst[i]]]
        i += 1
        if i == len(inst):
            i = 0
        p += 1
    return p
print(find_steps('AAA', 'ZZZ'))

min_steps = {}
from math import lcm
p2 = 0
i = 0
while(1):
    flag= False
    for s in range(len(starts)):
        starts[s] = graph[starts[s]][d[inst[i]]]
        if starts[s][-1] == 'Z':
            min_steps[s] = p2+1
        if (len(min_steps)) == len(starts):
            flag = True
            break
    p2 += 1
    i += 1
    if i == len(inst):
        i =0
    if flag:
        break
print(lcm(*min_steps.values()))
