# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) // 2]
        result = 0
        for num in nums:
            result += abs(median - num)
        return result
        
