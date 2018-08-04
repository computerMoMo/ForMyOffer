# -*- coding:utf-8 -*-
from __future__ import print_function


def maxSubString(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    p = 0
    max_len = 0
    temp_matrix = [[0 for _ in range(len_b + 1)] for _ in range(len_a+1)]

    for i in range(1, len_a+1):
        for j in range(1, len_b + 1):
            if str_a[i-1] == str_b[j-1]:
                temp_matrix[i][j] = temp_matrix[i-1][j-1] + 1
                if temp_matrix[i][j] > max_len:
                    p = i-1
                    max_len = temp_matrix[i][j]
    return max_len, str_a[p-max_len+1:p+1]


def maxSubSequence(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    len_matrix = [[0 for _ in range(len_b + 1)] for _ in range(len_a+1)]
    flag_matrix = [["None" for _ in range(len_b + 1)] for _ in range(len_a+1)]
    for i in range(1, len_a+1):
        for j in range(len_b+1):
            if str_a[i-1] == str_b[j-1]:
                len_matrix[i][j] = len_matrix[i-1][j-1] + 1
                flag_matrix[i][j] = "ok"
            else:
                if len_matrix[i-1][j] > len_matrix[i][j-1]:
                    len_matrix[i][j] = len_matrix[i-1][j]
                    flag_matrix[i][j] = "up"
                else:
                    len_matrix[i][j] = len_matrix[i][j-1]
                    flag_matrix[i][j] = "left"
    max_lens = len_matrix[len_a][len_b]
    temp_s = []
    i = len_a
    j = len_b
    while i > 0 and j>0:

        if flag_matrix[i][j] == "ok":
            temp_s.append(str_a[i-1])
            i -= 1
            j -= 1
        elif flag_matrix[i][j] == "up":
            i -= 1
        elif flag_matrix[i][j] == "left":
            j -= 1
    temp_s.reverse()
    return max_lens, "".join(temp_s)


if __name__ == "__main__":
    print(maxSubSequence('abcdfg', 'abdfg'))
