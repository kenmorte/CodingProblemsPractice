# https://leetcode.com/problems/longest-palindrome/description/

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        T = Counter(s)
        res = 0
        for c in T:
            if T[c]%2 == 0:
                res += T[c]
                T[c] = 0
            else:
                res += T[c] - 1
                T[c] = 1
        return res + max(T.values())
