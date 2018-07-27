# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        result_list = []
        while 2*start < rows and 2*start<columns:
            end_x = columns-1-start
            end_y = rows-1-start
            self.printCircle(matrix, start, end_x, end_y, result_list)
            start += 1
        return result_list

    def printCircle(self, matrix, start, end_x, end_y, result_list):
        # left to right
        i = start
        while i <= end_x:
            result_list.append(matrix[start][i])
            i += 1
        # up to down
        if start < end_y:
            j = start+1
            while j <= end_y:
                result_list.append(matrix[j][end_x])
                j += 1
        # right to left
        if start < end_y and start < end_x:
            i = end_x-1
            while i >= start:
                result_list.append(matrix[end_y][i])
                i -= 1
        # down to up
        if start < end_y-1 and start < end_x:
            j = end_y-1
            while j > start:
                result_list.append(matrix[j][start])
                j -= 1


if __name__ == "__main__":
    test_array = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

    print Solution().printMatrix(test_array)
