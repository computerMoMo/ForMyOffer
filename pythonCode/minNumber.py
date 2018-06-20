# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) <=0:
            return 0
        elif rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        else:
            index1 = 0
            index2 = len(rotateArray)-1
            mid = 0
            while rotateArray[index1] >= rotateArray[index2]:
                if index2 - index1 == 1:
                    mid = index2
                    break
                mid = (index1+index2)//2
                if rotateArray[mid] >= rotateArray[index1]:
                    index1 = mid
                elif rotateArray[mid] <= rotateArray[index2]:
                    index2 = mid
                # break
                elif rotateArray[index1] == rotateArray[index2] == rotateArray[mid]:
                    return self.find_by_order(rotateArray[index1:index2])
            return rotateArray[mid]

    def find_by_order(self, array):
        return min(array)

if __name__ == "__main__":
    my_solution = Solution()
    test_array = [3,4,5,1,2]
    print my_solution.minNumberInRotateArray(test_array)