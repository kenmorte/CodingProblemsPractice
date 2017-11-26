# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not m: return
        rs, cs = set(), set()
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] == 0:
                    rs.add(r)
                    cs.add(c)
        for r in rs: m[r] = [0 for _ in m[r]]
        for c in cs:
            for r in range(len(m)):
                m[r][c] = 0
