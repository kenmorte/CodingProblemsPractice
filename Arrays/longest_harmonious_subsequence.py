# https://leetcode.com/problems/longest-harmonious-subsequence/description/

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        res = 0
        for n in count:
            if n-1 in count: res = max(res, count[n] + count[n-1])
        return res
            
