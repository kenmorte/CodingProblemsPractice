# https://leetcode.com/problems/minimum-window-substring/description/

from collections import Counter

class Solution(object):
    def minWindow(self, S, T):
        if not S or not T: return ''
        if len(T) == 1: return T if T in S else ''
        i, j = 0, 0
        Tc, curr, res = Counter(T), Counter(), S+'_'
        while j < len(S):
            while j < len(S) and not self.isValid(curr, Tc):
                if S[j] in Tc: curr[S[j]] += 1
                j += 1
            while i < j and self.isValid(curr, Tc):
                res = min(res, S[i:j], key=len)
                if S[i] in Tc: curr[S[i]] -= 1
                i += 1
            while i < j and S[i] not in Tc:
                i += 1
        return '' if len(res) > len(S) else res
            
    def isValid(self, curr, T):
        if len(curr) < len(T): return False
        for c in curr:
            if curr[c] < T[c]: return False
        return True
