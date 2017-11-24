# https://leetcode.com/problems/container-with-most-water/description/

class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        if not h: return 0
        L, R = 0, len(h)-1
        res = 0
        while L < R:
            res = max(res, min(h[L],h[R])*(R-L))
            if h[L] < h[R]: L += 1
            else: R -= 1
        return res
