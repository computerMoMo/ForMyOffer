# -*- coding:utf-8 -*-

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k == len(tinput):
            return sorted(tinput)
        if k > len(tinput):
            return []
        if len(tinput) == 0 or k <= 0:
            return []
        # write code here
        start = 0
        end = len(tinput)-1
        pos = self.partition(tinput, start, end)
        while pos != k:
            if pos > k:
                end = pos-1
                pos = self.partition(tinput, start, end)
            else:
                start = pos+1
                pos = self.partition(tinput, start, end)
        return sorted(tinput[:k])

    def partition(self, array, start, end):
        key = array[start]
        low = start
        high = end
        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] <= key:
                low += 1
            array[high] = array[low]
        array[low] = key
        return low