# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array
        first_index = 0
        for i in range(len(array)):
            if array[i] % 2 == 0:
                first_index = i
                break
        if first_index == len(array) - 1:
            return array
        second_index = first_index+1
        # print first_index,second_index
        while second_index <= len(array)-1:
            if array[second_index] % 2 == 0:
                second_index += 1
            else:
                temp = array[second_index]
                for i in range(second_index, first_index, -1):
                    array[i] = array[i-1]
                array[first_index] = temp
                first_index = first_index+1
                second_index += 1
            # print array
        return array


if __name__ == "__main__":
    test_array = [1,2,3,4,5,6,7]
    test_array = Solution().reOrderArray(test_array)
    print test_array
