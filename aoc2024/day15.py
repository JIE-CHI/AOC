#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:52:27 2025

@author: jiechi
"""


import copy
f_in = open('inputs/day15.txt').read()
# f_in = open('test.txt').read()

G = []

for x, line in enumerate(f_in.split("\n\n")[0].split('\n')):
    G.append(list(line))
    if '@' in line:
        state = (x, line.index('@'))

D = {'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
M = list(f_in.split("\n\n")[1].strip())

def move(state, m):
    (x,y) = state
    next_x = x + m[0]
    next_y = y + m[1]
    if G[next_x][next_y] == '.': 
        G[next_x][next_y] = G[x][y]
        G[x][y] = '.'
         
        return True
    if G[next_x][next_y] == '#':
        return False
    if G[next_x][next_y] == 'O':
        if move((next_x, next_y), m):
            G[next_x][next_y] = G[x][y]
            return True
    if m[0] ==0:
        if move((next_x, next_y), m):
            G[next_x][next_y] = G[x][y]
            return True

    else:
        if G[next_x][next_y] == '[':
            if move((next_x, next_y), m) and move((next_x, next_y+1),m):
                G[next_x][next_y] = G[x][y]
                G[next_x][next_y+1] = '.'
                return True
        if G[next_x][next_y] == ']':
            if move((next_x, next_y), m) and move((next_x, next_y-1),m):
                G[next_x][next_y] = G[x][y]
                G[next_x][next_y-1] = '.'
                return True

    return False
for m in M:
    if m =='\n':
        continue
 
    m = D[m]
    if move(state, m):
        G[state[0]][state[1]] = '.'
        state = (state[0] + m[0], state[1] + m[1])
        G[state[0]][state[1]] = '@'

p1 = 0
for x in range(len(G)):
    for y in range(len(G[0])):
        if G[x][y] == 'O':
            p1 += 100*x + y
print(p1)
            
G = []   
for x, line in enumerate(f_in.split("\n\n")[0].split('\n')):
    new_line = []
    y=0
    for c in line.strip():
        if c=='#':
            new_line.extend(['#', '#'])
            y+=2
        elif c=='O':
            new_line.extend(['[', ']'])
            y+=2
        elif c =='.':
            new_line.extend(['.', '.'])
            y+=2
        elif c =='@':
            new_line.append('@')
            state = (x,y)
            new_line.append('.')
    G.append(new_line)            

for m in M:
    if m =='\n':
        continue
    m = D[m]
    G_back = copy.deepcopy(G)
    if move(state, m):
        G[state[0]][state[1]] = '.'
        state = (state[0] + m[0], state[1] + m[1])
        G[state[0]][state[1]] = '@'
    else:
        G=copy.deepcopy(G_back)
    
    # pg = [''.join(i) for i in G]
    # print(pg)
        
p2 = 0
for x in range(len(G)):
    for y in range(len(G[0])):
        if G[x][y] == '[':
            p2 += 100*x + y
print(p2)
    
    