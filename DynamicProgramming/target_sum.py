# https://leetcode.com/problems/target-sum/description/

class Solution(object):
    def findTargetSumWays(self, A, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not A: return 0
        if len(A) == 1: return 1 if A[0] == abs(S) else 0
        s = sum(A)
        if S > s: return 0
        dp = [[0 for _ in xrange(2*s+1)] for _ in A]
        dp[0] = [(2 if A[0] == 0 else 1)*1 if abs(n) == A[0] else 0 for n in xrange(-s,s+1)]
        for i in xrange(1,len(A)):
            for j in xrange(2*s+1):
                plus = dp[i-1][j-A[i]] if j-A[i] >= 0 else 0
                minus = dp[i-1][j+A[i]] if j+A[i] < 2*s+1 else 0
                dp[i][j] = plus + minus
        return dp[-1][s+S]
