# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-20 20:20:29
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-23 19:43:04
valves = {}

with open('inputs/day16.txt') as f:
    for line in f:
        words = line.split()
        left = words[1]
        rate = int(words[4][0:-1].split('=')[1])
        right = []
        for i in words[9::]:
            if ',' in i:
                i = i[0:-1]
            right.append(i)
        valves[left] = (rate, right)


from collections import deque
#distance beteen valves
dists = {}
switches = {}
ind = 0
for v in valves:
    if valves[v][0] or v == 'AA':
        dists[v] = {v:0}       
        visited = set()
        visited.add(v)
        queue = deque([(v,0)])
        if v != 'AA':
            switches[v] = ind
            ind += 1
        while queue:
            valve, dist = queue.popleft()
            for neigh in valves[valve][1]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                if valves[neigh][0]:
                    dists[v][neigh] = dist+1
                queue.append((neigh, dist+1))
        del dists[v][v]

cache = {}
        
def dfs(time, v, ss):
    if (time,v,ss) in cache:
        return cache[(time,v,ss)]
    ans = 0
    for neigh in dists[v]:
        bit = 1 << switches[neigh]
        if ss & bit:
            continue
        time_next = time - dists[v][neigh] - 1
        if time_next <= 0:
            continue
        ans = max(ans, time_next * valves[neigh][0] + dfs(time_next, neigh, ss|bit)) 
    cache [(time, v, ss)] = ans
    return ans
print(dfs(30, 'AA', 0))
p2 = 0
all_s = (1 << len(switches)) - 1
for m in range(all_s//2):
    n = all_s ^ m
    p2 = max(p2, dfs(26, 'AA', m) + dfs(26, 'AA', n))
print(p2)
# from itertools import product
# all_s = list(product([0, 1], repeat=len(switches)))
# print(len(all_s))

# p2 = 0
# for m in range(len(all_s)):
#     n = len(all_s) - m - 1
#     if m %1000 == 0:
#         print(m)
#     if m > n:
#         break
#     p2 = max(p2, dfs(26, 'AA', list(all_s[m])) + dfs(26, 'AA', list(all_s[n])))  
# print(p2)

