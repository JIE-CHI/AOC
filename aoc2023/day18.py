# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-18 13:20:59
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-30 20:46:08
# area = I + 0.5*B - 1
# I + B = area + 1 + 0.5*B
lines = open('inputs/day18.txt').readlines()
inst = [ ]
inst2 = [ ]
for line in lines:
    d,n,c = line.strip().split()
    inst.append((d,int(n)))
    inst2.append((c[-2],int(c[2:-2],16)))

D = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
# 0 means R, 1 means D, 2 means L, and 3 means U.
D2 = {'3':(-1,0), '1':(1,0), '2':(0,-1), '0':(0,1)}
def cal(inst, D):
    S = (0,0)
    b = 0
    ps = [(0,0)]
    for (d,n) in inst:
        d = D[d]
        b += n 
        S = (d[0]*n+S[0], d[1]*n+S[1])
        ps.append(S)
    area = 0
    for i in range(len(ps) - 1):
        (x0,y0) = ps[i]
        (x1,y1) = ps[i+1]
        area += x1 * y0 - x0 * y1
    return area //2 + b // 2 + 1
print(cal(inst,D))
print(cal(inst2,D2))


    





