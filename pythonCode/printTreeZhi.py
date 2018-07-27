# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        # write code here
        depth = 1
        first_stack = []
        second_stack = []
        print_res = []
        first_stack.append(pRoot)
        while first_stack:
            temp_val = []
            while first_stack:
                temp_node = first_stack.pop(0)
                temp_val.append(temp_node.val)
                if temp_node.left:
                    second_stack.append(temp_node.left)
                if temp_node.right:
                    second_stack.append(temp_node.right)
            if depth % 2 == 0:
                temp_val.reverse()
                print_res.append(temp_val)
            else:
                print_res.append(temp_val)

            first_stack = second_stack
            second_stack = []
            depth += 1
        return print_res


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

    print Solution().Print(treeNode1)

