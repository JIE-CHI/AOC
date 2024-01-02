# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-18 00:02:07
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-29 00:46:19
from collections import deque,defaultdict
lines = open('inputs/day17.txt').readlines()
grids = []
for line in lines:
    grids.append(list(map(int, list(line.strip()))))
R = len(grids)
C = len(grids[0])
S = (0,0)
E = (R-1, C-1)


def travel(queue,cost,max_len,p2=False):
    reverse = (0,0)
    start = False
    ic = -1
    while queue:
        node, ds = queue.popleft()
        (x,y) = node
        assert ds.count(0) >=3
        for ic in range(4):
            if ds[ic] > 0:
                d = [(0,1),(0,-1),(1,0),(-1,0)][ic]
                reverse = (d[0]*-1, d[1]*-1)
                break
            ic = -1
        #right left down up
        if p2 and start and ds[ic] < 4:
            if  0 <= d[0] + x <R and 0<=d[1]+y < C:
                new_ds = ds.copy()
                new_ds[ic] += 1
                if cost[((x+d[0],y+d[1]),tuple(new_ds))] > cost[(node,tuple(ds))] + grids[x+d[0]][y+d[1]]:
                    cost[((x+d[0],y+d[1]),tuple(new_ds))] = cost[(node,tuple(ds))] + grids[x+d[0]][y+d[1]]
                    queue.append(((x+d[0],y+d[1]),new_ds))
        else:
            start = True
            for di,d in enumerate([(0,1),(0,-1),(1,0),(-1,0)]):
                if ds[di] < max_len and 0 <= d[0] + x <R and 0<=d[1]+y < C and d!=reverse:
                    new_ds = ds.copy()
                    new_ds[di] += 1
                    if ic >=0 and ic != di:
                            new_ds[ic] = 0
                    if cost[((x+d[0],y+d[1]),tuple(new_ds))] > cost[(node,tuple(ds))] + grids[x+d[0]][y+d[1]]:
                        cost[((x+d[0],y+d[1]),tuple(new_ds))] = cost[(node,tuple(ds))] + grids[x+d[0]][y+d[1]]
                        queue.append(((x+d[0],y+d[1]),new_ds))
    ans = float('inf')
    for i in cost:
        if i[0] == E:
            if p2:
                for i2 in range(4):
                    if i[1][i2] > 3:
                        ans = min(ans, cost[i])
            else:
                ans = min(ans, cost[i])
    return ans

cost = defaultdict(lambda: float('inf'))
cost[(S,(0,0,0,0))] = 0
queue = deque()
queue.append((S,[0,0,0,0]))
print(travel(queue,cost,3,p2=False))  
cost.clear()
cost[(S,(0,0,0,0))] = 0
queue.clear()
queue.append((S,[0,0,0,0]))
print(travel(queue,cost,10,p2=True))  
