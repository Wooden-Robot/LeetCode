# -*- coding: utf-8 -*-
# @Time     : 2017/12/19 00:25
# @Author   : woodenrobot


class Solution(object):
    def move_zeroes_shit(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_list = []
        while True:
            try:
                nums.remove(0)
                zero_list.append(0)
            except Exception,e:
                break
        nums.extend(zero_list)

    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i in nums:
            if i:
                nums[position] = i
                position += 1
        for i in range(position, len(nums) ):
            nums[i] = 0
