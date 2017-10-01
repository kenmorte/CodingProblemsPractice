# https://leetcode.com/problems/array-partition-i/description/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        result = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result += sorted_nums[i]
        return result
        
