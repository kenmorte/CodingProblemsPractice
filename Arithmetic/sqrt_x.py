# https://leetcode.com/problems/sqrtx/description/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x == 1: return 1
        L, R = 1, x
        M = (L+R)//2
        while L != R:
            M = (L+R)//2
            Msquared = M*M
            if Msquared == x: return M
            if Msquared < x: L=M+1
            if Msquared > x: R=M
        if M*M > x: M -= 1
        return M
