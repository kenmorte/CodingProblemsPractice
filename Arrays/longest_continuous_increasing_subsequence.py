# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = 1
        length = 1
        for i in xrange(1,len(nums)):
            if nums[i] > nums[i-1]: length += 1
            else:
                res = max(res, length)
                length = 1
        return max(res, length)
