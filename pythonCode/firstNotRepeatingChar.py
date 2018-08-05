# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count_dict = dict()
        for ch in s:
            if ch not in count_dict:
                count_dict[ch] = 1
            else:
                count_dict[ch] += 1
        for i,ch in enumerate(s):
            if count_dict[ch] ==1:
                return i
        return -1
