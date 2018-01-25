# https://leetcode.com/problems/unique-paths-ii/description/

class Solution(object):
    def uniquePathsWithObstacles(self, G):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not G: return 0
        if G[0][0] or G[-1][-1]: return 0
        m, n = len(G), len(G[0])
        dp = [[0 for _ in row] for row in G]
        dp[-1][-1] = 1
        for i in xrange(m-2,-1,-1):
            if not G[i][-1]: dp[i][-1] = dp[i+1][-1]
        for j in xrange(n-2,-1,-1):
            if not G[-1][j]: dp[-1][j] = dp[-1][j+1]
        for i in xrange(m-2,-1,-1):
            for j in xrange(n-2,-1,-1):
                if not G[i][j]: dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
