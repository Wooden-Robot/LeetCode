# -*- coding: utf-8 -*-
# @Time     : 2017/12/18 23:48
# @Author   : woodenrobot


class Solution(object):
    def find_disappeared_numbers_shit(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return []
        sorted_nums = sorted(nums)
        set_nums = set(sorted_nums)
        if len(set_nums) == 1:
            num = sorted_nums[0] + 1
            if num > len(nums):
                num = sorted_nums[0] - 1
            return [num]
        p_nums = [i for i in range(1, len(nums) + 1)]
        return list(set(p_nums) - set_nums)

    def find_disappeared_numbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        set_nums = set(nums)
        disappear_nums = []
        for i in range(1, length + 1):
            if i not in set_nums:
                disappear_nums.append(i)
        return disappear_nums
