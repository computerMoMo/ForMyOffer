# -*- coding:utf-8 -*-
from __future__ import print_function

if __name__ == "__main__":
    n = int(raw_input().strip())
    value_list = map(int, raw_input().strip().split(" "))

    if sum(value_list) % n !=0:
        print(-1)
    else:
        avg = sum(value_list)/n
        count = 0
        flag = True
        for i in range(n):
            if abs(value_list[i] - avg) %2!=0:
                flag = False
                break
            else:
                if value_list[i]-avg <0:
                    count+=avg-value_list[i]
        if not flag:
            print(-1)
        else:
            print(count // 2)
