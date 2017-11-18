# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, d):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not d: return []
        c = [0 for _ in d]
        r = [0 for _ in d]
        c[-1] = 1
        for i in range(len(d)-1, 0, -1):
            s = c[i] + d[i]
            if s > 9: c[i-1] = 1
            else: r[i] = s
        if c[0] == 1 and d[0] == 9: r = [1] + r
        else: r[0] = c[0] + d[0]
        return r
