# -*- coding: utf-8 -*-
# @Time     : 2017/12/19 13:12
# @Author   : woodenrobot


class Solution(object):
    def is_one_bit_character(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        position = 0
        length = len(bits)
        while True:
            if position == length - 2:
                if bits[position]:
                    return False
                else:
                    return True
            elif position == length - 1:
                return True
            if bits[position]:
                position += 2
            else:
                position += 1
