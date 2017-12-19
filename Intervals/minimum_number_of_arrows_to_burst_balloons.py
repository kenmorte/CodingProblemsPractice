# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution(object):
    def findMinArrowShots(self, A):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not A: return 0
        A.sort(key=lambda I: I[0])
        curr, res = A[0], 1
        for I in A[1:]:
            if curr[0] <= I[0] and I[0] <= curr[1]:
                curr = [max(curr[0], I[0]), min(curr[1], I[1])]
            else:
                curr = I
                res += 1
        return res
