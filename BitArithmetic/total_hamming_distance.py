# https://leetcode.com/problems/total-hamming-distance/description/

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        
        all_zero = False
        result = 0
        while not all_zero:
            all_zero = True
            number_of_ones = 0
            number_of_zeros = 0
            
            for i in range(len(nums)):
                if nums[i]: all_zero = False
                if nums[i] & 1: number_of_ones += 1
                else: number_of_zeros += 1
                nums[i] = nums[i] >> 1
            
            result += number_of_ones * number_of_zeros
        
        return result
        
        
