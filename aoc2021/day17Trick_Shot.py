#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:44:50 2021

@author: jiechi
"""
import math

test = [20, 30, -10, -5]
x1, x2, y1, y2= [119, 176, -141, -84]
n_min = math.floor(math.sqrt(176 * 2)) 

min_x = 0
vx_min, vx_max = [0, x2]
vy_min, vy_max = [y1, -1 * y1 ]
hit = 0
res = 0
for vx in range(vx_min, vx_max+1):
    for vy in range(vy_min, vy_max):
        x = y = 0
        dx, dy = [vx, vy]
        
        y_max = 0
        for _ in range(10000):
            x += dx
            y += dy
            y_max = max(y_max, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                hit += 1
                res = max(y_max, res)
                break
            elif (x < x1 and y < y1) or (x > x2 and y > y2):
                break
            
        
print("*************result for part 1*************")
print(res)
print("*************result for part 2*************")
print(hit)
