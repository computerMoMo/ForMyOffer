# -*- coding -*-
from __future__ import print_function


def max_value(goods, max_w):
    n = len(goods)
    temp_v = [[0 for _ in range(max_w+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, max_w+1):
            if goods[i-1][1] > w:
                temp_v[i][w] = temp_v[i-1][w]
            else:
                temp_w = goods[i-1][1]
                temp_v[i][w] = max(goods[i-1][0]+temp_v[i-1][w-temp_w], temp_v[i-1][w])

    current_w = max_w
    for i in range(n, 0, -1):
        if goods[i-1][0] == temp_v[i][current_w]-temp_v[i-1][current_w-goods[i-1][1]]:
            print(i)
            current_w -= goods[i-1][1]

    return temp_v[n][max_w]


if __name__ == "__main__":
    goods = [[60, 10], [100, 20], [120, 30]]
    print(max_value(goods, 50))

