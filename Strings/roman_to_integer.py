# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        is_special = lambda s: s in {'IV','IX','XL','XC','CD','CM'}
        v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i, res = 0, 0
        while i < len(s):
            c = s[i]
            n_c = s[i+1] if i+1 < len(s) else ''
            if is_special(c+n_c):
                res += v[n_c] - v[c]
                i += 2
            else:
                res += v[c]
                i+= 1
        return res
