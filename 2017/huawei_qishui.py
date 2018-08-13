# -*- coding:utf-8 -*-
def solution(n):
    return n//2


if __name__ == "__main__":
    n_list = []
    while True:
        try:
            n = int(raw_input().strip())
            if n != 0:
                print solution(n)
            else:
                break
        except:
            break