# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-02 12:32:26
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-02 12:52:16
goal = {'red':12, 'green':13, 'blue':14}
p1 = 0
p2 = 0
with open('inputs/day2.txt') as f:
    for line in f:
        game = int(line.split(':')[0].split()[1])
        sets = line.split(':')[1].split(';')
        r = g = b = 0
        for s in sets:
            items = s.split(',')
            for i in items:
                n,c = i.split()
                n = int(n)
                if n > goal[c]:
                    game = 0
                if c == 'red':
                    r = max(r,n)
                elif c == 'green':
                    g = max(g,n)
                elif c == 'blue':
                    b = max(b,n)
            
        p1 += game
        p2 += r * g * b
print(p1)
print(p2)
                