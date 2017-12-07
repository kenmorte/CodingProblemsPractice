# https://leetcode.com/problems/daily-temperatures/description/

import heapq

class Solution(object):
    def dailyTemperatures(self, T):
        if not T: return []
        if len(T) == 1: return [0]
        S, res = [], [0 for _ in T]
        for i in xrange(len(T)):
            while len(S) and T[i] > T[S[-1]]:
                j = S.pop()
                res[j] = i - j
            S.append(i)
        return res
    
    def dailyTemperaturesFirstSolution(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not T: return []
        if len(T) == 1: return [0]
        H, res = [], [0 for _ in T]
        for i in xrange(len(T)):
            while len(H) and T[i] > H[0][0]:
                j = heapq.heappop(H)[1]
                res[j] = i - j
            heapq.heappush(H, (T[i], i))
        return res
