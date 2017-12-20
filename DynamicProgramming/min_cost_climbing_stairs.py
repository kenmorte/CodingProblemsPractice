# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution(object):
    def minCostClimbingStairs(self, C):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not C: return 0
        if len(C) < 3: return C[-1]
        dp = [0 for _ in C]
        dp[-1], dp[-2] = C[-1], C[-2]
        for i in xrange(len(C)-3,-1,-1):
            dp[i] = C[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
