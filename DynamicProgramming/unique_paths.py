# https://leetcode.com/problems/unique-paths/discuss/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0: return 0
        r,c = m,n
        dp = [[1 for _ in range(c)] for _ in range(r)]
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
