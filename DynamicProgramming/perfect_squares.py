# https://leetcode.com/problems/perfect-squares/description/

import math

class Solution(object):
    def __init__(self):
        self.table = {0:0, 1:1}
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.table: return self.table[n]
        range_sq = int(math.sqrt(n))
        res = n
        for i in range(2, range_sq+1):
            sq = i*i
            num_sq = n // sq
            res = min(res, num_sq + self.numSquares(n-(sq*num_sq)))
        self.table[n] = res
        return res
