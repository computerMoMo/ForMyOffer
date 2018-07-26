# -*- coding:utf-8 -*-
from __future__ import print_function


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        pLoop = self.getLoopNode(pHead)
        # print(pLoop.val)
        if not pLoop:
            return None
        else:
            pStart = pLoop.next
            loopNum = 1
            while pStart != pLoop:
                loopNum += 1
                pStart = pStart.next
            pFirst = pHead
            pSecond = pHead
            # print(loopNum, pFirst.val, pSecond.val)
            for i in range(loopNum):
                pSecond = pSecond.next
            while pFirst!=pSecond:
                pFirst = pFirst.next
                pSecond = pSecond.next
            return pFirst

    def getLoopNode(self, pHead):
        if not pHead or not pHead.next:
            return None
        pSlow = pHead.next
        pFast = pSlow.next
        while pFast and pSlow:
            if pFast == pSlow:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast.next:
                pFast = pFast.next
        return None


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3

    print(Solution().EntryNodeOfLoop(node1).val)
