# -*- coding: utf-8 -*-
# @Author: Jie Chi
# @Date:   2023-12-09 18:44:31
# @Last Modified by:   Jie Chi
# @Last Modified time: 2023-12-09 19:11:24
lines  = open('inputs/day9.txt').readlines()
p1 = p2 = 0
for nums in lines:
    nums = list(map(int, nums.split()))
    first = []
    while(len(set(nums)) != 1):
        p1 += nums[-1]
        first.append(nums[0])
        nums2 = []
        for i in range(len(nums) - 1):
            nums2.append(nums[i+1] - nums[i])
        nums = nums2
    p = nums[0]
    for i in first[::-1]:
        p = i - p
    p2 += p
    p1 += nums[-1]
print(p1)
print(p2)
