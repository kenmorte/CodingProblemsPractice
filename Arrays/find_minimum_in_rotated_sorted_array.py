# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, len(nums)-1
        while L < R:
            M = (L+R)//2
            if nums[M] > nums[R]: L = M+1
            else: R = M
        return nums[L]
