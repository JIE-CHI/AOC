# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-07 11:17:08
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-07 12:36:50
bids = {}
cards = {'high':[], 'one':[], 'two':[], 'three':[], 'full':[], 'four':[], 'five':[]}
cards2 = {'high':[], 'one':[], 'two':[], 'three':[], 'full':[], 'four':[], 'five':[]}

from collections import Counter
with open('inputs/day7.txt') as f:
    for line in f:
        c, s = line.split()
        bids[c] = int(s)
        counter = Counter(list(c))
        if len(counter) == 1:
            cards['five'].append(c)
            cards2['five'].append(c)
        elif len(counter) == 2:
            if counter.most_common(1)[0][1] == 4:
                cards['four'].append(c)
                if 'J' in c:
                    cards2['five'].append(c)
                else:
                    cards2['four'].append(c)
            else:
                cards['full'].append(c)
                if 'J' in c:
                    cards2['five'].append(c)
                else:
                    cards2['full'].append(c)
        elif len(counter) == 3:
            if counter.most_common(1)[0][1] == 3:
                cards['three'].append(c)
                if  'J' in c:
                    cards2['four'].append(c)
                else:
                    cards2['three'].append(c)
            else:
                cards['two'].append(c)
                if counter['J'] == 2:
                    cards2['four'].append(c)
                elif counter['J'] == 1:
                    cards2['full'].append(c)
                else:
                    cards2['two'].append(c)
        elif len(counter)==4:
            cards['one'].append(c)
            if 'J' in c:
                cards2['three'].append(c)
            else:
                cards2['one'].append(c)
        else:
            cards['high'].append(c)
            if 'J' in c:
                cards2['one'].append(c)
            else:
                cards2['high'].append(c)

seq = '23456789TJQKA'
seq2 = 'J23456789TQKA'
rank = 1
p1 = 0
for h in cards:
    cards[h] = sorted(cards[h], key=lambda x: [seq.index(c) for c in x])
    for c in cards[h]:
        p1 += bids[c] * rank
        rank += 1
print(p1)
rank = 1
p2 = 0
for h in cards2:
    cards2[h] = sorted(cards2[h], key=lambda x: [seq2.index(c) for c in x])
    for c in cards2[h]:
        p2 += bids[c] * rank
        rank += 1
print(p2)