# https://leetcode.com/problems/find-right-interval/description/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start_indices = {intervals[i].start:i for i in xrange(len(intervals))}
        starts = sorted(start_indices.keys())
        res = []
        for interval in intervals:
            end = interval.end
            index = -1
            
            # Binary search for this end in our starts
            L, R = 0, len(starts)-1
            while L < R:
                M = (L+R)//2
                if starts[M] < end: L = M+1
                else: R = M
                    
            if starts[L] >= end: index = start_indices[starts[L]]
            res.append(index)
        return res
            
            
