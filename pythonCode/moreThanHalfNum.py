# -*- coding:utf-8 -*-
from __future__ import print_function


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers) == 0:
            return 0
        mid = len(numbers)//2
        start = 0
        end = len(numbers)-1
        pos = self.partition(numbers, start, end)
        while pos != mid:
            if pos > mid:
                end = pos-1
                pos = self.partition(numbers, start, end)
            else:
                start = pos+1
                pos = self.partition(numbers, start, end)
        temp_num = numbers[mid]
        count = 0
        for item in numbers:
            if item == temp_num:
                count +=1
        if count*2 > len(numbers):
            return temp_num
        else:
            return 0

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


if __name__ == "__main__":
    test_array=[1,2,3,2,2,2,5,4,2]
    print(Solution().MoreThanHalfNum_Solution(test_array))
