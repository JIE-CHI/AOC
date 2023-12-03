# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-03 16:24:17
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-03 17:42:54

grids = []
with open('inputs/day3.txt') as f:
    for line in f:
        line = line.strip()
        t = []
        for i,s in enumerate(line):
            if s == '.':
                t.append( '.')
            else:
                if s.isdigit():
                    t.append(s)
                else:
                    t.append( '*')
        grids.append(t)
def get_num (x,y,grids):
    s = grids[x][y]
    nums = s
    i = y
    start = i
    while(i>0):
        if grids[x][i-1].isdigit():
            nums = grids[x][i-1] + nums
            start = i-1
            i -= 1
        else:
            break
    i = y
    while(i<len(grids[0])-1):
        if grids[x][i+1].isdigit():
            nums += grids[x][i+1]
            i+=1
        else:
            break
    return (int(nums), x, start)
def check_neighbour(x,y,grids):
    nums = []
    if x > 0:
        if grids[x-1][y].isdigit():
            nums.append(get_num (x-1,y,grids))
        else:
            if y > 0 and grids[x-1][y-1].isdigit():
                nums.append(get_num (x-1,y-1,grids))
            if y < len(grids[0])-1 and grids[x-1][y+1].isdigit():
                nums.append( get_num (x-1,y+1,grids))
    if x < len(grids) - 1:
        if grids[x+1][y].isdigit():
            nums.append(get_num (x+1,y,grids))
        else:
            if y > 0 and grids[x+1][y-1].isdigit():
                nums.append(get_num (x+1,y-1,grids))
            if y < len(grids[0])-1 and grids[x+1][y+1].isdigit():
                nums.append(get_num (x+1,y+1,grids))
    if y > 0:
        if grids[x][y-1].isdigit():
            nums.append(get_num (x,y-1,grids))
    if y < len(grids[0]) - 1:
        if grids[x][y+1].isdigit():
            nums.append(get_num (x,y+1,grids))
    return nums
    
visited = []
p1 = 0
p2 = 0
for x,line in enumerate(grids):
    for y,s in enumerate(line):
        if s == '*':
            nums = check_neighbour(x,y,grids)
            if len(nums) == 2:
                p2 += nums[0][0] * nums[1][0]
            for n in nums:
                if (n[1],n[2]) not in visited:
                    visited.append((n[1],n[2]))
                    p1 += n[0]
print(p1)
print(p2)

