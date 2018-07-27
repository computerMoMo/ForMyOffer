# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        first_stack = []
        second_stack = []
        result_list = []
        first_stack.append(root)
        while first_stack:
            while first_stack:
                temp_node = first_stack.pop(0)
                result_list.append(temp_node.val)
                if temp_node.left:
                    second_stack.append(temp_node.left)
                if temp_node.right:
                    second_stack.append(temp_node.right)
            first_stack = second_stack
            second_stack = []
        return result_list
    