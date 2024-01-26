# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-25 15:37:04
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-26 01:01:39


lines = open('inputs/day25.txt').readlines()

#2,1,0,-,=
s2i = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
i2s = {2:'2', 1:'1', 0:'0', -1:'-', -2:'='}
tot = 0
for line in lines:
    line = line.strip()
    l = len(line)-1
    temp = 0
    for c in line:
        temp += 5**l * s2i[c]
        l -= 1
    tot += temp
print(tot)

ans = ''
while tot:
    rem = tot%5
    tot = tot//5
    if rem < 3:
        ans = i2s[rem] + ans
    else:
        tot +=1
        ans = i2s[rem - 5] + ans
print(ans)

