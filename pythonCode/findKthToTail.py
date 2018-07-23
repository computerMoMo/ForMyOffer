# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<=0:
            return None
        if not head:
            return None
        first = head
        tail = head
        # get k
        for i in range(k-1):
            if not tail.next:
                return None
            tail = tail.next
        while tail.next:
            first = first.next
            tail = tail.next
        return first