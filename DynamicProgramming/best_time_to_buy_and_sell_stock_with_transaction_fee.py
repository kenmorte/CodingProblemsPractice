# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution(object):
    def maxProfit(self, P, F):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not P: return 0
        B = [-n for n in P]
        S = [0 for _ in P]
        S[0] = float('-inf')
        for i in xrange(1, len(P)):
            B[i] = max(B[i], S[i-1] - P[i], B[i-1])
            S[i] = max(S[i-1], B[i-1] + P[i] - F)
        return max(0, B[-1], S[-1])
