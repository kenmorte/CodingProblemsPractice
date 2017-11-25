# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor, res = 5, 0
        curr = n // factor
        while curr != 0:
            res += curr
            factor *= 5
            curr = n//factor
        return res
