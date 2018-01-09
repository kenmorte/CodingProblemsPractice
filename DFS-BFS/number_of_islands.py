# https://leetcode.com/problems/number-of-islands/description/

class Solution(object):
    def numIslands(self, M):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not M: return 0
        V = [[False for _ in row] for row in M]
        res = 0
        for i in xrange(len(M)):
            for j in xrange(len(M[i])):
                if M[i][j] == '1' and not V[i][j]:
                    res += 1
                    self.dfs(i,j,M,V)
        return res
        
    def dfs(self, i, j , M, V):
        if i < 0 or i == len(M) or j < 0 or j == len(M[i]): return
        if M[i][j] == '0' or V[i][j]: return
        V[i][j] = True
        self.dfs(i+1, j, M, V)
        self.dfs(i-1, j, M, V)
        self.dfs(i, j-1, M, V)
        self.dfs(i, j+1, M, V)
