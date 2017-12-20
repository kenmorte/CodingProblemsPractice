# https://leetcode.com/problems/delete-operation-for-two-strings/description/

class Solution(object):
    def minDistance(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not s1: return len(s2)
        if not s2: return len(s1)
        dp = [[0 for _ in xrange(len(s2)+1)] for _ in xrange(len(s1)+1)]
        dp[0] = [n for n in xrange(len(s2)+1)]
        for i in xrange(len(s1)+1): dp[i][0] = i
        for i in xrange(1,len(s1)+1):
            for j in xrange(1,len(s2)+1):
                if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
