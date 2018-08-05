# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result = []

    def Permutation(self, ss):
        # write code here
        self.full_permutation(list(ss), 0, len(ss)-1)
        return sorted(self.result)

    # 产生全排列
    def get_permutation(self, pre_str, cur_ss):
        if len(cur_ss) == 1:
            if pre_str+cur_ss not in self.result:
                self.result.append(pre_str+cur_ss)
            return
        else:
            for i in range(len(cur_ss)):
                temp_list = list(cur_ss)
                temp_list.pop(i)
                self.get_permutation(pre_str+cur_ss[i], "".join(temp_list))

    def swap(self, ss_list, index_a, index_b):
        temp = ss_list[index_a]
        ss_list[index_a] = ss_list[index_b]
        ss_list[index_b] = temp

    def judge_swap(self, ss_list, index_a, index_b):
        for i in range(index_a, index_b):
            if ss_list[i] == ss_list[index_b]:
                return False
        return True

    def full_permutation(self, str_list, begin, end):
        if begin == end:
            self.result.append("".join(str_list))
            return
        else:
            for i in range(begin, end+1):
                if self.judge_swap(str_list, begin, i):
                    self.swap(str_list, begin, i)
                    self.full_permutation(str_list, begin+1, end)
                    self.swap(str_list, begin, i)


if __name__ == "__main__":
    test_str = "abb"
    test_str_list = list(test_str)
    res = Solution().Permutation(test_str)
    print res