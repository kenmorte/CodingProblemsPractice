# https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/

from collections import Counter

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return 0
        firstBiggest, secondBiggest, thirdBiggest = float('-inf'), float('-inf'), float('-inf')
        firstSmallest, secondSmallest = float('-inf'), float('-inf')
        C = Counter(nums)
        
        firstBiggest = max(C)
        C[firstBiggest] -= 1
        if not C[firstBiggest]: del C[firstBiggest]
            
        secondBiggest = max(C)
        C[secondBiggest] -= 1
        if not C[secondBiggest]: del C[secondBiggest]
            
        thirdBiggest = max(C)
        C[thirdBiggest] -= 1
        if not C[thirdBiggest]: del C[thirdBiggest]
            
        if not C: return firstBiggest*secondBiggest*thirdBiggest
            
        firstSmallest = min(C)
        C[firstSmallest] -= 1
        if not C[firstSmallest]: del C[firstSmallest]
            
        if not C: return firstBiggest*secondBiggest*thirdBiggest
            
        secondSmallest = min(C)
        C[secondSmallest] -= 1
        if not C[secondSmallest]: del C[secondSmallest]
            
        return max(firstBiggest*secondBiggest*thirdBiggest, firstBiggest*firstSmallest*secondSmallest)
    
    def maximumProductFirstSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return 0
        A = sorted(nums)
        return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[2], A[-1]*A[0]*A[1])
