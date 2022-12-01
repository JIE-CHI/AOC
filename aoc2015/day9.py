#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:22:18 2022

@author: jiechi
"""
import itertools

dists = open('inputs/day9.txt').read()
dists = dists.strip().split('\n')
cities = {}
city_list = set()
for i in dists:
    dist = int(i.split(' = ')[-1])
    city1, city2 = i.split(' = ')[0].split(' to ')
    city_list.add(city1)
    city_list.add(city2)
    cities[(city1,city2)] = dist
    cities[(city2,city1)] = dist


possible_routes = list(itertools.permutations(city_list))
possible_dist = []
for route in possible_routes:
    dist = 0
    for m,n in zip(route[0:-1], route[1::]):
        dist += cities[(m,n)]
    possible_dist.append(dist)
possible_dist = sorted(possible_dist)
print(possible_dist[0])
print(possible_dist[-1])
    