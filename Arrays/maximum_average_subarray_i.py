# https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution(object):
    def findMaxAverage(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not A: return 0
        curr = sum(A[:k])
        res = curr/float(k)
        ptr = 0
        for n in A[k:]:
            curr = curr - A[ptr] + n
            ptr += 1
            res = max(res, curr/float(k))
        return res
