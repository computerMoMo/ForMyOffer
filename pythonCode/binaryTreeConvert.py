# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.node_array = []

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        self.midOrder(pRootOfTree)
        self.node_array[0].left = None
        self.node_array[-1].right = None
        for i, v in enumerate(self.node_array[:-1]):
            v.right = self.node_array[i+1]
            self.node_array[i+1].left = v
        return self.node_array[0]

    def midOrder(self, root):
        if not root:
            return
        self.midOrder(root.left)
        self.node_array.append(root)
        self.midOrder(root.right)
