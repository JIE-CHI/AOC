lines, inst = open('inputs/day22.txt').read().split('\n\n')
lines = lines.split("\n")
X = len(lines)
Y = max(len(line) for line in lines)

grids = []
for x in range(X):
    if len(lines[x]) == Y:
        grids.append(lines[x])
    else:
        grids.append(lines[x] + ' '*(Y-len(lines[x])))

start = (0,0)
#   3
# 2 @  0
#   1
#  

def move_step(grids, start, d):
    x,y = start
    if d == 0:
        while(grids[x][(y+1)%Y] == ' '):
            y += 1
        y += 1
    elif d == 1:
        while(grids[(x+1)%X][y] == ' '):
            x += 1
        x += 1
    elif d == 2:
        while(grids[x][(y-1)%Y] == ' '):
            y -= 1
        y -= 1
    else:
        while(grids[(x-1)%X][y] == ' '):
            x -= 1
        x -= 1       
        
    return x%X,y%Y

def move(grids, start, n, d):
    x,y =start
    for i in range(n):
        next_x, next_y = move_step(grids, (x,y), d)
        if grids[next_x][next_y] != '#':
            x = next_x
            y = next_y
        else:
            break
    return x,y


import re 
inst  =  re.split('(\d+)',inst.strip()) 

d = 0
start = move(grids, start, 1, d)

for i in inst:
    if i.isdigit():
        n = int(i)
        start = move(grids, start, n, d)
    if i == 'L':
        d -= 1
        if d == -1:
            d = 3
    elif i == 'R':
        d += 1
        if d == 4:
            d = 0


p1 = 1000*(start[0] + 1) + 4 * (start[1] + 1) + d
print(p1)