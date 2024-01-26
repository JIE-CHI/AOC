# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-25 15:36:48
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-26 00:22:51


lines = open('inputs/day24.txt').readlines()
up, down, left, right = (set() for _ in range(4))
for x, line in enumerate(lines[1:-1]):
    for y, c in enumerate(line[1:-2]):
        if c == '>':
            right.add((x,y))
        elif c == '<':
            left.add((x,y))
        elif c == '^':
            up.add((x,y))
        elif c == 'v':
            down.add((x,y))

R = len(lines)-2
C = len(lines[0])-3
#up down left right
ds = [(-1,0), (1,0), (0,-1), (0,1), (0,0)]
end = (R, C-1)

import math
lcm = (R*C)//math.gcd(R,C)

from collections import deque

queue = deque([(-1,0, 0,end,0)])

visited = set() 
while queue:
    (x,y,time, end,s) = queue.popleft()
    if (x,y,time%lcm,s) in visited:
        continue
    visited.add((x,y,time%lcm,s))
    if (x,y) == end:
        print(time,s)
        if s == 0:
            s = 1
            end = (-1,0)
        elif s == 1:
            s = 2
            end = (R, C-1)
        else:
            exit(0)
        queue = deque([(x,y, time,end,s)])
    time = time+1
    
    for (dx, dy) in ds: #ds = [(-1,0), (1,0), (0,-1), (0,1)]
        next_x = (x + dx) 
        next_y = (y + dy) 
        if (next_x == -1 and next_y != 0) or (next_x == R and next_y != C-1):
            continue
        if  not(-1 <= next_x <= R and  0 <= next_y < C):
            continue
        if ((next_x - time)%R, next_y) in down or ((next_x + time)%R, next_y) in up or  (next_x,(next_y - time)%C) in right or  (next_x,(next_y + time)%C) in left:
            continue
        else:
            queue.append((next_x, next_y, time, end, s))





