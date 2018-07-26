# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        p1_node = pHead1
        p2_node = pHead2
        temp_head = ListNode(0)
        new_node = temp_head
        while p1_node and p2_node:
            if p1_node.val < p2_node.val:
                new_node.next = p1_node
                p1_node = p1_node.next
            else:
                new_node.next = p2_node
                p2_node = p2_node.next
            new_node = new_node.next
        if p1_node:
            new_node.next = p1_node
        else:
            new_node.next = p2_node
        return temp_head.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node3
    node2.next = node4
    node3.next = node5
    node4.next = node6

    new_node = Solution().Merge(node1, node2)

    temp_node = new_node
    while temp_node:
        print temp_node.val
        temp_node = temp_node.next
