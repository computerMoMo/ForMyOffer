# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.length = 0

    def Serialize(self, root):
        # write code here
        result_list = []
        self.firstRoot(result_list, root)
        return ",".join(result_list)

    def firstRoot(self, result_list, root):
        if not root:
            result_list.append("#")
            return
        result_list.append(str(root.val))
        self.firstRoot(result_list, root.left)
        self.firstRoot(result_list, root.right)

    def Deserialize(self, s):
        # write code here
        result_list = s.split(",")
        rootNode = self.rebuildFirst(result_list)
        return rootNode

    def rebuildFirst(self, result_list):
        node_val = result_list[self.length]
        self.length += 1
        treeNode = None
        if node_val != "#":
            treeNode = TreeNode(int(node_val))
            treeNode.left = self.rebuildFirst(result_list)
            treeNode.right = self.rebuildFirst(result_list)
        return treeNode


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

    tree_str = Solution().Serialize(treeNode1)
    print tree_str
    print Solution().Deserialize(tree_str).val
