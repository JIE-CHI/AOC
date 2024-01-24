# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-15 18:38:51
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-17 01:59:36
lines, inst = open('inputs/day22.txt').read().split('\n\n')
lines = lines.split("\n")
X = len(lines)
Y = max(len(line) for line in lines)
grids = []
for x in range(X):
    if len(lines[x]) == Y:
        grids.append(lines[x])
    else:
        grids.append(lines[x] + ' '*(Y-len(lines[x])))

start = (0,0)

def move_step(grids, start, d):
    x,y = start
    if d == 0:
        while(grids[x][(y+1)%Y] == ' '):
            y += 1
        y += 1
    elif d == 1:
        while(grids[(x+1)%X][y] == ' '):
            x += 1
        x += 1
    elif d == 2:
        while(grids[x][(y-1)%Y] == ' '):
            y -= 1
        y -= 1
    else:
        while(grids[(x-1)%X][y] == ' '):
            x -= 1
        x -= 1       
    return x%X,y%Y

def move(grids, start, n, d):
    x,y =start
    for i in range(n):
        next_x, next_y = move_step(grids, (x,y), d)
        if grids[next_x][next_y] != '#':
            x = next_x
            y = next_y
        else:
            break
    return x,y

import re 
inst  =  re.split('(\d+)',inst.strip()) 

d = 0
start = move(grids, start, 1, d)

for i in inst:
    if i.isdigit():
        n = int(i)
        start = move(grids, start, n, d)
    if i == 'L':
        d -= 1
        if d == -1:
            d = 3
    elif i == 'R':
        d += 1
        if d == 4:
            d = 0
p1 = 1000*(start[0] + 1) + 4 * (start[1] + 1) + d
print(p1)


#x1, x2, y1, y2
f1 = (0, 49, 50, 99)
f2 = (50, 99, 50, 99)
f3 = (100, 149, 50, 99)
f4 = (100, 149, 0, 49)
f5 = (150, 199, 0, 49)
f6 = (0, 49, 100, 149)

def edge_check(x,y, d):
    if d == 0:
        if f6[0] <= x <= f6[1] and y == f6[3]:
            y = f3[3] 
            x = f6[1] - x + f3[0]
            d = 2
        elif f2[0] <= x <= f2[1] and y == f2[3]:
            y = x - f2[0] + f6[2]
            x = f6[1] 
            d = 3
        elif f3[0] <=x <= f3[1] and y == f3[3]:
            x = f6[1] - (x - f3[0])
            y = f6[3]
            d = 2
        elif f5[0] <= x <= f5[1] and y == f5[3]:
            y = x - f5[0] + f3[2] 
            x = f3[1] 
            d = 3
        else:
            y += 1
    elif d == 1:
        if x == f5[1] and f5[2] <= y <= f5[3]:
            x = f6[0] 
            y = f6[2] + y
        elif x == f3[1] and f3[2] <= y <= f3[3]:
            x = y - f3[2] +f5[0]
            y = f5[3] 
            d = 2
        elif x == f6[1] and f6[2] <= y <= f6[3]:
            x = y - f6[2] +f2[0]
            y = f2[3] 
            d = 2
        else:
            x += 1
    elif d == 2:
        if f1[0] <= x <= f1[1] and y == f1[2]:
            y = f4[2] 
            x =  f1[1] - x + f4[0]
            d = 0
        elif f2[0] <= x <= f2[1] and y == f2[2]:
            y = x - f2[0] + f4[2]
            x = f4[0] 
            d = 1
        elif f4[0] <= x <= f4[1] and y == f4[2]:
            y = f1[2] 
            x =  f4[1] - x + f1[0]
            d = 0
        elif f5[0] <= x <= f5[1] and y == f5[2]:
            y = x - f5[0] + f1[2] 
            x = f1[0] 
            d = 1
        else:
            y -= 1
    elif d == 3:
        if x == f1[0] and f1[2] <= y <= f1[3]:
            x = y - f1[2] + f5[0]
            y = f5[2] 
            d = 0
        elif x == f6[0] and f6[2] <= y <= f6[3]:
            x = f5[1] 
            y = f5[2] + y - f6[2]
        elif x == f4[0] and f4[2] <= y <= f4[3]:
            x = y - f4[2] + f2[0]
            y = f2[2] 
            d = 0
        else:
            x -= 1
    return x,y,d
def move_cube(grids, start, n, d):
    x,y =start
    for i in range(n):
        next_x, next_y,next_d = edge_check(x,y, d)
        if grids[next_x][next_y] == '.':
            x = next_x
            y = next_y
            d = next_d
        else:
            break
    start = (x,y)
    return start,d


d = 0
start = (0,50)
for i in inst:
    if i.isdigit():
        n = int(i)
        start,d = move_cube(grids, start, n, d)
    elif i == 'L':
        d -= 1
        if d == -1:
            d = 3
    elif i == 'R':
        d += 1
        if d == 4:
            d = 0
p2 = 1000*(start[0] + 1) + 4 * (start[1] + 1) + d
print(p2)
