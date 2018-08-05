# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        low = 0
        high = len(array)-1
        res = []
        while low < high:
            temp_sum = array[low] + array[high]
            if temp_sum == tsum:
                res.append(array[low])
                res.append(array[high])
                break
            elif temp_sum>tsum:
                high -= 1
            else:
                low += 1
        return res
