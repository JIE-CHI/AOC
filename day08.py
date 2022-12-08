#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:26:34 2022

@author: jiechi
"""

text = open('inputs/day08.txt').read().strip()
rows = text.split('\n')
arr = []
for row in rows:
    arr.append([int(i) for i in row])

tot = 0
for i in range(len(arr)):
    for k in range(len(arr[0])):
        if i ==0 or k == 0 or i == len(arr)-1 or k == len(arr[0])-1 :
            tot += 1
        else:
            if arr[i][k] > max(arr[i][0:k]) or arr[i][k] > max(arr[i][k+1::]) or  arr[i][k] > max([m[k] for m in arr[0:i]]) or arr[i][k] > max([m[k] for m in arr[i+1::]]):
                tot += 1
print(tot)
            
score_max = 0
for i in range(len(arr)):
    for k in range(len(arr[0])):
        if i ==0 or k == 0 or i == len(arr)-1 or k == len(arr[0])-1 :
            pass
        else:
            for idl, left in enumerate(reversed(arr[i][0:k])):
                if left >= arr[i][k]:
                    break
            for idr, right in enumerate(arr[i][k+1::]):
                if right >= arr[i][k]:
                    break
            for idu, up in enumerate(reversed([m[k] for m in arr[0:i]])):
                if up >= arr[i][k]:
                    break
            for idd, down in enumerate([m[k] for m in arr[i+1::]]):
                if down >= arr[i][k]:
                    break
            if arr[i][k] > max(arr[i][0:k]) or arr[i][k] > max(arr[i][k+1::]) or  arr[i][k] > max([m[k] for m in arr[0:i]]) or arr[i][k] > max([m[k] for m in arr[i+1::]]):
                score_max = max(score_max, (idl+1) * (idr+1) * (idu+1) * (idd+1))

            
print(score_max )  