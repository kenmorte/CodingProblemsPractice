# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n== 0: return []
        if n == 1: return [[1]]
        if n == 2: return [[1],[1,1]]
        res = [[1 for _ in range(i+1)] for i in range(n)]
        for i in range(2,n):
            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
