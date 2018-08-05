# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        forward = [1 for _ in range(len(A))]
        backword = [1 for _ in range(len(A))]
        B = [1 for _ in range(len(A))]

        for i in range(1, len(A)):
            forward[i] = forward[i-1]*A[i-1]
            backword[i] = backword[i-1]*A[len(A)-i]

        for i in range(0, len(A)):
            B[i] = forward[i]*backword[len(A)-i-1]
        return B
