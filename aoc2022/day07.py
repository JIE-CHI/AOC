#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:56:38 2022

@author: jiechi
"""

text = open('inputs/day07.txt').readlines()
text = [i.strip()  for i in text]
current_path= ''
file_size = {}
def update(path, dir_in):
    if dir_in == '..':
        return '/'.join(path.split('/')[0:-1])
    elif dir_in == '/':
        return ''
    else:
        return path + '/' + dir_in
# get all filesize first to avoid duplicatant
for line in text:
    if line[0] == '$':
        if line.split()[1] == 'cd':
            dir_in = line.split()[-1]
            current_path = update(current_path, dir_in)
    else:
        if line.split()[0] != 'dir':
            size, filename = line.split()
            file_size[current_path + '/' + filename] = int(size)

dir_size = {}
for k, v in file_size.items():
    ds = k.split('/')[0:-1]
    for d in range(len(ds)):
        if '/'.join(ds[0:d+1])  in dir_size:
            dir_size['/'.join(ds[0:d+1])] += v
        else:
            dir_size['/'.join(ds[0:d+1])] = v
tot1 = 0
max_used = 70000000 - 30000000
for i in dir_size:
    if dir_size[i] <= 100000:
        tot1 += dir_size[i]
print (tot1)

delete = dir_size[''] - max_used 
small = max_used
for k,v in dir_size.items():
    if v >= delete:
        small = min(small,v)
print(small)
        