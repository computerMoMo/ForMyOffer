# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        pNode = pHead
        while pNode:
            copyNode = RandomListNode(pNode.label)
            copyNode.next = pNode.next
            pNode.next = copyNode
            pNode = copyNode.next

        pNode = pHead
        while pNode:
            pNodeRandom = pNode.random
            copyNode = pNode.next
            if pNodeRandom:
                copyNode.random = pNodeRandom.next
            pNode = copyNode.next

        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext
        return copyHead


