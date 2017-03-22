# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
#   For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return 0
            
        result = 0 if nums[0] > nums[1] else len(nums) - 1 if nums[-1] > nums[-2] else -1
        
        for i in range(1, len(nums)-1):
            left = nums[i-1]
            mid = nums[i]
            right = nums[i+1]
            
            if mid > left and mid > right:
                result = i
        return result
