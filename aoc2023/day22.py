# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-02 18:54:30
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-03 00:48:04
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
p1 = 0
for i,brick in enumerate(bricks):
    x1,y1,z1 = brick[0]
    x2,y2,z2 = brick[1]
    plane = np.zeros((X+1,Y+1))
    found = True
    for ii, next_brick in enumerate(bricks):
        nextx1,nexty1,nextz1 = next_brick[0]
        nextx2,nexty2,nextz2 = next_brick[1]
        assert nextz2 >= nextz1
        if nextz2 < z2:
            continue
        if nextz1 -1 > z2:
            break
        elif nextz2 == z2 and brick!=next_brick:
            for x in range(nextx1,nextx2+1):
                for y in range(nexty1, nexty2+1):
                    plane[x][y] = 1
           # print(brick, plane)
        elif nextz1 - 1 == z2:
            found = False
            for x in range(nextx1,nextx2+1):
                for y in range(nexty1, nexty2+1):
                    if plane[x][y] == 1:
                        found = True
                        break
            if not found:
                break
    if found:
        p1 += 1

print(p1)


