# https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        dp = [0 for _ in xrange(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in xrange(3,n+1):
            dp[i] += 2*dp[i-1]
            for j in xrange(2,i): dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
