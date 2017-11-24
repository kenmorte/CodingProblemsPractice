# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution(object):
    def longestIncreasingPath(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not m: return 0
        dp = [[0 for j in xrange(len(m[i]))] for i in xrange(len(m))]
        res = 0
        for i in xrange(len(m)):
            for j in xrange(len(m[i])):
                res = max(res, self.dfs(i,j,m,dp,float('-inf')))
        return res
        
    def dfs(self, i, j, m, dp, prev):
        if not self.areIndicesValid(i, j, m): return 0
        if m[i][j] <= prev: return 0
        if dp[i][j]: return dp[i][j]
        dp[i][j] = 1 + max(self.dfs(i+1,j,m,dp,m[i][j]),
                          self.dfs(i-1,j,m,dp,m[i][j]),
                          self.dfs(i,j+1,m,dp,m[i][j]),
                          self.dfs(i,j-1,m,dp,m[i][j]))
        return dp[i][j]
        
            
    def areIndicesValid(self, i, j, m):
        return i >= 0 and i < len(m) and j >= 0 and j < len(m[i])
            
            
