# https://leetcode.com/problems/max-consecutive-ones/#/description

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,1,0,1,1,1]
        max_global = 0
        max_so_far = 0
        
        for num in nums:
            if num:
                max_so_far += 1
            else:
                max_so_far = 0
            
            if max_so_far > max_global:
                max_global = max_so_far
        
        return max_global
