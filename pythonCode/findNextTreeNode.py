# -*- coding:utf-8 -*-

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            temp_node = pNode.right
            while temp_node.left:
                temp_node = temp_node.left
            return temp_node
        else:
            while pNode.next:
                preNode = pNode.next
                if preNode.left == pNode:
                    return preNode
                pNode = preNode
            return None
