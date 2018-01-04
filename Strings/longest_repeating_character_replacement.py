# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s: return 0
        if k >= len(s): return len(s)
        res = 0
        for L in set(s):
            index = s.index(L)
            if index < 0: continue
            i, j = max(0, index-k), index
            kLeft = k - (j - i)
            while j < len(s):
                while j < len(s) and (kLeft or s[j] == L):
                    if s[j] != L: kLeft -= 1
                    j += 1
                res = max(res, j-i)
                while i < len(s) and s[i] == L: i += 1
                while i < len(s) and s[i] != L:
                    i += 1
                    kLeft = min(kLeft+1, k)
                j = max(j, i)
        return res
