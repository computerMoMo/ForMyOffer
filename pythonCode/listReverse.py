# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        newHead = None
        pPrev = None
        pNode = pHead
        while pNode:
            pNext = pNode.next
            if not pNext:
                newHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return newHead