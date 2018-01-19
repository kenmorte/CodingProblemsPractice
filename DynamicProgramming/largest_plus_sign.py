# https://leetcode.com/problems/largest-plus-sign/description/

class Solution(object):
    def orderOfLargestPlusSign(self, N, M):
        B = [[1 for _ in xrange(N)] for _ in xrange(N)]
        for m in M:
            r, c = tuple(m)
            B[r][c] = 0
            
        U = [list(r) for r in B]
        D = [list(r) for r in B]
        L = [list(r) for r in B]
        R = [list(r) for r in B]
        
        for i in xrange(1,N):
            for j in xrange(N):
                if U[i][j]: U[i][j] += U[i-1][j]
        for i in xrange(N-2,-1,-1):
            for j in xrange(N):
                if D[i][j]: D[i][j] += D[i+1][j]      
        for i in xrange(N):
            for j in xrange(1,N):
                if L[i][j]: L[i][j] += L[i][j-1]
        for i in xrange(N):
            for j in xrange(N-2,-1,-1):
                if R[i][j]: R[i][j] += R[i][j+1]
        res = 0
        for i in xrange(N):
            for j in xrange(N):
                if B[i][j]: res = max(res, min(U[i][j], D[i][j], L[i][j], R[i][j]))
        return res
    
    def orderOfLargestPlusSignFirstSolution(self, N, M):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        B = [[1 for _ in xrange(N)] for _ in xrange(N)]
        for mine in M:
            r,c = tuple(mine)
            B[r][c] = 0
        res = 0
        for i in xrange(N):
            for j in xrange(N):
                if B[i][j]: res = max(res, self.dfs(B, i, j, N))
        return res
    
    def dfs(self, B, i, j, N):
        Ui, Di = i-1, i+1
        Lj, Rj = j-1, j+1
        res = 1
        while Ui >= 0 and Di < N and Lj >= 0 and Rj < N and B[Ui][j] and B[Di][j] and B[i][Lj] and B[i][Rj]:
            res += 1
            Ui -= 1
            Di += 1
            Lj -= 1
            Rj += 1
        return res
