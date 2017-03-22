# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            to_sum = target - nums[i]
            
            if to_sum in num_indices:
                if num_indices[to_sum] == i:
                    continue
                
                return [i, num_indices[to_sum]]
            
