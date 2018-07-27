# -*- coding:utf-8 -*-
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path_list = []

    def FindPath(self, root, expectNumber):
        # write code here
        current_path = []
        self.depthFirst(root, current_path, expectNumber)
        temp_path_list = sorted(self.path_list, key=lambda x: len(x), reverse=True)
        return temp_path_list

    def depthFirst(self, node, current_path_list, expectNumber):
        if not node:
            return
        current_path_list.append(node.val)
        if not node.right and not node.left:
            if sum(current_path_list) == expectNumber:
                self.path_list.append(current_path_list)
            return
        else:
            self.depthFirst(node.left, copy.deepcopy(current_path_list), expectNumber)
            self.depthFirst(node.right, copy.deepcopy(current_path_list), expectNumber)
            return


if __name__ == "__main__":
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(3)
    treeNode4 = TreeNode(4)
    treeNode5 = TreeNode(5)
    treeNode6 = TreeNode(6)
    treeNode7 = TreeNode(7)

    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeNode6
    treeNode3.right = treeNode7

    print Solution().FindPath(treeNode1, 7)