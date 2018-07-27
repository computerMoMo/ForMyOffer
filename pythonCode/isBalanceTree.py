# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        flag, depth = self.getDepth(pRoot)
        return flag

    def getDepth(self, root):
        if not root:
            return True, 0
        left_flag, left_depth = self.getDepth(root.left)
        if not left_flag:
            return False, left_depth+1
        right_flag, right_depth = self.getDepth(root.right)
        if not right_flag:
            return False, right_depth+1

        if abs(right_depth-left_depth) <=1:
            return True, 1+max(left_depth, right_depth)
        else:
            return False, 1+max(left_depth, right_depth)


if __name__ == "__main__":
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(3)
    treeNode4 = TreeNode(4)
    treeNode5 = TreeNode(5)
    treeNode6 = TreeNode(6)

    treeNode1.left = treeNode2
    treeNode1.right = treeNode6
    treeNode2.left = treeNode3
    treeNode2.right = treeNode4
    treeNode3.left = treeNode5

    print Solution().IsBalanced_Solution(treeNode1)