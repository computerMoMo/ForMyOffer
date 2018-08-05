# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result_list = []
        for i in range(1, tsum//2+1):
            temp_sum = 0
            for j in range(i, tsum//2+2):
                temp_sum += j
                if temp_sum == tsum:
                    result_list.append(list(range(i, j+1)))
                    break
                if temp_sum > tsum:
                    break
        return result_list


if __name__ == "__main__":
    print Solution().FindContinuousSequence(100)
