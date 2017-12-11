# https://leetcode.com/problems/powx-n/description/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if x == 0: return 0
        if x == 1: return 1
        if n < 0: return 1.0 / self.myPow(x, -n)
        if n < 1000000:
            res = 1
            for i in xrange(n): res *= x
            return res
        else:
            res = self.myPow(abs(x),n//2)
            return (-1 if x < 0 and n%2 == 1 else 1)*res*res
