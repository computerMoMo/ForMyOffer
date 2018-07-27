# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        first_stack = []
        second_stack = []
        first_stack.append(pRoot)
        depth = 0
        while first_stack:
            depth += 1
            while first_stack:
                temp_node = first_stack.pop(0)
                if temp_node.left:
                    second_stack.append(temp_node.left)
                if temp_node.right:
                    second_stack.append(temp_node.right)
            first_stack = second_stack
            second_stack = []
        return depth