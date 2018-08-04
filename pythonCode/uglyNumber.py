# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 1:
            return index
        t2 = 0
        t3 = 0
        t5 = 0
        temp_num = [1]
        while len(temp_num) < index:
            temp_num.append(min(temp_num[t2]*2, temp_num[t3]*3, temp_num[t5]*5))
            if temp_num[-1] == temp_num[t2]*2:
                t2+=1
            if temp_num[-1] == temp_num[t3]*3:
                t3+=1
            if temp_num[-1] == temp_num[t5]*5:
                t5+=1
        return temp_num[-1]
