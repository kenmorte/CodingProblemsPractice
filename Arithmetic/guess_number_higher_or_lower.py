# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L < R:
            M = (L+R)//2
            if guess(M) > 0: L = M+1
            else: R = M
        return L
        
