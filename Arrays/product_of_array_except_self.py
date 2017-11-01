# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        factor = 1
        t = []
        b = []
        
        for num in nums:
            factor *= num
            t.append(factor)
            
        factor = 1
        for num in nums[::-1]:
            factor *= num
            b.append(factor)
        b = list(reversed(b))
            
        result = []
        t_index = -1
        b_index = 1
        while len(result) < len(nums):
            t_val = t[t_index] if t_index >= 0 else 1
            b_val = b[b_index] if b_index < len(b) else 1
            result.append(t_val * b_val)
            
            t_index += 1
            b_index += 1
        return result
            
