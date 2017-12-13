# https://leetcode.com/problems/minimum-time-difference/description/

from collections import Counter

class Solution(object):
    def findMinDifference(self, times):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(times) < 2: return 0
        C = Counter(times)
        for t in C:
            if C[t] > 1: return 0
        S = set(times)
        T = sorted(self.convert(time) for time in S)
        res = float('inf')
        for i in xrange(1,len(T)):
            res = min(res, T[i] - T[i-1])
        return min(res, T[-1]-T[0], T[0]-T[-1]+1440)
        
    def convert(self, time):
        H, M = tuple(time.split(':'))
        return int(M) + (60*int(H))
