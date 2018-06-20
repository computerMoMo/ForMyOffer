# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            f_n_1 = 1
            f_n_2 = 0
            f_n = 0
            i = 2
            while i <= n:
                f_n = f_n_1 + f_n_2
                f_n_2 = f_n_1
                f_n_1 = f_n
                i += 1
            return f_n

if __name__ == "__main__":
    print Solution().Fibonacci(39)