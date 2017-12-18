# -*- coding: utf-8 -*-
# @Time     : 2017/12/18 22:58
# @Author   : woodenrobot


class Solution(object):
    def array_pair_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        return sum(sorted_nums[::2])
