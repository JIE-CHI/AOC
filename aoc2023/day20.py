# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-20 14:16:12
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-01 23:48:21
modules = {}
flip = {}
conj = {}

with open('inputs/day20.txt') as f:
    for line in f:
        left,right = line.strip().split(' -> ')
        if left == 'broadcaster':
            modules['S'] = right.split(', ')
        elif left[0] == '%':
            modules[left[1::]] = right.split(', ')
            flip[left[1::]] = -1                
        else:
            modules[left[1::]] = right.split(', ')
            conj[left[1::]] = {}
   
for i in modules:
    for r in modules[i]:
        if r in conj: 
            conj[r][i] = -1 #memory


cycles = {}
low = 0
high = 0
presses = 0
target = [i for i in modules if 'rx' in modules[i]][0]

from collections import deque
import math
while 1:
    if presses == 1000:
        print(low * high)
    queue = deque([(None, 'S',  -1)])#-1 low pulse
    presses += 1
    while queue:
        (recieve, output, pulse) = queue.popleft()
        if output == target and pulse == 1:
            if recieve not in cycles:
                cycles[recieve] = presses
            assert presses  % cycles[recieve] == 0, f"{presses} {cycles[recieve]}"

        if len(cycles) == 4:
            p2 = 1
            for c in cycles.values():
                p2 = math.lcm(c, p2)
            print(p2)
            exit(0)
        if pulse < 0 :
            low += 1
        else:
            high += 1
        if output == 'S':
            for node in modules['S']:
                queue.append((output, node, -1))
        elif output in flip:
            if pulse > 0 :
                continue
            flip[output] *= -1
            for node in modules[output]:
                queue.append((output, node, flip[output]))
        elif output in conj:
            conj[output][recieve] = pulse
            if all(p == 1 for p in conj[output].values()):
                pulse = -1
            else:
                pulse = 1
            for node in modules[output]:
                queue.append((output,node, pulse))