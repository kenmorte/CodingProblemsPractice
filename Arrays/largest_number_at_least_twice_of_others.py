# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # One pass
        index = 0
        largest = nums[0]
        secondLargest = float('-inf')
        for i,n in enumerate(nums[1:],1):
            if n > largest:
                secondLargest = largest
                largest = n
                index = i
            elif n > secondLargest: secondLargest = n
        return -1 if secondLargest*2 > largest else index
        
        # Two passes
        # m = max(nums)
        # mi = nums.index(m)
        # for i in xrange(len(nums)):
        #     if i != mi and nums[i]*2 > m: return -1
        # return mi
