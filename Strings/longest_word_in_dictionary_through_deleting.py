# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

class Solution(object):
    def findLongestWord(self, S, D):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not S or not D: return ''
        res = ''
        for w in D:
            if self.isValid(S, w):
                if len(w) > len(res): res = w
                elif len(w) == len(res): res = min(w, res)
        return res
    
    def isValid(self, S, W):
        if not W or not S or len(W) > len(S): return False
        i = 0
        for c in S:
            if c == W[i]:
                i += 1
                if i == len(W): return True
        return False
