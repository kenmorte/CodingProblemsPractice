# https://leetcode.com/problems/is-subsequence/description/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        if not t: return False
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s): return True
        return False
