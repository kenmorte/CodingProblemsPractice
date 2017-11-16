# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1: return 1
        dp = [1 for _ in range(n+1)]
        for i in range(2,n+1): dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
