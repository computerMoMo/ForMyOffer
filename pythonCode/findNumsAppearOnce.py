# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) == 2:
            return [array[0], array[1]]
        temp_sum = 0
        for item in array:
            temp_sum ^= item
        index = 0
        while temp_sum & 1 == 0:
            temp_sum = temp_sum >> 1
            index += 1
        a = 0
        b = 0
        for item in array:
            if self.judge(item, index):
                a ^= item
            else:
                b ^= item
        return [a,b]

    def judge(self, num, index):
        num = num >> index
        if num & 1 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test_array = [1,2,2,3,5,5]
    print Solution().FindNumsAppearOnce(test_array)
