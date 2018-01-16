# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0: return []
        if n == 1: return [[1]]
        M = [[0 for _ in xrange(n)] for _ in xrange(n)]
        maxR, maxD, maxL, maxU = n-1, n-1, 0, 1
        count, nSq = 1, n*n
        x, y = 0, 0
        dx, dy = 1, 0
        while count <= nSq:
            M[y][x] = count
            if x == maxR and dx == 1: dx, dy, maxR = 0, 1, maxR-1
            elif x == maxL and dx == -1: dx, dy, maxL = 0, -1, maxL+1
            elif y == maxD and dy == 1: dx, dy, maxD = -1, 0, maxD-1
            elif y == maxU and dy == -1: dx, dy, maxU = 1, 0, maxU+1
            count += 1
            x, y = x+dx, y+dy
        return M
                
