# https://leetcode.com/problems/degree-of-an-array/description/

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        degree = 0
        occurrence_map = dict()
        
        for num in nums:
            if num not in occurrence_map:
                occurrence_map[num] = 1
            else:
                occurrence_map[num] += 1
            degree = max(degree, occurrence_map[num])
        
        degree_map = dict()
        for num in occurrence_map:
            if occurrence_map[num] == degree:
                degree_map[num] = []
        
        for i in range(len(nums)):
            num = nums[i]
            if num in degree_map:
                degree_map[num].append(i)
                
        result = float('inf')
        for num in degree_map:
            result = min(result, (degree_map[num][-1] - degree_map[num][0]) + 1)
        
        return result
                
        
