# https://leetcode.com/problems/knight-probability-in-chessboard/description/
# NOTE: Asked by Google 12/20/2017

class Solution(object):
    def knightProbability(self, N, k, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if k == 0: return 1
        table = {}
        return self.P(table, N, k, r, c)
    
    def P(self, T, N, k, r, c):
        if (r,c,k) in T: return T[(r,c,k)]
        moves = self.getValidMoves(N,r,c)
        if k == 1:
            T[(r,c,k)] = len(moves)/8.0
        else:
            res = 0
            for nr, nc in moves:
                res += self.P(T, N, k-1, nr, nc)
            T[(r,c,k)] = res/8.0
        return T[(r,c,k)]
    
    def getValidMoves(self, N, r, c):
        moves = [(r-2,c+1),
                 (r-2,c-1),
                 (r-1,c-2),
                 (r+1,c-2),
                 (r+2,c-1),
                 (r+2,c+1),
                 (r-1,c+2),
                 (r+1,c+2)
                ]
        return [(r,c) for r,c in moves if r >= 0 and r < N and c >= 0 and c < N]
