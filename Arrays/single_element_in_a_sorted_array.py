# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        L = 0
        R = len(nums) - 1
        
        while R - L > 2:
            M = (L + R) // 2
            
            if abs(L-M) % 2 == 0: # Difference between left and mid index is even
                if nums[M] == nums[M-1]:
                    R = M
                elif nums[M] == nums[M+1]:
                    L = M
                else: # Middle number is unique
                    return nums[M]
                
            else: # Difference between left and mid index is odd
                if nums[M] == nums[M-1]:
                    L = M + 1
                elif nums[M] == nums[M+1]:
                    R = M - 1
                else: # Middle number is unique
                    return nums[M]
            
        M = (L + R) // 2
        if nums[M] == nums[L]:
            return nums[R]
        if nums[M] == nums[R]:
            return nums[L]
        return nums[M]
