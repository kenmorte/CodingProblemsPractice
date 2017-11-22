# https://leetcode.com/problems/merge-intervals/description/
# Asked by Palantir 11/21

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals.sort(key=lambda interval: interval.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            is_overlapping = interval.start <= res[-1].end
            if is_overlapping: res[-1].end = max(res[-1].end, interval.end)
            else: res.append(interval)
        return res
