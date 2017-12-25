# -*- coding: utf-8 -*-
# @Time     : 2017/12/21 13:26
# @Author   : woodenrobot


class Solution(object):
    def min_cost_climbing_stairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost1 = cost[0]
        cost2 = cost[1]
        for i in range(2, len(cost)):
            cost1, cost2 = cost2, cost[i] + min(cost1, cost2)
        return min(cost1, cost2)

    def min_cost_climbing_stairs_2(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n + 1
        for i in xrange(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
