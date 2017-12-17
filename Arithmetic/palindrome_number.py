# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, n):
        """
        :type x: int
        :rtype: bool
        """
        if not n: return True
        copyn = abs(n)
        factor = 1
        while copyn >= 10:
            factor *= 10
            copyn /= 10
        copyn = abs(n)
        newn = 0
        # print factor
        while copyn:
            newn += (copyn % 10) * factor
            copyn /= 10
            factor /= 10
        # print newn, n
        return newn == n
