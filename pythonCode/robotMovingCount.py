# -*- coding:utf-8 -*-
class Solution:
    def getDigitSum(self, number):
        total_sum = 0
        while number//10 > 0:
            total_sum += number % 10
            number = number//10
        total_sum += number
        return total_sum

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited_flag = [[False for _ in range(cols)] for _ in range(rows)]
        count = self.moveCount(threshold, rows, cols,0,0,visited_flag)
        return count

    def moveCount(self, threshold, rows, cols, row_id, col_id, visited_flag):
        count = 0
        if self.checkNode(threshold, rows, cols, row_id, col_id, visited_flag):
            visited_flag[row_id][col_id] = True
            count = 1 + self.moveCount(threshold, rows, cols, row_id+1, col_id, visited_flag) + \
                    self.moveCount(threshold, rows, cols, row_id-1, col_id, visited_flag) + \
                    self.moveCount(threshold, rows, cols, row_id, col_id+1, visited_flag) + \
                    self.moveCount(threshold, rows, cols, row_id, col_id-1, visited_flag)
            return count
        return count

    def checkNode(self, threshold, rows, cols, row_id, col_id, visited_flag):
        if 0<=row_id<rows and 0<=col_id<cols and not visited_flag[row_id][col_id] \
                and (self.getDigitSum(row_id)+self.getDigitSum(col_id))<=threshold:
            return True
        return False


if __name__ == "__main__":
    print Solution().movingCount(345)
