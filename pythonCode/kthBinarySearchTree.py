# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
        self.node = None

    def KthNode(self, pRoot, k):
        # write code here
        self.midOrder(pRoot, k)
        return self.node

    def midOrder(self, root, k):
        if not root:
            return
        self.midOrder(root.left, k)
        self.count += 1
        if self.count == k:
            self.node = root
            return
        self.midOrder(root.right, k)
