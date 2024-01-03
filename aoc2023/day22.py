# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-02 18:54:30
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-03 14:30:04
from collections import deque

bricks = []
with open('inputs/day22.txt') as f:
    for line in f:
        brick = []
        for xyz in line.strip().split('~'):
            x,y,z = map(int, xyz.split(','))
            brick.append((x,y,z))
        bricks.append(brick)
bricks = sorted(bricks, key=lambda x: x[0][2])
X = max([max(x[0][0], x[1][0]) for x in bricks])
Y = max([max(x[0][1], x[1][1]) for x in bricks])
import numpy as np
current = np.zeros((X+1,Y+1))

def fall(brick, current):
    x1,y1,z1 = brick[0]
    x2,y2,z2 = brick[1]
    if x1 == x2 and y1 == y2:
        cz = current[x1][y1] 
    elif x1 == x2:
        cz = max(current[x1][y1:y2+1])
    else:
        cz = max(current[x1:x2+1][:,y1])
    diff = z1 - cz - 1
    brick[0] =  (x1, y1, z1-diff)
    brick[1] = (x2, y2 , z2- diff)
    for x in range(x1,x2+1):
        for y in range(y1, y2+1):
            current[x][y] = brick[1][2]
    return current, brick

for i,brick in enumerate(bricks):
    current, bricks[i] = fall(brick, current)
bricks = sorted(bricks, key=lambda x: x[0][2])    

from collections import defaultdict
brick_support = defaultdict(set)
support_brick = defaultdict(set)
for i,brick in enumerate(bricks[0:-1]):
    x1,y1,z1 = brick[0]
    x2,y2,z2 = brick[1]
    for next_brick in bricks[i+1::]:
        nextx1,nexty1,nextz1 = next_brick[0]
        nextx2,nexty2,nextz2 = next_brick[1]
        if nextz1 == z2+1 and max(nextx1,x1) <= min(nextx2,x2) and max(nexty1,y1) <= min(nexty2,y2):
            brick_support[tuple(brick)].add(tuple(next_brick))
            support_brick[tuple(next_brick)].add(tuple(brick))
        elif nextz1 > z2+1:
            break

p1 = 0
for i in bricks:
    i = tuple(i)
    if all(len(support_brick[j]) >1 for j in brick_support[i]):
        p1 += 1
print(p1)

p2 = 0
for i in bricks:
    queue = deque(tuple(i) for j in brick_support[tuple(i)] if len(support_brick[j]) ==1)
    visited = set(queue)
    visited.add(tuple(i))
    while queue:
        brick = queue.popleft()
        for k in brick_support[brick] - visited:
            if support_brick[k] <= visited:
                queue.append(k)
                visited.add(k)
    p2 += len(visited)-1
print(p2)

