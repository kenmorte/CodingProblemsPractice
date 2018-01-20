# https://leetcode.com/problems/valid-perfect-square/description/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        L, R = 1, num
        while L < R:
            M = (L+R)//2
            if M*M >= num: R = M
            else: L = M+1
        return L*L == num
