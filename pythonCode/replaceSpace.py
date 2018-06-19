# -*- coding:utf-8 -*-
import sys
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        space_num = s.count(" ")
        # print space_num
        temp_array = ["" for _ in range(len(s)+2*space_num)]
        temp_j = len(temp_array)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                temp_array[temp_j] = s[i]
                temp_j -= 1
            else:
                temp_array[temp_j] = "0"
                temp_array[temp_j-1] = "2"
                temp_array[temp_j-2] = "%"
                temp_j -= 3
        return "".join(temp_array)

if __name__ == "__main__":
    mySolution = Solution()
    print mySolution.replaceSpace("fff")
