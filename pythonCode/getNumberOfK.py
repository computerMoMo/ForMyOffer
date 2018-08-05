# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        low = 0
        high = len(data)-1
        index = -1
        while low <= high:
            mid = (low + high) / 2
            if data[mid] == k:
                index = mid
                break
            elif data[mid] < k:
                low = mid+1
            else:
                high = mid-1
        if index == -1:
            return 0
        else:
            start = index
            i = index
            while i >= 0:
                if data[i] != k:
                    break
                else:
                    start = i
                i -= 1
            end = index
            i = index
            while i < len(data):
                if data[i] != k:
                    break
                else:
                    end = i
                i += 1
            return end-start+1


if __name__ == "__main__":
    test_array = [3]
    print Solution().GetNumberOfK(test_array, 3)
