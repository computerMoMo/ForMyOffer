# -*- coding:utf-8 -*-
class Solution:

    def InversePairs(self, data):
        # write code here
        count, new_data = self.merge_sort(data)
        return count%1000000007

    def merge_sort(self, data):
        if len(data) == 1:
            return 0, data
        else:
            mid = len(data)/2
            left_count, left_data = self.merge_sort(data[0:mid])
            right_count, right_data = self.merge_sort(data[mid:])

            temp_data = []
            count = 0
            i = len(left_data)-1
            j = len(right_data)-1
            while i>=0 and j>=0:
                if left_data[i]>right_data[j]:
                    count += j+1
                    temp_data.append(left_data[i])
                    i-=1
                else:
                    temp_data.append(right_data[j])
                    j-=1
            while i>=0:
                temp_data.append(left_data[i])
                i-=1
            while j>=0:
                temp_data.append(right_data[j])
                j-=1
            temp_data.reverse()
            return left_count+right_count+count, temp_data


if __name__ == "__main__":
    test_array = [1,2,3,4,5,6,7,0]
    count = Solution().InversePairs(test_array)

    print count
    print test_array
