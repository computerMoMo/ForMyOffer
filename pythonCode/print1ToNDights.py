# -*- coding:utf-8 -*-
class Solution:
    def print1ToN(self, n):
        if n <= 0:
            return
        numbers = ['0' for _ in range(n)]
        for i in range(10):
            numbers[0] = str(i)
            self.printRecurisively(numbers, n, 1)

    def printRecurisively(self, numbers, length, index):
        if index == length:
            self.printNumbers(numbers)
            return
        else:
            for i in range(10):
                numbers[index] = str(i)
                self.printRecurisively(numbers, length, index+1)

    def printNumbers(self, numbers):
        if len(numbers) == 1:
            print "".join(numbers)
            return
        start_idx = 0
        for index, items in enumerate(numbers):
            if items != "0":
                start_idx = index
                break
        if start_idx == 0 and numbers[0] == "0":
            print 0
            return
        print "".join(numbers[start_idx:])


if __name__ == "__main__":
    Solution().print1ToN(3)
