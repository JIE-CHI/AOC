# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-03 23:53:18
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-04 12:50:26
class line2d:
    def __init__(self, x, y, dx, dy) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def cal_slop(self):
        k = self.dy / self.dx
        b = self.y - k * self.x
        return k,b

t1 = 200000000000000
t2 = 400000000000000

def cross(k1,b1, k2, b2,x1,x2,dx1,dx2):
    if k1 == k2:
        return False
    else:
        x = (b2 - b1)/(k1 - k2)
        y = k1 * x + b1
        if not (t1 <= x <= t2 and t1 <= y <= t2):
            return False
        return (0 >= dx1 * (x1 - x) and 0 >= dx2 * (x2 - x))



hailstones = []
with open('inputs/day24.txt') as f:
    for line in f:
        p, dp = line.split('@')
        x,y,z = map(int, p.split(','))
        dx, dy, dz = map(int, dp.split(','))
        hailstones.append((x,y,z,dx,dy,dz))

p1 = 0
for i, (x1,y1,z1,dx1,dy1,dz1) in enumerate(hailstones[0:-1]):
    k1,b1 = line2d(x1,y1,dx1,dy1).cal_slop()
    for i2, (x2,y2,z2,dx2,dy2,dz2) in enumerate(hailstones[i+1::]):
        k2,b2 = line2d(x2,y2,dx2,dy2).cal_slop()
        if cross(k1,b1,k2,b2,x1,x2,dx1,dx2):
            p1 += 1
print(p1)

import sympy
x,y,z,dx,dy,dz = sympy.symbols('x,y,z,dx,dy,dz')
eqs = []
for i,  (x1,y1,z1,dx1,dy1,dz1) in enumerate(hailstones):
    eqs.append((x - x1) * (dy - dy1) - (y-y1)* (dx - dx1))
    eqs.append((y-y1) * (dz - dz1) - (z-z1)* (dy - dy1))
    if i > 2:
        ans = [sol for sol in sympy.solve(eqs)]
        if len(ans) == 1:
            print(ans)
            break
ans = ans[0]
print(ans[x] + ans[y] + ans[z])