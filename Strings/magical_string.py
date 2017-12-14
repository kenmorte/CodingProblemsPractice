# https://leetcode.com/problems/magical-string/description/

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 0
        if n < 4: return 1
        S = [1,2,2]
        H, mark, res = 2, 1, 1
        while H < n:
            S += [mark] * S[H]
            res += 1 if S[H] == 1 else 0
            mark = 1 if mark == 2 else 2
            H += 1
        return res
