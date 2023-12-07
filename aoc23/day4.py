# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-04 15:31:02
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-04 15:54:02
p1 = 0
p2 = 0
from collections import defaultdict
copy_cards = defaultdict(int)
with open('inputs/day4.txt') as f:
    for line in f:
        card = int(line.split(':')[0].split()[1])
        wins = line.split(':')[1].split('|')[0]
        nums = line.split(':')[1].split('|')[1]
        nums = nums.split()
        wins = wins.split()
        t = 0
        for i in nums:
            if i in wins:
                t += 1
        if t == 0:
            copy_cards[card] += 1
        else:
            copy_cards[card] += 1
            for i in range(int(t)):
                if card+i+1 < 220:
                    copy_cards[card+i+1] += copy_cards[card] 
            p1 += 2**(t-1)
p2 = sum(copy_cards.values())
print(p1)
print(p2)