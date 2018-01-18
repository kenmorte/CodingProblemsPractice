# https://leetcode.com/problems/set-mismatch/description/
# NOTE: Similar question asked by Google on 12/20/2017

class Solution(object):
    # O(1) space
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup, missing = -1, -1
        for n in nums:
            if nums[abs(n)-1] < 0: dup = abs(n)
            else: nums[abs(n)-1] *= -1
        for i in xrange(len(nums)):
            if nums[i] > 0:
                missing = i+1
                break
        return [dup, missing]
    
    # O(n) space
    def findErrorNumsFirstSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = set()
        dup, missing = -1, -1
        for n in nums:
            if n not in S: S.add(n)
            else: dup = n
        for i in xrange(1,len(nums)+1): 
            if i not in S: 
                missing = i
                break
        return [dup,missing]
