# -*- coding:utf-8 -*-
from __future__ import print_function


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root_value = sequence[-1]
        for i in range(0, len(sequence)):
            if sequence[i] > root_value:
                break
        part_index = i
        for i in range(part_index, len(sequence)):
            if sequence[i] < root_value:
                return False
        left = True
        if part_index > 0:
            left = self.VerifySquenceOfBST(sequence[0: part_index])
        right = True
        if part_index < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[part_index:-1])
        return right and left


if __name__ == "__main__":
    test_array = [6, 7]
    print(Solution().VerifySquenceOfBST(test_array))
