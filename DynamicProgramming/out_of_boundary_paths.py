# https://leetcode.com/problems/out-of-boundary-paths/description/

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dfs(m, n, N, i, j, {})
    
    def dfs(self, m, n, N, i, j, dp):
        if i < 0 or i >= m or j < 0 or j >= n: return 1
        if N == 0: return 0
        if (i,j,N) in dp: return dp[(i,j,N)]
        dp[(i,j,N)] = int((
            self.dfs(m,n,N-1,i+1,j,dp) + 
            self.dfs(m,n,N-1,i-1,j,dp) + 
            self.dfs(m,n,N-1,i,j-1,dp) + 
            self.dfs(m,n,N-1,i,j+1,dp)) % (1e9 + 7))
        return dp[(i,j,N)]
