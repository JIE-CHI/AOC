# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-06 15:27:23
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-06 18:56:11
file = "Time:      7  15   30\nDistance:  9  40  200"
file = "Time:        59     79     65     75 \n Distance:   597   1234   1032   1328"
lines = file.split("\n")
time = lines[0].split()[1::]
time = list(map(int, time))
dist = lines[1].split()[1::]
dist = list(map(int, dist))
import math
p1 = 1
time = [59796575]
dist = [597123410321328]
for t,d in zip(time, dist):
    x2 = (0.5 * (t + (t*t-4*d)**0.5) )
    print(x2)
    if x2 == int(x2):
        x2 = int(x2) - 1
    else:
        x2 = math.floor(x2)
    x1 =  0.5 *(t - (t*t-4*d)**0.5) 
    print(x1)
    if x1 == int(x1):
        x1 = int(x1) + 1
    else:
        x1 = math.ceil(x1)
    x1 = max(0, x1)
    p1 *= (x2 - x1+1)
print(p1)