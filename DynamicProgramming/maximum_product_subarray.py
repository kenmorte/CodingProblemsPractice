# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A: return 0
        if len(A) == 1: return A[0]
        T = [(0,0) for _ in A]
        T[0] = (A[0],A[0])
        for i in xrange(1,len(A)):
            a,b,c = A[i], A[i]*T[i-1][0], A[i]*T[i-1][1]
            T[i] = (max(a,b,c),min(a,b,c))
        return max([t[0] for t in T])
