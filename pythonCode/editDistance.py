# -*- coding:utf-8 -*-
from __future__ import print_function


def editDistance(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    temp_matrix = [[0 for _ in range(len_b+1)] for _ in range(len_a+1)]

    for j in range(len_b+1):
        temp_matrix[0][j] = j
    for i in range(len_a+1):
        temp_matrix[i][0] = i

    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if str_a[i-1] == str_b[j-1]:
                temp_matrix[i][j] = temp_matrix[i-1][j-1]
            else:
                temp_matrix[i][j] = min(temp_matrix[i-1][j-1], temp_matrix[i-1][j], temp_matrix[i][j-1])+1
    return temp_matrix[len_a][len_b]


if __name__ == "__main__":
    print(editDistance("coffee", "cafe"))
