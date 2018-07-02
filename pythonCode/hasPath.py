# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path or rows<1 or cols<1:
            return False
        temp_matrix = []
        for i in range(0, rows):
            temp_row = list(matrix[i*cols:(i+1)*cols])
            temp_matrix.append(temp_row)
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        path_length = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(temp_matrix, rows, cols, i, j, path, path_length, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, path_length, visited):
        if len(path) == path_length:
            return True
        hasPathFlag = False
        if row>=0 and col>=0 and row < rows and col < cols and not visited[row][col] and matrix[row][col] == path[path_length]:
            path_length += 1
            visited[row][col] = True
            hasPathFlag = self.hasPathCore(matrix, rows, cols, row, col - 1, path, path_length, visited) or \
                          self.hasPathCore(matrix, rows, cols, row, col + 1, path, path_length, visited) or \
                          self.hasPathCore(matrix, rows, cols, row - 1, col, path, path_length, visited) or \
                          self.hasPathCore(matrix, rows, cols, row + 1, col, path, path_length, visited)
            if not hasPathFlag:
                path_length -= 1
                visited[row][col] = False
        return hasPathFlag


if __name__ == "__main__":
    print Solution().hasPath(matrix="ABCESFCSADEE", rows=3, cols=4, path="ABCCED")

