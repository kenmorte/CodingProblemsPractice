# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        k = len(s1)
        C1, C2 = Counter(s1), Counter(s2[:k])
        for i in xrange(k, len(s2)):
            if C1 == C2: return True
            C2[s2[i-k]] -= 1
            if not C2[s2[i-k]]: del C2[s2[i-k]]
            C2[s2[i]] += 1
        return C1 == C2
