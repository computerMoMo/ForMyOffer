# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size==0 or size>len(num):
            return []
        res = []
        cur_max = max(num[:size])
        res.append(cur_max)

        for i in range(0, len(num)-size):
            if num[i] == cur_max:
                cur_max = max(num[i+1:i+1+size])
            elif num[i+size] > cur_max:
                cur_max = num[i+size]
            res.append(cur_max)

        return res