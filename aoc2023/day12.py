# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-12 11:42:32
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-12 17:52:51
lines = open('inputs/day12.txt').readlines()
def dp(symbols, nums, s, n, i, mem):
    if (s,n,i) in mem:
        return mem, mem[(s,n,i)]
    if s == len(symbols):
        if i == 0 and n == len(nums):
            return mem, 1
        elif i==nums[-1] and n == len(nums) -1:
            return mem,1
        else:
            return mem,0
    p = 0
    if symbols[s] in ['#', '?']:
        mem, p0 = dp(symbols, nums, s+1, n, i+1,mem)
        p += p0
    if symbols[s] in ['.', '?']:
        if i == 0:
            mem, p0 = dp(symbols, nums, s+1, n,i,mem)
            p += p0
        elif i > 0 and n < len(nums)  and nums[n] == i:
            mem, p0 = dp(symbols, nums, s+1, n+1, 0, mem)
            p += p0
    mem[(s,n,i)] = p
    return mem, p

p1 = 0
p2 = 0
for line in lines:
    mem = {}
    symbols, nums = line.strip().split()
    nums = nums.split(',')
    nums = list(map(int,nums))
    p1 += dp(symbols, nums, 0, 0, 0, mem)[1]
    mem = {}
    p2 += dp('?'.join([symbols]*5), nums*5, 0, 0, 0, mem)[1]
print(p1)
print(p2)
    
