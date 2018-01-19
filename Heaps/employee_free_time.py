# https://leetcode.com/problems/employee-free-time/description/

from heapq import heappush, heappop

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, S):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        if len(S) == 1: return []
        
        heap = []
        merged = []
        
        for id,E in enumerate(S): 
            heappush(heap, (E[0].start, id, 0))
        
        while heap:
            start, id, index = heappop(heap)
            interval = S[id][index]
            
            if not merged: 
                merged += [interval]
            elif merged[-1].start <= start and start <= merged[-1].end: 
                merged[-1] = Interval(merged[-1].start, max(interval.end, merged[-1].end))
            else: merged += [interval]
            
            index += 1
            if index < len(S[id]): heappush(heap, (S[id][index].start, id, index))
            
        return [Interval(merged[i-1].end, merged[i].start) for i in xrange(1,len(merged))]
