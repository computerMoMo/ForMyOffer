# -*- coding:utf-8 -*-
class Solution:
    def product(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        elif number == 4:
            return 4
        else:
            best_product = []
            best_product.append(0)
            best_product.append(1)
            best_product.append(2)
            best_product.append(3)
            for num in range(4, number+1):
                temp_max = 0
                best_product.append(temp_max)
                for i in range(1, num//2+1):
                    temp_res = best_product[i]*best_product[num-i]
                    # print temp_res, i, num-i
                    if temp_res > temp_max:
                        temp_max = temp_res
                        best_product[num] = temp_max
            # print best_product
            return best_product[number]


if __name__ == "__main__":
    print Solution().product(9)
