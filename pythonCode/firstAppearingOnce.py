# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count_dict = dict()
        self.char_list = []
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for ch in self.char_list:
            if self.count_dict[ch] == 1:
                return ch
        return "#"

    def Insert(self, char):
        # write code here
        self.char_list.append(char)
        if char not in self.count_dict:
            self.count_dict[char] = 1
        else:
            self.count_dict[char] += 1