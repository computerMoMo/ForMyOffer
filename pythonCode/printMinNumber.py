# -*- coding:utf-8 -*-
class Solution:
    def my_compare(self, a,b):
        sum1 = int(a+b)
        sum2 = int(b+a)
        if sum1>sum2:
            return 1
        elif sum1 == sum2:
            return 0
        else:
            return -1

    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        # write code here
        str_numbers = list(map(str, numbers))
        str_numbers = sorted(str_numbers, cmp=self.my_compare)

        return int("".join(str_numbers))
