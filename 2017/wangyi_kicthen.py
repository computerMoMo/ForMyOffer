# -*- coding:utf-8 -*-
from __future__ import print_function
import sys


if __name__ == "__main__":
    temp_list = []

    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        line_list = line.split(" ")
        for item in line_list:
            if item not in temp_list:
                temp_list.append(item)

    print(len(temp_list))