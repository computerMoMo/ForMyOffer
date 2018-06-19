# -*- coding:utf-8 -*-
import sys

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        start_i = len(array)-1
        start_j = 0
        while start_i >= 0 and start_j < len(array[0]):
            if array[start_i][start_j] == target:
                return True
            elif array[start_i][start_j] > target:
                start_i -= 1
            else:
                start_j += 1
        return False

if __name__ == "__main__":
    mySolution = Solution()
    test_array = [[2,4,6,8],[10,12,14,16]]
    print mySolution.Find(5,test_array)
