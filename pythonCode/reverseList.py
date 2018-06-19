# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        temp_stack = []
        head_node = listNode
        while head_node:
            temp_stack.append(head_node.val)
            head_node = head_node.next
        # while temp_stack:
        #     print temp_stack.pop(-1)
        return [temp_stack[i] for i in range(len(temp_stack)-1, -1, -1)]


if __name__ == "__main__":
    test_stack = ListNode(1)
    test_stack.next = ListNode(2)
    test_stack.next.next = ListNode(3)
    my_solution = Solution()
    print my_solution.printListFromTailToHead(test_stack)
