# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-01 13:02:42
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-01 13:27:58
l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
r1 = r2 = 0
with open('inputs/day1.txt') as f:
    for line in f:
        p1 = []
        p2 = []
        for idx, s in enumerate(line):
            if s.isdigit():
                p1.append(int(s))
                p2.append(int(s))
            else:
                for idy, n in enumerate(l):
                    if line[idx::].startswith(n):
                        p2.append(idy+1)
        r1 += p1[0] * 10 + p1[-1]
        r2 += p2[0] * 10 + p2[-1]

print(r1)
print(r2)


        
