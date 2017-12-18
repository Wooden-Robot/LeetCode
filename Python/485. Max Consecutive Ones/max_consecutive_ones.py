# -*- coding: utf-8 -*-
# @Time     : 2017/12/18 23:05
# @Author   : woodenrobot


class Solution(object):
    def find_max_consecutive_ones(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        count_list = []
        if 0 not in nums:
            return len(nums)
        elif 1 not in nums:
            return 0
        for n, i in enumerate(nums):
            if i == 1:
                count += 1
            else:
                count_list.append(count)
                count = 0
        count_list.append(count)
        return max(count_list)

    def find_max_consecutive_ones_2(self, nums):
        # 方法2
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = count = 0
        flag = False
        if 0 not in nums:
            return len(nums)
        elif 1 not in nums:
            return 0
        for n, i in enumerate(nums):
            if i == 1:
                count += 1
                if n == len(nums) - 1:
                    max_count = max(max_count, count)
                flag = True
            else:
                if flag:
                    max_count = max(max_count, count)
                    flag = False
                count = 0
        return max_count
