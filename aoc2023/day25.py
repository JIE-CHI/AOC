# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2024-01-04 13:00:31
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-04 13:56:32
import networkx as nx
g = nx.Graph()
S = set()
with open('inputs/day25.txt') as f:
    for line in f:
        left, right = line.split(":")
        S.add(left)
        for node in right.strip().split():
            g.add_edge(left, node, capacity = 1.0)
            S.add(node)
for n in S:
    if list(S)[0]!=n:
        cv, ps = nx.minimum_cut(g,list(S)[0],n) 
        if cv == 3:
            print(len(ps[0]) * len(ps[1]))
            break

