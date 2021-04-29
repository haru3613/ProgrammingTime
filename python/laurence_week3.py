#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:22:56 2021

@author: xs0004173
"""

#Q1.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

#l1 = ListNode(1, ListNode(2, ListNode(4)))
#l2 = ListNode(1, ListNode(3, ListNode(4)))

class Q1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #共用記憶體位置
        root = ListNode()
        l3 = root
        print("-----------------------------------------")
        while l1 and l2:
            if l1.val <= l2.val:
                print("l1.val = ", l1.val)
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                print("l2.val =", l2.val)
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
            print("l3.val = ", l3.val)
            print("Root.next = ", root.next)
        if l1 == None and l2 != None:
            l3.next = l2
        if l1 != None and l2 == None:
            l3.next = l1
        print("Root.next = ", root.next)
        
#Q2.
class Q2:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
