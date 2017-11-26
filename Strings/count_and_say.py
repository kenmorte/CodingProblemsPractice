# https://leetcode.com/problems/count-and-say/description/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ''
        if n == 1: return '1'
        res, pres = '', self.countAndSay(n-1)
        prev, count = pres[0], 0
        for c in pres:
            if c == prev: count += 1
            else:
                res += str(count) + prev
                prev = c
                count = 1
        return res + str(count) + prev
