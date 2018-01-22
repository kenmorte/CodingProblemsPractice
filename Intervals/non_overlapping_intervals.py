# https://leetcode.com/problems/non-overlapping-intervals/description/

import functools

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        interval_key = lambda i1, i2: i1.start - i2.start if i1.start != i2.start else i1.end - i2.end
        intervals.sort(key=functools.cmp_to_key(interval_key))
        cnt = 0
        i = 0
        while i < len(intervals):
            j = i+1
            while j < len(intervals) and intervals[j].start < intervals[i].end:
                cnt += 1
                if intervals[i].end > intervals[j].end: break
                else: j += 1
            i = j
        return cnt
