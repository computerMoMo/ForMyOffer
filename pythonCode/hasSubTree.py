# -*- coding:utf-8 -*-
from __future__ import print_function
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False

        # write code here
        equal_flag = False
        if pRoot1.val == pRoot2.val:
            equal_flag = self.CheckTree(pRoot1, pRoot2)
        if not equal_flag:
            equal_flag = self.HasSubtree(pRoot1.left, pRoot2)
        if not equal_flag:
            equal_flag = self.HasSubtree(pRoot1.right, pRoot2)
        return equal_flag

    def CheckTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            return self.CheckTree(pRoot1.left, pRoot2.left) and self.CheckTree(pRoot1.right, pRoot2.right)
        else:
            return False


if __name__ == "__main__":
    tree_node1 = TreeNode(8)
    tree_node2 = TreeNode(8)
    tree_node3 = TreeNode(7)
    tree_node4 = TreeNode(9)
    tree_node5 = TreeNode(2)
    tree_node6 = TreeNode(4)
    tree_node7 = TreeNode(7)

    tree_node1.left = tree_node2
    tree_node1.right = tree_node3
    tree_node2.left = tree_node4
    tree_node2.right = tree_node5
    tree_node5.left = tree_node6
    tree_node5.right = tree_node7

    sub_tree_node1 = TreeNode(8)
    sub_tree_node1.left = TreeNode(9)
    sub_tree_node1.right = TreeNode(2)

    print (Solution().HasSubtree(tree_node1, sub_tree_node1))