# -*- coding:utf-8 -*-
from __future__ import print_function


def calculate(x, y, i, j, sum_matrix):
    return sum_matrix[x][y]-sum_matrix[x][j]-sum_matrix[i][y]+sum_matrix[i][j]


def judge(x, n,m, sum_matrix):
    for i in range(1,m-2):
        for j in range(i+1, m-1):
            for k in range(j+1, m):
                last, cnt = 0, 0
                for r in range(1, n + 1):
                    s1 = calculate(r, i, last, 0, sum_matrix)
                    s2 = calculate(r, j, last, i, sum_matrix)
                    s3 = calculate(r, k, last, j, sum_matrix)
                    s4 = calculate(r, m, last, k, sum_matrix)
                    if s1 >= x and s2 >= x and s3 >= x and s4 >= x:
                        last = r
                        cnt += 1
                if cnt >= 4:
                    return True


if __name__ == "__main__":
    mn_str = raw_input().strip().split(" ")
    n = int(mn_str[0])
    m = int(mn_str[1])
    land = [[int(x) for x in raw_input().strip()] for i in range(n)]
    sum_matrix = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + land[i - 1][j - 1]
    l, ans = 0, 0

    s = sum_matrix[n][m]
    while l <= s:
        x = int((l + s) / 2)
        if judge(x, n, m, sum_matrix):
            l = x + 1
            ans = x
        else:
            s = x - 1
    print(ans)
