# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if len(s) == 0:
            return s
        # write code here
        str_len = len(s)
        real_n = n % str_len
        temp_s = ["" for _ in range(str_len)]
        for i in range(str_len):
            index = (i-real_n) % str_len
            temp_s[index] = s[i]
        return "".join(temp_s)


if __name__ == "__main__":
    print Solution().LeftRotateString("abc", 1)
