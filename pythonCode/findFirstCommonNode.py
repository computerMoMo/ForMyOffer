# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        # write code here
        len_1 = 0
        p_node = pHead1
        while p_node:
            len_1 += 1
            p_node = p_node.next

        len_2 = 0
        p_node = pHead2
        while p_node:
            len_2 += 1
            p_node = p_node.next
        p1_node = pHead1
        p2_node = pHead2
        if len_1 >= len_2:
            temp_len = len_1-len_2
            for _ in range(0, temp_len):
                p1_node = p1_node.next
        else:
            temp_len = len_2-len_1
            for _ in range(0, temp_len):
                p2_node = p2_node.next

        while p1_node != p2_node:
            p1_node = p1_node.next
            p2_node = p2_node.next
        return p1_node
            
