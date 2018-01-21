# https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        sumLeft = 0
        sumRight = sum(nums)
        for i,n in enumerate(nums):
            sumRight -= n
            if sumLeft == sumRight: return i
            sumLeft += n
        return -1
            
            
        
        # O(n) space
#         if not nums: return -1
#         presum = [0]
#         for n in nums:
#             presum += [presum[-1]+n]
#         presum += [0]
#         for i in xrange(1,len(nums)+1):
#             sumLeft = presum[i-1]
#             sumRight = presum[-2] - presum[i]
#             if sumLeft == sumRight: return i-1
#         return -1
    
        
