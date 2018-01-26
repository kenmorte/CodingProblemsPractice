# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 1: return False
        for length in xrange(1,(n//2)+1):
            factor = n//length
            if s[:length]*factor == s: 
                return True
        return False
