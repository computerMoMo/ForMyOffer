# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n = int(raw_input().strip())
    number_list = []
    for _ in range(n):
        number_list.append(int(raw_input().strip()))

    number_list = list(set(number_list))

    number_list = sorted(number_list)

    for num in number_list:
        print num
