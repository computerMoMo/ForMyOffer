# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [i for i in array]
        for i in range(1, len(array)):
            dp[i] = max(array[i], array[i]+dp[i-1])
        return max(dp)

    def FindGreatestSumOfSubArray2(self, array):
        cur,res = array[0], array[0]
        for i in range(1,len(array)):
            cur = cur+array[i]
            res = max(cur, res)
            if cur < 0:
                cur = 0
        return res