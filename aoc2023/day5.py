# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-05 10:42:04
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-05 19:39:11
maps = {}
keys = []
# with open('test.txt') as f:
with open('inputs/day5.txt') as f:
    for line in f:
        if line.strip() == '':
            pass
        elif line.startswith('seeds'):
            seeds = line.strip().split()[1::]
            seeds = list(map(int, seeds))
        elif 'map' in line.strip():
            k = line.split()[0]
            maps[k] = {}
            keys.append(k)
        else:
            d,s,l = list(map(int,line.strip().split()))
            maps[k][(s,s+l-1)] = d-s
for k in maps:
    maps[k] = dict(sorted(maps[k].items()))

p1 = p2 =  float('inf')
for i in seeds:
    for k in keys:
       
        prev = None
        for p in maps[k]:
            if p[0] <= i <= p[1]:
                i += maps[k][p]
                break
            elif prev and prev[1] < i < p[0]:
                break
            prev = p
    p1 = min(p1, i)
print(p1)

seed_pair = []
for i,s in enumerate(seeds):
    if i%2 == 0:
        start = s
    else:
        seed_pair.append((start,s))
print(maps)
for pair in seed_pair:
    segs = [(pair[0],sum(pair)-1)]
    print(pair)
    for k in keys:
        print(k)
        segs2 = set()
        for seg in segs:
            print(seg)
            tmp_seg =set()
            s1 = seg[0]
            s2 = seg[1]
            prev = None
            for p in maps[k]:
                if prev and prev[1] < s1 < p[0]:
                    segs2.add((prev[1],p[0]))
                    tmp_seg.add((prev[1],p[0]))
                if p[1] < s1:
                    pass
                elif p[0] > s2:
                    if prev and s2 > prev[1]:
                        segs2.add((prev[1],s2))
                        tmp_seg.add((prev[1],s2))
                        break
                elif s1<= p[0] <= seg[1]:
                    if p[0] > s1:
                        segs2.add((s1, p[0]-1))
                        tmp_seg.add((s1, p[0]-1))
                    if s2 >= p[1]:
                        segs2.add((p[0]+maps[k][p], p[1]+maps[k][p]))
                        tmp_seg.add((p[0]+maps[k][p], p[1]+maps[k][p]))
                        s1 = p[1]+1
                    else:
                        segs2.add((p[0]+maps[k][p],seg[1]+maps[k][p]))
                        tmp_seg.add((p[0]+maps[k][p],seg[1]+maps[k][p]))
                        s1 = seg[1]+1
                elif seg[0]<= p[1] <= seg[1]:
                    segs2.add((seg[0] +maps[k][p], p[1]+maps[k][p]))
                    tmp_seg.add((seg[0] +maps[k][p], p[1]+maps[k][p]))
                    s1 = p[1]+1
                elif p[0] <= s1 <= s2 <= p[1]:
                    segs2.add((s1 +maps[k][p], s2+maps[k][p]))
                    tmp_seg.add((s1 +maps[k][p], s2+maps[k][p]))
                    break
                prev = p
            if len(tmp_seg) == 0:
                segs2.add (seg)
            if s1 >p[1]:
                segs2.add ((s1, s2))
            segs = sorted(list(segs2))
    p2 = min(p2,sorted(segs)[0][0])
print(p2)
