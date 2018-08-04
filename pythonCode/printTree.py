# -*- coding:utf-8 -*-
from __future__ import print_function


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderRecursive(root):
    if not root:
        return
    print(root.val)
    preOrderRecursive(root.left)
    preOrderRecursive(root.right)


def preOrder(root):
    if not root:
        return
    temp_stack = []
    temp_stack.append(root)
    while temp_stack:
        temp_node = temp_stack.pop(-1)
        print(temp_node.val)
        if temp_node.right:
            temp_stack.append(temp_node.right)
        if temp_node.left:
            temp_stack.append(temp_node.left)
    return


def midOrderRecursive(root):
    if not root:
        return
    midOrderRecursive(root.left)
    print(root.val)
    midOrderRecursive(root.right)


def midOrder(root):
    if not root:
        return
    temp_stack = []
    temp_node = root
    while temp_node or temp_stack:
        while temp_node:
            temp_stack.append(temp_node)
            temp_node = temp_node.left
        temp_node = temp_stack.pop(-1)
        print(temp_node.val)
        temp_node = temp_node.right


def endOrderRecursive(root):
    if not root:
        return
    else:
        endOrderRecursive(root.left)
        endOrderRecursive(root.right)
        print(root.val)


def endOrder(root):
    if not root:
        return
    temp_stack1 = [root]
    temp_stack2 = []
    while temp_stack1:
        temp_node = temp_stack1.pop(-1)
        if temp_node.left:
            temp_stack1.append(temp_node.left)
        if temp_node.right:
            temp_stack1.append(temp_node.right)
        temp_stack2.append(temp_node)
    while temp_stack2:
        print(temp_stack2.pop(-1).val)


def levelOrder(root):
    if not root:
        return
    stack_1 = []
    stack_2 = []
    stack_1.append(root)
    while stack_1:
        while stack_1:
            temp_node = stack_1.pop(0)
            print(temp_node.val)
            if temp_node.left:
                stack_2.append(temp_node.left)
            if temp_node.right:
                stack_2.append(temp_node.right)
        stack_1 = stack_2
        stack_2 = []


if __name__ == "__main__":
    tree_node_1 = TreeNode(1)
    tree_node_2 = TreeNode(2)
    tree_node_3 = TreeNode(3)
    tree_node_4 = TreeNode(4)
    tree_node_5 = TreeNode(5)
    tree_node_6 = TreeNode(6)
    tree_node_7 = TreeNode(7)
    tree_node_8 = TreeNode(8)

    tree_node_1.left = tree_node_2
    tree_node_1.right = tree_node_3
    tree_node_2.left = tree_node_4
    tree_node_2.right = tree_node_5
    tree_node_3.left = tree_node_7
    tree_node_3.right = tree_node_8

    levelOrder(tree_node_1)
