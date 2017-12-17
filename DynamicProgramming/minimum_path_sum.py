# https://leetcode.com/problems/minimum-path-sum/description/

class Solution(object):
    def minPathSum(self, M):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        T = [[None for _ in M[i]] for i in xrange(len(M))]
        T[-1][-1] = M[-1][-1]
        return self.dfs(0,0,T,M)
    
    def dfs(self, i, j, T, M):
        if i >= len(M) or j >= len(M[i]): return float('inf')
        if T[i][j] is not None: return T[i][j]
        T[i][j] = M[i][j] + min(self.dfs(i+1,j,T,M), self.dfs(i,j+1,T,M))
        return T[i][j]
