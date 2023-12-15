strings = open('inputs/day15.txt').read()
seqs = strings.strip().split(',')

def hash_f(s):
    a = 0
    for i in s:
        a += ord(i)
        a *= 17
        a %= 256
    return a

p1 = 0
for s in seqs:
    p1 += hash_f(s)
print(p1)

from collections import defaultdict
boxes = defaultdict(lambda: [[],[]])
for s in seqs:
    if '=' in s:
        lab, l = s.split('=')
        b = hash_f(lab)
        try:
            i = boxes[b][0].index(lab) 
            boxes[b][1][i] = int(l)
        except ValueError:
            boxes[b][0].append(lab)
            boxes[b][1].append(int(l))
    else:
        lab = s[0:-1]
        b = hash_f(lab)
        try:
            i = boxes[b][0].index(lab)
            del boxes[b][0][i]
            del boxes[b][1][i]
        except ValueError:
            pass
p2 = 0
for i in range(256):
    for vi,v in enumerate(boxes[i][1]):
        p2 += (i+1) * (vi+1)*v
print(p2)


