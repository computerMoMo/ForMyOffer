# -*- coding:utf-8 -*-
from __future__ import print_function
import codecs
import sys

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr_array = map(int, raw_input().strip().split(" "))
    k_d = map(int, raw_input().strip().split(" "))
    kk = k_d[0]
    dd = k_d[1]

    max_array = [[0 for _ in range(kk+1)] for _ in range(n+1)]
    min_array = [[0 for _ in range(kk+1)] for _ in range(n+1)]

    for one in range(1, n+1):
        max_array[one][1] = arr_array[one-1]
        min_array[one][1] = arr_array[one-1]

    for k in range(2, kk+1):
        for one in range(k, n+1):
            temp_min = sys.maxint
            temp_max = -sys.maxint
            for left in range(max(k-1, one-dd), one):
                t_max = max(max_array[left][k-1]*arr_array[one-1], min_array[left][k-1]*arr_array[one-1])
                t_min = min(max_array[left][k-1]*arr_array[one-1], min_array[left][k-1]*arr_array[one-1])
                if t_max > temp_max:
                    temp_max = t_max
                if t_min < temp_min:
                    temp_min = t_min
            max_array[one][k] = temp_max
            min_array[one][k] = temp_min
    result = -sys.maxint
    for one in range(kk, n+1):
        if result<max_array[one][kk]:
            result = max_array[one][kk]

    print(result)
