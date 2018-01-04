# https://leetcode.com/problems/task-scheduler/description/

from collections import Counter

class Solution(object):
    def leastInterval(self, T, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not T: return 0
        if len(T) == 1: return 1
        C = Counter(T)
        maxPriority = C[max(C, key=lambda t: C[t])]
        return max(len(T), ((n+1)*(maxPriority-1)) + C.values().count(maxPriority))
