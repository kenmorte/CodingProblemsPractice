# https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not n: return 0
        if len(n) < 3: return max(n)
        dp = [0 for _ in n]
        dp[0], dp[1] = n[0], max(n[0],n[1])
        for i in range(2,len(n)): 
            dp[i] = max(dp[i-1], n[i] + dp[i-2])
        return dp[-1]
