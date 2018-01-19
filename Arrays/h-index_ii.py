# https://leetcode.com/problems/h-index-ii/description/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        if not citations[-1]: return 0
        if len(citations) == 1: return 0 if not citations[0] else 1
        L, R = 0, len(citations)-1
        while L != R:
            M = (L+R)//2
            H = len(citations) - M
            if H > citations[M]: L = M+1
            else: R = M
        return len(citations) - L
