# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in B] for _ in A]
        res = 0
        for j in xrange(len(B)):
            if A[0] == B[j]: dp[0][j] = 1
        for  i in xrange(len(A)):
            if A[i] == B[0]: dp[i][0] = 1
        for i in xrange(1,len(A)):
            for j in xrange(1,len(B)):
                if A[i] == B[j]: 
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        return res
