# https://leetcode.com/problems/optimal-division/description/

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1: return str(nums[0])
        if len(nums) == 2: return str(nums[0]) + '/' + str(nums[1])
        result = str(nums[0]) + '/('
        for num in nums[1:]:
            result += str(num) + '/'
        result = result[:len(result)-1] + ')'
        return result
        
