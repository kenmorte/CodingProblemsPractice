# https://leetcode.com/problems/sum-of-square-numbers/description/

from math import sqrt

class Solution(object):
    def judgeSquareSum(self, n):
        """
        :type c: int
        :rtype: bool
        """
        for a in xrange(int(sqrt(n))+1):
            bSquared = n - (a*a)
            if bSquared < 0: continue
            sqrtB = sqrt(bSquared)
            if int(sqrtB) == sqrtB: return True
        return False
