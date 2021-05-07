#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 08:12:49 2021

@author: xs0004173
"""

#Q1

a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1]
c = [5,4,-1,7,8]
d = [-1,2,3]
e = [-1,-1,2,2]


def maxSubArray(nums:list)-> int:
    
    mid = int(len(nums)/2)
    #迭代次數
    k = 0
    ans = myFunction(nums, mid, k)
    return sum(ans)

def myFunction(nums: list, mid: int, k: int)-> list:
        print("-----------------------------------------")
        print(nums)
        leftSum = 0
        rightSum = 0
        leftSum = sum(nums[0:mid])
        rightSum = sum(nums[mid+1::])
        
        newLeft = leftSum + nums[mid]
        newRight = rightSum + nums[mid]
        
        if k == len(nums):
            return nums
        elif len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        elif len(nums) == 2:
            if nums[0] < 0:
                return nums[1]
            elif nums[1] < 0:
                return nums[0]
            else:
                return nums
        elif mid == 0:
            return nums
        else:
            if leftSum <= 0 or newLeft <= 0 or newLeft <= nums[mid]:
                nums.pop(0)
            if rightSum <= 0 or newRight <= 0 or newRight <= nums[mid]:
                nums.pop()
            if newLeft > 0 and newRight > 0:
                return myFunction(nums, int(len(nums)/2)-1, k+1)
            
        return myFunction(nums, int(len(nums)/2), k)

print(maxSubArray(c))

#Q2
class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        
        temp = s.split()
        length = len(temp)
        if length == 0:
            return length
        else:
            return len(temp[length-1])

    
    