# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-19 21:03:32
# @Last Modified by:   Jie Chi
# @Last Modified time: 2024-01-01 02:44:44
from collections import deque
import copy
f = open('inputs/day19.txt').read()
rules, parts = f.split("\n\n")
parts = parts.strip().split("\n")
R = {}

def parse_con(s):
    for op in ['>', '<']:
        if op in c:
            left, right = c.split(':')[0].split(op)
            t = c.split(':')[1]
            return (left, op, int(right), t, None)
for r in rules.split("\n"):
    k = r.split('{')[0]
    v = []
    c = r.split('{')[1][0:-1]
    cs = c.split(',')
    for c in cs[0:-1]:
        v.append(parse_con(c))
    vi = parse_con(c)
    vi = (vi[0], vi[1], vi[2], vi[3], cs[-1])
    v[-1] = vi
    R[k] = v

def compare(ri, c):
    (l, op, r, t, f) = ri
    if op == '<':
        return c < r
    else:
        return c > r
            
def workflow(name, cons):
    if name in ['A', 'R']:
        return name == 'A'
    rs = R[name]
    for ri in rs:
        (l, op, r, t, f) = ri
        if compare(ri,cons[l]):
            return workflow(t, cons)
        else:
            if f != None:
                return workflow(f, cons)
    return True
    
p1 = 0
for p in parts:
    cons = {}
    for pi in p[1:-1].split(','):
        l,r = pi.split('=')
        cons[l] = int(r)
    if workflow('in', cons):
        for l in cons:
            p1 += cons[l]
print(p1)

queue = deque()
queue.append(('in',1,4000,1,4000,1,4000,1,4000))
p2 = 0 
while(queue):
    s, xl, xh, ml, mh, al, ah, sl, sh = queue.popleft()
    s_dict = {'x':[xl,xh],'m':[ml,mh],'a':[al,ah],'s':[sl,sh]}
    if s == 'A':
        p2 += (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
    elif s == 'R':
        continue
    else:
        for ss in R[s]:
            (l, op, r, t, f) = ss
            if op == '<':
                s_dict2 = copy.deepcopy(s_dict)
                if s_dict[l][0] <= r-1 <= s_dict[l][1] :
                    s_dict2[l][1] = r-1
                    queue.append((t,s_dict2['x'][0],s_dict2['x'][1],s_dict2['m'][0],s_dict2['m'][1],s_dict2['a'][0],s_dict2['a'][1],s_dict2['s'][0],s_dict2['s'][1]))
                    if f:
                        s_dict2 = copy.deepcopy(s_dict)
                        s_dict2[l][0] = r
                        queue.append((f,s_dict2['x'][0],s_dict2['x'][1],s_dict2['m'][0],s_dict2['m'][1],s_dict2['a'][0],s_dict2['a'][1],s_dict2['s'][0],s_dict2['s'][1]))
                    else:
                        s_dict[l][0] = r

            else:
                s_dict2 = copy.deepcopy(s_dict)
                if s_dict[l][0] <= r < s_dict[l][1] :
                    s_dict2[l][0] = r+1
                    queue.append((t,s_dict2['x'][0],s_dict2['x'][1],s_dict2['m'][0],s_dict2['m'][1],s_dict2['a'][0],s_dict2['a'][1],s_dict2['s'][0],s_dict2['s'][1]))
                    if f:
                        s_dict2 = copy.deepcopy(s_dict)
                        s_dict2[l][1] = r
                        queue.append((f,s_dict2['x'][0],s_dict2['x'][1],s_dict2['m'][0],s_dict2['m'][1],s_dict2['a'][0],s_dict2['a'][1],s_dict2['s'][0],s_dict2['s'][1]))
                    else:
                        s_dict[l][1] = r
print(p2)
                

