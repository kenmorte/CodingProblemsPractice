# https://leetcode.com/problems/range-addition-ii/description/

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        
        r, c = tuple(ops[0])
        for op in ops:
            r = min(r, op[0])
            c = min(c, op[1])
        return r*c
