# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        if not pHead.next:
            return pHead

        new_head = ListNode(0)
        new_head.next = pHead
        pre = new_head
        last = new_head.next
        while last:
            if last.next and last.val == last.next.val:
                while last.next and last.val == last.next.val:
                    last = last.next
                pre.next = last.next
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return new_head.next
