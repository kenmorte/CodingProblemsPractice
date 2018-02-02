# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution(object):
    def maxProfit(self, P):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(P) < 2: return 0
        B = [0 for _ in P]
        S = [0 for _ in P]
        S[len(S)-2:] = [max(P[-1], P[-2])]*2
        B[-2] = max(B[-1], S[-1] - P[-2])
        for i in xrange(len(B)-3,-1,-1):
            S[i] = max(S[i+1], P[i] + B[i+2])
            B[i] = max(B[i+1], S[i+1] - P[i])
        return B[0]
